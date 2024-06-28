import logging
import yaml
import pandas as pd

# Load configuration files
with open("./conf/config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

logger = logging.getLogger(__name__)

def selected_columns(df):
    logger.info("Selecting specific columns from the DataFrame.")
    df_selected_column = df[["borough", "account_name","serial_number","funding_origin","total_bill",
                                     'kwh_consumption','kwh_bill', 'kw_consumption', 'kw_bill',
                                     "year_month","start_date", "end_date"]]
    logger.info("Selected columns: %s", df_selected_column.columns.tolist())
    return df_selected_column

def rename_columns(df):
    logger.info("Renaming columns of the DataFrame.")
    rename_dict = {
        "borough": "Borough", 
        "account_name": "Account_Name",
        "serial_number": "Serial_Number",
        "funding_origin": "Funding_Origin",
        "total_bill": "Total_Bill",
        "year_month": "Year_Month",
        "kwh_consumption": "KWH_Consumption", 
        "kwh_bill": "KWH_Bill",
        "kw_consumption": "KW_Consumption",
        "kw_bill": "KW_Bill",
        "start_date": "Start_Date",
        "end_date": "End_Date"
    }
    
    df_rename = df.rename(columns=rename_dict)
    logger.info("Renamed columns: %s", df_rename.columns.tolist())
    return df_rename

def drop_columns(df):
    logger.info("Dropping columns with NaN values in 'Start_Date' and 'End_Date'.")
    columns = ["Start_Date", "End_Date"]
    df_drop = df.dropna(subset=columns)
    logger.info("Remaining columns after drop: %s", df_drop.columns.tolist())
    return df_drop

def fix_data_types_columns(df):
    logger.info("Fixing data types of specific columns.")
    df['Start_Date'] = pd.to_datetime(df['Start_Date'])
    df['End_Date'] = pd.to_datetime(df['End_Date'])

    df['Year_Month'] = df['Year_Month'].astype(str) + '-01'
    df['Year_Month'] = pd.to_datetime(df['Year_Month'])

    float_columns = ["Total_Bill", "KWH_Consumption", "KW_Consumption", "KW_Bill", "KWH_Bill"]
    df[float_columns] = df[float_columns].astype(float)
    logger.info("Data types fixed for columns: %s", float_columns)
    return df

def clean_textual_column(df):
    logger.info("Cleaning textual columns: 'Borough', 'Account_Name', 'Funding_Origin'.")
    columns = ["Borough", "Account_Name", "Funding_Origin"]
    for column in columns:
        df[column] = df[column].str.strip()
        df[column] = df[column].str.replace(r'\s+', ' ', regex=True)
        df[column] = df[column].str.replace(r'[^\w\s]', ' ', regex=True)
    logger.info("Textual columns cleaned.")
    return df
