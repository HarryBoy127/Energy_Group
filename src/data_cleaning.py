def test_drop_columns():
    print("this is working")

def selected_columns(df):
    df_selected_column = df[["borough", "account_name","serial_number","funding_origin","total_bill",
                                     'kwh_consumption','kwh_bill', 'kw_consumption', 'kw_bill',
                                     "year_month","start_date", "end_date"]]
    return df_selected_column

def rename_columns(df):
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
    return df_rename

def drop_columns(df):
    columns = ["Start_Date","End_Date"]
    df_drop = df.dropna(subset=columns)
    return df_drop



