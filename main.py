from data_transform.WE_transform import WE_transform as wet
from revenue.revenue import Revenue as rev
from revenue.revenue import WE_income_items as weii
# from report_outlook.report_outlook_positioning import Report_outlook_positioning as rop
import pandas as pd
import xlwings as xw
import time
from report_outlook.report_template import Report_template as rt

# Fixed as Weds to Tues
# Start with df, suppose it is querying from Wed
# dataframe in new downloaded folder
# dataVault\waste_edge_booking_data\23.12.2020_to_26.1.2021
path = "../../dataVault/waste_edge_booking_data/23.12.2020_to_26.1.2021.csv"

df = pd.read_csv(path)
# df.drop(columns=['Schd Time Start','PO'])
# =================================================================================
# ==============Transform the dataframe==========================

# Make sure column Route Number
df['Route number'] = df['Route number'].astype('str')
# Clean Route number data from dash weekday  e.g. BR1-1
# Extract the day number and assign it to a new column

df = wet().extract_weekday(df)
# Clean Route number column
df = wet().clean_route_num_column(df)
# Transform date to date index for resample purposes
df = wet().transform_date_format(df)
# Sort df by date Value desc


# =================================================================================
# Seperate Dataframe by 7 days
series = df.resample('7D')
# Weekly - create excel file per 7 Days
series_keys = series.Price.sum().keys()

# created name
# create the condiitons for creating

# ================================================================================
rev_types = ['total', 'general_waste', 'cardboard',
             'comingled', 'subContractor', 'uos']
list_of_worksheet = ['total', 'general_waste', 'cardboard',
                     'comingled', 'subContractor', 'uos', 'weekly_fr']
# else:
# series[0]
# df_date = series_keys["2021-01-13"]
dates = rev(df).get_dates()
# must not be string dates[-1], since its a key for extracting dataset
current_report_date = dates[-1]

# [x for x in lst if 'abc' in x]
rev_types_inc = [rev(df).get_income_by_rev_type(
    rev_type, current_report_date) for rev_type in rev_types]

routes_inc = [rev(df).get_income_per_route_by_rev_type(rev_type, current_report_date)
              for rev_type in rev_types]


weii_obj = weii(rev_types_inc[0], rev_types_inc[1], rev_types_inc[2],
                rev_types_inc[3], rev_types_inc[4], rev_types_inc[5])

wb = xw.Book()
rt().add_sheets(wb, list_of_worksheet)

# list compre
# [s for s in my_list if any(xs in s for xs in matchers)]
# Paul report
current_report_date_title = "Date : " + str(current_report_date)
rt().paul_weekly_fr1(wb, "weekly_fr", current_report_date_title, weii_obj)

# df_date = "2021-01-20"
# df_series = series.get_group(df_date)

# rop.create_and_name_ws_by_routes(wb, rev_types)
# [report_templates_horizontal(wb,rev_type,df_series,df_date) for rev_type in rev_types]


# /D/'Run Analysis'/'WEEKLY SUMMARY from January 2021'/'January 2021/Weekly Summary'