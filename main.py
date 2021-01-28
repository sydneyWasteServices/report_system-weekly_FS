from data_transform.WE_transform import WE_transform as wet
from revenue.revenue import Revenue as rev
from report_outlook.report_outlook_positioning import Report_outlook_positioning as rop
import pandas as pd
import xlwings as xw
import time

# Fixed as Weds to Tues

# Start with df, suppose it is querying from Wed
# dataframe in new downloaded folder 
# dataVault\waste_edge_booking_data\23.12.2020_to_26.1.2021
path = "../../dataVault/waste_edge_booking_data/23.12.2020_to_26.1.2021.csv"

df = pd.read_csv(path)

rev_types = ['total','general_waste', 'cardboard', 'comingled', 'subContractor', 'uos']

# =================================================================================
# ==============Transform the dataframe==========================

# Make sure column Route Number
df['Route number'] = df['Route number'].astype('str')
# Clean Route number data from dash weekday  e.g. BR1-1
    # Extract the day number and assign it to a new column  
df = wet.extract_weekday(df)
    # Clean Route number column 
df = wet.clean_route_num_column(df)
# Transform date to date index for resample purposes
df = wet.transform_date_format(df)
# Sort df by date Value desc 


# =================================================================================
# Seperate Dataframe by 7 days
series = df.resample('7D') 
# Weekly - create excel file per 7 Days  
series_keys = series.Price.sum().keys()

# created name 
# create the condiitons for creating  

# ======================================================

# else:
# series[0]
# df_date = series_keys["2021-01-13"]
df_date = "2021-01-20"
df_series = series.get_group(df_date)
wb = xw.Book()
rop.create_and_name_ws_by_routes(wb, rev_types)    

[report_templates_horizontal(wb,rev_type,df_series,df_date) for rev_type in rev_types]



# wb workbook,   series resmapled data (by 7D)


# try catch on excel configuring
# =============================
# wb = xw.Book()
# rop.format_ws_font_style_to_arial(wb,"Sheet1")
# rop.format_headers(wb,"Sheet1")
# rop.format_left_columns(wb,"Sheet1")
# rop.format_report_content_total_income(wb,"Sheet1")
# rop.format_report_content_rev_by_route_num(wb,"Sheet1",[[1],[2],[3]],[[4],[5],[6]])
# =============================

# time.sleep(5)
# wb.close()
# df = wet.extract_weekday(df)
# df = wet.clean_route_num_column(df)
# rev_general_waste = rev.extract_by_rev_type_hardcode('general_waste')

# df = df[df['Route number'].isin(rev_general_waste)]

# df = wet.transform_date_format(df)

# df = df.sort_values(by=['Date'], inplace=True, ascending=False)


# series = df.resample('7D')
# 
# df_123 = series.get_group('2020-12-02')

# print(series.Price.sum())
# print(df)
# print(df)

