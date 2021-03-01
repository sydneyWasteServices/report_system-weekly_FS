# os.path.dirname(__file__) just gives you the directory that your current python file is in,
#  and then we navigate to 'Common/' the directory and import 'Common' the module.

import sys, os
sys.path.append(sys.path[0] + "/..")
from routes_tipping.routes_tipping import Routing_tipping

from revenue.revenue import Revenue as rev
from data_transform.WE_transform import WE_transform as dt_wet
from revenue.revenue_by_type import Revenue_by_type
import pandas as pd


path = '../../../ubuntuShareDrive/Datasets/tipping_data/TipRecords_17.02.2021_23.02.2021.csv'
df = pd.read_csv(path)

a = Routing_tipping()
df = a.drop_no_docket(df)
route_tip_df = a.transform(df)

route_tip = Routing_tipping(route_tip_df).routes_weight('CARDBOARD')

diff = Routing_tipping(route_tip_df).routes_diff('CARDBOARD')

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
