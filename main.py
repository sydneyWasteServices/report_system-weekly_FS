# data Transform - waste Edge
from data.operating_inc import Operating_inc as op_inc
from data.operating_exp import Operating_exp as op_exp
from data.operating_salary import Operating_salary as salary
from data.mv_exp import Mv_exp as mv_exp
from data.admin_exp import Admin_exp as admin_exp
from data.bins_exp import Bins_exp as bins_exp

from data_transform.WE_transform import WE_transform as dt_wet
from revenue.revenue import Revenue as rev
from revenue.revenue_by_type import Revenue_by_type

from report_outlook.report_template import Report_template as rt
from report_outlook.component.basic_component import Basic_component as bc

import xlwings as xw
import pandas as pd
import time


# Fixed as Weds to Tues
# Start with df, suppose it is querying from Wed
# dataframe in new downloaded folder
# dataVault\waste_edge_booking_data\23.12.2020_to_26.1.2021

path = "../../dataVault/booking/10.2.2021_16.2.2021.csv"

list_rev_types = ['TOTAL', 'GENERAL_WASTE',
                  'CARDBOARD', 'COMINGLED', 'SUBCONTRACTED', 'UOS']

list_report_sheets = ['WEEKLY_SUMMARY', 'TOTAL', 'GENERAL_WASTE',
                      'CARDBOARD', 'COMINGLED', 'SUBCONTRACTED', 'UOS']

df = pd.read_csv(path, dtype={"Schd Time Start": str, "PO": str})

# Transform
trans_df = dt_wet().transform_and_clean_Route_num(df)
trans_df = dt_wet().transform_date(df)

# resample df by 7D
resampled_df = rev().resample_by_7d(trans_df)

date_keys = rev().date_keys(resampled_df)

current_date = date_keys[0]

df_by_date = rev().get_df_by(resampled_df, current_date)

rev_type = Revenue_by_type(df_by_date)

# TOTAL
# GENERAL_WASTE
# CARDBOARD
# COMINGLED
# SUBCONTRACTED
# UOS

total_inc = rev_type.total_inc('TOTAL')
gw_inc = rev_type.total_inc('GENERAL_WASTE')
cb_inc = rev_type.total_inc('CARDBOARD')
cm_inc = rev_type.total_inc('COMINGLED')
sub_inc = rev_type.total_inc('SUBCONTRACTED')
uos_inc = rev_type.total_inc('UOS')

current_op_inc = op_inc(total_inc, gw_inc, cb_inc, cm_inc, sub_inc, uos_inc)
current_op_exp = op_exp(275,190,240,0.03,0.132,0.003)
current_op_salary = salary(0.303)
current_mv_exp = mv_exp(0.03,0.0046, 0.0086,0.0122,0.0178,0.013,0.0006,0.0039,0.012,0.0024)
current_admin_exp = admin_exp(0.0218,0.011,0.0243)


report_bc_tools = bc()

wb = report_bc_tools.open_wb()

report_bc_tools.add_sheets(wb, list_report_sheets)

weekly_report = rt()

(weekly_report
    .weekly_op_summary(
        wb,
        "WEEKLY_SUMMARY",
        current_date,
        current_op_inc,
        current_op_exp,
        current_op_salary,
        current_mv_exp,
        current_admin_exp
        )
)

for rev_type_name in list_rev_types:

    # Also use if to catch Total => list out all route income
    route_inc = rev_type.routes_inc(rev_type_name)
    (weekly_report
        .by_rev_type(
            wb,
            rev_type_name,
            current_date,
            route_inc))
  


# rev_routes_inc = [rev_type.routes_inc(rev_type_name) for rev_type_name in list_rev_types]

# (weekly_report
#     .by_rev_type())


wb.save(f'D:\\Run Analysis\\WEEKLY_SUMMARY_from_January_2021\\January_2021\\Weekly_Summary\\{str(current_date)}.xlsx')
wb.close()
