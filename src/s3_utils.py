import io
import boto3
import pandas as pd
import logging
import yaml
from datetime import datetime

# Load configuration files
with open("./conf/config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

logger = logging.getLogger(__name__)

def s3_uploader(selection='raw', bucket="tkh-nyc-energy", file_path='../data/processed/energy_clean.csv'):
    current_date = datetime.now().strftime("%m%d%Y")

    if selection == 'raw':
        local_file = file_path
        name_s3_file = f"energy_raw_{current_date}.csv"
        s3 = boto3.resource('s3')
        try:
            s3.meta.client.upload_file(local_file, bucket, name_s3_file)
            logger.info(f"Successfully uploaded {local_file} to {bucket}/{name_s3_file}")
        except Exception as e:
            logger.error(f"Failed to upload {local_file} to {bucket}/{name_s3_file}: {e}")

    elif selection == 'cleaned':
        local_file = file_path
        name_s3_file = f"energy_cleaned_{current_date}.csv"
        s3 = boto3.resource('s3')
        try:
            s3.meta.client.upload_file(local_file, bucket, name_s3_file)
            logger.info(f"Successfully uploaded {local_file} to {bucket}/{name_s3_file}")
        except Exception as e:
            logger.error(f"Failed to upload {local_file} to {bucket}/{name_s3_file}: {e}")

    else:
        logger.error(f"Invalid selection: {selection}")
        return False

def s3_fetcher(bucket="tkh-nyc-energy", object_key='energy_raw_06032024.csv'):
    client = boto3.client('s3')

    try:
        response = client.get_object(Bucket=bucket, Key=object_key)
        data = response['Body'].read()
        df = pd.read_csv(io.BytesIO(data))
        logger.info(f"Successfully fetched {object_key} from {bucket}")
        return df
    except Exception as e:
        logger.error(f"Failed to fetch {object_key} from {bucket}: {e}")
        return None
