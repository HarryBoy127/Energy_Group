import logging
import yaml
import os
from datetime import datetime
import pandas as pd
from src.s3_utils import (
    s3_fetcher,
    s3_uploader
) 
from src.data_cleaning import (
    selected_columns,
    rename_columns,
    drop_columns,
    fix_data_types_columns,
    clean_textual_column
)


# Load configuration files
with open("./conf/config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

# Setup logging
log_dir = os.path.join(os.path.dirname(__file__), 'logs')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_filename = os.path.join(log_dir, f"logs_{datetime.now().strftime('%d%m%Y')}.log")
logging.basicConfig(filename=log_filename, level=logging.INFO, format=config['logging']['format'])
logger = logging.getLogger(__name__)

def run_etl():
    logger.info("Pipeline started.")
    
    # Extract: 
    # Step 1 - Extract energy raw from s3 bucket
    energy_raw = s3_fetcher(
                    bucket = "tkh-nyc-energy",    
                    object_key = 'energy_raw_06032024.csv'
                )
    
    # Transform: 
    # Step 2: selected columns
    energy_raw_selected_columns = selected_columns(energy_raw)
    
    # Step 3: rename columns
    energy_rename_column = rename_columns(energy_raw_selected_columns)
    
    # Step 4: drop columns
    energy_drop_columns = drop_columns(energy_rename_column)
    
    # Step 5: fix data types columns
    energy_fix_data_types_column = fix_data_types_columns(energy_drop_columns)

    # Step 6: clean textual column
    energy_clean_textual_column = clean_textual_column(energy_fix_data_types_column)
    
    # Step 6: clean textual column
    energy_clean_textual_column = clean_textual_column(energy_fix_data_types_column)
    
    # Step 7: save cleaned data on local
    energy_clean_textual_column
    
    # Step 8: Save to clean data 
    energy_clean_textual_column.to_csv('./data/processed/energy_clean.csv', index = False)
    
    # Load:
    # Step 7: Data Loading
    s3_uploader(
            selection = 'cleaned', 
            bucket = "tkh-nyc-energy/cleaned-zone",
            file_path = './data/processed/energy_clean.csv'
        )

    logger.info("Pipeline finished successfully.")

if __name__ == "__main__":
    run_etl()
