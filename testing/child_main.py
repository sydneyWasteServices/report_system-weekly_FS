# os.path.dirname(__file__) just gives you the directory that your current python file is in,
#  and then we navigate to 'Common/' the directory and import 'Common' the module.

import sys, os
sys.path.append(sys.path[0] + "/..")
from routes_tipping.routes_tipping import Routing_tipping

from revenue.revenue import Revenue as rev
from data_transform.WE_transform import WE_transform as dt_wet
from revenue.revenue_by_type import Revenue_by_type
from data.rate import Rate
import pandas as pd

rateObj = Rate(1,2,3,4)

# , 'ORGANICS'
tiplist = ['GENERAL_WASTE', 'CARDBOARD', 'COMINGLED']

path = '../../../ubuntuShareDrive/Datasets/tipping_data/TipRecords_17.02.2021_23.02.2021.csv'
df = pd.read_csv(path)

df['Route No'] = df['Route No'].astype('str')
df[['Route No', 'weekday']] = df['Route No'].str.split('-', 1, expand=True)

routes_tip_df = Routing_tipping(df)

series_a = [routes_tip_df.route_weight_series(tip) for tip in tiplist]

print(series_a[1].index)

# a = Routing_tipping()
# df = a.drop_no_docket(df)
# route_tip_df = a.transform(df)

# route_tip = Routing_tipping(route_tip_df).routes_weight('CARDBOARD')

# diff = Routing_tipping(route_tip_df).routes_diff('CARDBOARD')

# print(route_tip)

# list_rev_types = ['TOTAL', 'GENERAL_WASTE',
#                   'CARDBOARD', 'COMINGLED', 'SUBCONTRACTED', 'UOS']

# list_report_sheets = ['WEEKLY_SUMMARY', 'TOTAL', 'GENERAL_WASTE',
#                       'CARDBOARD', 'COMINGLED', 'SUBCONTRACTED', 'UOS']


# df = pd.read_csv(path, dtype={"Schd Time Start": str, "PO": str})

# # Transform
# trans_df = dt_wet().transform_and_clean_Route_num(df)
# trans_df = dt_wet().transform_date(df)

# # resample df by 7D
# resampled_df = rev().resample_by_7d(trans_df)

# date_keys = rev().date_keys(resampled_df)

# current_date = date_keys[0].date()

# print(current_date)

# df_by_date = rev().get_df_by(resampled_df, current_date)

# # df_by_date => 
# rev_type = Revenue_by_type(df_by_date)

# names = rev_type.routes_name('GENERAL_WASTE')
# series = rev_type.routes_inc_series('GENERAL_WASTE')
# incs = rev_type.routes_inc('GENERAL_WASTE')
