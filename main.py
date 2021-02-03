# data Transform - waste Edge
from data_transform.WE_transform import WE_transform as dt_wet
from revenue.revenue import Revenue as rev
from revenue.rev_types import Rev_types 
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

df = pd.read_csv(path, dtype={"Schd Time Start" : str, "PO" : str})

# Transform
trans_df = dt_wet().transform_and_clean_Route_num(df)
trans_df = dt_wet().transform_date(df)

# resample df by 7D  
resampled_df = rev().resample_by_7d(trans_df)

date_keys = rev().date_keys(resampled_df)

current_date = date_keys[0]


print(current_date)
current_ = rev().get_df_by(resampled_df,current_date)

Revenue_by_type()


# # dates 
# weekly_dfs_key = list(weekly_dfs.groups.keys())


# # ================================================================================
# rev_types = ['total', 'general_waste', 'cardboard',
#              'comingled', 'subContractor', 'uos']

# list_of_worksheet = ['total', 'general_waste', 'cardboard',
#                      'comingled', 'subContractor', 'uos', 'weekly_fr']
# # else:
# # series[0]
# # df_date = series_keys["2021-01-13"]
# dates = rev(df).get_dates()
# # print(dates)

# # (['2020-12-23', '2020-12-30', '2021-01-06', '2021-01-13','2021-01-20']

# # must not be string dates[-1], since its a key for extracting dataset
# current_report_date = dates[3]

# # [x for x in lst if 'abc' in x]
# rev_types_inc = [rev(df).get_income_by_rev_type(
#     rev_type, current_report_date) for rev_type in rev_types]

# routes_inc = [rev(df).get_income_per_route_by_rev_type(rev_type, current_report_date)
#               for rev_type in rev_types]


# weii_obj = weii(rev_types_inc[0], rev_types_inc[1], rev_types_inc[2],
#                 rev_types_inc[3], rev_types_inc[4], rev_types_inc[5])

# wb = xw.Book()
# rt().add_sheets(wb, list_of_worksheet)

# # list compre
# # [s for s in my_list if any(xs in s for xs in matchers)]
# # Paul report
# current_report_date_title = "Date : " + str(current_report_date)
# rt().paul_weekly_fr1(wb, "weekly_fr", current_report_date_title, weii_obj)


# # wb.save(f'D:\\Run Analysis\\WEEKLY_SUMMARY_from_January_2021\\January_2021\\Weekly_Summary\\{str(current_report_date)}.xlsx')
# # wb.close()
