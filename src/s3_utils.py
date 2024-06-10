import io
import boto3
import pandas as pd
from datetime import datetime

def s3_uploader(
    selection = 'raw', 
    bucket = "tkh-nyc-energy",    
    file_path = '../data/processed/energy_clean.csv',
    object_key = 'energy_raw_06032024.csv'
):
    current_date = datetime.now().strftime("%m%d%Y")

    if selection == 'raw':
        local_file = file_path
        name_s3_file = f"energy_raw_{current_date}.csv"
        s3 = boto3.resource('s3')
        s3.meta.client.upload_file(local_file, bucket, name_s3_file)
        print(f"Successfully uploaded {local_file} to {bucket}/{name_s3_file}")
        
    elif selection == 'cleaned':
        local_file = file_path
        name_s3_file = f"energy_cleaned_{current_date}.csv"
        s3 = boto3.resource('s3')
        s3.meta.client.upload_file(local_file, bucket, name_s3_file)
        print(f"Successfully uploaded {local_file} to {bucket}/{name_s3_file}")
 
    else:
        print(f"Invalid selection: {selection}")
        return False 
    
def s3_fetcher(
    bucket = "tkh-nyc-energy",    
    object_key = 'energy_raw_06032024.csv'
):
    # open client
    client = boto3.client('s3')

    ### DOWNLOADING SINGLE OBJECTS FROM A BUCKET ###
    response = client.get_object(
        Bucket=bucket,
        Key=object_key,
    )

    # read in data from request
    data = response['Body'].read() 
    df = pd.read_csv(io.BytesIO(data))
    return df
    