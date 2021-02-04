import xlwings as xw
import typing
# from collections.abc import Sized, Iterable, Iterator
# Type interface
# List_route_num = list[str]


class Report_outlook_positioning:
    def __init__(self):
        return

    def format_weekly_fr1_header(self, wb: object, ws_name: str, start_date: str = "dd/mm/yyyy"):
        report_title = wb.sheets[ws_name].range('A1')
        report_start_date = wb.sheets[ws_name].range('A2')
        report_title.value = "Weekly Financial Report Summary"
        report_start_date.value = start_date
# Also need to calculate finish date
# ================
        # Adjust the Head title
        report_title.api.Font.Size = 13
        report_start_date.api.Font.Size = 13
        report_title.api.Font.Bold = True
        report_start_date.api.Font.Bold = True

    # Left 2 columns width format

    def format_weekly_fr1_service_income(
            self,
            wb: object,
            ws_name: str,
            position: str = "B4"):

        # Main Service Cat title
        service_inc_title = wb.sheets[ws_name].range(position)
        service_inc_title.value = "Service Income"
        service_inc_title.api.Font.Size = 13
        service_inc_title.api.Font.Bold = True

        # service inc item 1
        # position left 1 down 1
        # service_inc_items         item1 item2
        # service_inc_items figure  [123, 456]
        service_inc_item1 = service_inc_title.offset(
            row_offset=1, column_offset=1)
        service_inc_item1.value = "Service Income"
        service_inc_item1_figure = service_inc_item1.offset(column_offset=6)
        service_inc_item1_figure.value = ""


# ===================================================================================

    def format_weekly_fr1_operating_income(
            self,
            wb: object,
            ws_name: str,
            rev_types: object = {},
            anchor_cell: str = "B4"):
        # Main Operating Income title
        operating_inc = wb.sheets[ws_name].range(
            anchor_cell).offset(row_offset=6)
        operating_inc.value = "Operating Income"
        operating_inc.api.Font.Size = 13
        operating_inc.api.Font.Bold = True
# Sub title
        subtitle = operating_inc.offset(row_offset=1)
        subtitle.value = "Add:"

        operating_inc_header = subtitle.offset(column_offset=6)
        operating_inc_header.value = ['Ton', 'Rate', 'Percentage']
# Income Items Content
        # Should be refractor
        # switch object

        def switch_rev_type(key):
            # Revenue type 

            switcher = {
                'total': 'Revenue - Total',
                'gw': "Revenue - General Waste",
                'cb': "Revenue - Cardboard",
                'cm': "Revenue - Comingled",
                'sub': "Revenue - Subcontractor",
                'uos': "Revenue - UOS",
                'fx': "Revenue - Fixed Revenue"
            }
            rev_routes = switcher.get(key, "invalid entry")
            return rev_routes

        def inspect_fill_empty_cell(
                target_cell: object,
                rev_type_key,
                rev_type_figure):

            if target_cell.value is None:
                if rev_type_key == "total":
                    target_cell.value = switch_rev_type(rev_type_key)
                    target_cell.offset(column_offset=9).value = rev_type_figure
                else:
                    target_cell.value = switch_rev_type(rev_type_key)
                    target_cell.offset(column_offset=8).value = rev_type_figure
                    return target_cell
            else:
                target_cell = target_cell.offset(row_offset=1)
                return inspect_fill_empty_cell(target_cell, rev_type_key, rev_type_figure)

        # left 1 down 1 and check has value
        inc_content_anchor_cell = subtitle.offset(
            row_offset=1, column_offset=1)
        # Start from  operating_inc position
        rev_types_dict = rev_types.__dict__
        keys = rev_types_dict.keys()
        # keys = rev_types_dict.keys()

        rev_types_cells = [inspect_fill_empty_cell(
            inc_content_anchor_cell, key, rev_types_dict[key]) for key in keys]
        # down one by all rev types
        last_of_rev_types_cells = rev_types_cells[-1]

        cardboard_rebate = last_of_rev_types_cells.offset(row_offset=1)
        cardboard_rebate.value = "CardBoard Recycling Rebate"

        cardboard_rebate_rate = cardboard_rebate.offset(column_offset=6)

        total_rev = cardboard_rebate.offset(row_offset=2)
        total_rev.value = "Total Revenue"
        total_rev.api.Font.Bold = True

# ===================================================================================
        # Anchor Cell B4
        # add_rebate_figure = add_rebate.offset(column_offset=5)
        # cws - Contract Waste Services Exp
        # cgt - Contract Grease Trap Exp
    def format_weekly_fr1_operating_expense(
            self,
            wb: object,
            ws_name: str,
            gw_tons: float = 0,
            gw_rate: float = 0,
            cm_tons: float = 0,
            cm_rate: float = 0,
            org_tons: float = 0,
            org_rate: float = 0,
            cws: float = 0,
            cgt: float = 0,
            others: float = 0,
            anchor_cell: str = "B4"):

        operating_exp = wb.sheets[ws_name].range(
            anchor_cell).offset(row_offset=20)
# Main Operating Expense title
        operating_exp.value = "Operating Expense"
        operating_exp.api.Font.Size = 13
        operating_exp.api.Font.Bold = True
# Sub title
        subtitle = operating_exp.offset(row_offset=1)
        subtitle.value = "Less:"

        operating_exp_header = subtitle.offset(column_offset=6)
        operating_exp_header.value = ['Ton', 'Rate', 'Percentage']


# Exp Item Content
        def switch_exp_items(key):

            switcher = {
                'gw': 'Expense - General Waste',
                'cm': "Expense - Comingled",
                'org': "Expense - Organics",
                'cws': "Contracting Waste Service",
                'cgt': "Contracting Grease Trap",
                'others': "Expense - Others"
            }
            exp_item = switcher.get(key, "invalid entry")
            return exp_item

        def inspect_fill_empty_cell(
                target_cell: object,
                exp_items_key,
                exp_item_figure: float = 0):

            if target_cell.value is None:
                target_cell.value = switch_exp_items(exp_items_key)
                target_cell.offset(column_offset=8).value = exp_item_figure
                return target_cell

            else:
                
                target_cell = target_cell.offset(row_offset=1)
                return inspect_fill_empty_cell(target_cell, exp_items_key, exp_item_figure)

        # Operating expense Items content 
        exp_items_list = ['gw','cm','org' ,'cws','cgt','others']
        # left 1 down 1 and check has value
        op_exp_content_anchor_cell = subtitle.offset(
            row_offset=1, column_offset=1)

        exp_items_cell = [inspect_fill_empty_cell(op_exp_content_anchor_cell, exp_item) for exp_item in exp_items_list]
        
        last_of_exp_item = exp_items_cell[-1]
        
        total_exp = last_of_exp_item.offset(row_offset=2)
        total_exp.value = "Total Expense"
        total_exp.api.Font.Bold = True
# =============================================================================


    def format_report_content_total_income(self, wb, ws_name: str, total_revenue: float = 0.00):
        ws = wb.sheets[ws_name]
        income_title = ws.range('B4')
        income_title.value = "Income"
        income_title.api.Font.Bold = True
        total_revenue_title = ws.range('B6')
        # =================================================================
        # Total Rev title
        total_revenue_title.value = "Total Revenue from Waste Edge"
        # ===================================================================
        total_revenue_title.offset(column_offset=7).value = total_revenue

        # Route numbers List
        # How to type route_num as List[str] or iter[str]

    # offset(row_offset=0, column_offset=0)
        # By Route / Tuck Number / By Bin Vol =>
        # It would designed as offset by one Cell location
        # So to be flexiblely replace by Cell location
        # Anchor Cell as B5 as Total Revenue title cell

    def routes_rev_display_vertical(
            self,
            wb,
            ws_name: str,
            route_nums=[],
            route_nums_figure=[],
            anchor_cell: str = "B6"):

        ws = wb.sheets[ws_name]
        # anchor_cell => Revenue label
        anchor_cell_loc = ws.range(anchor_cell)
        # down 1 and left 1 By B6
        rev_by_route_num_title = anchor_cell_loc.offset(
            row_offset=1, column_offset=1)
        rev_by_route_num_title.value = "By Route Number"
        rev_by_route_num_title.api.Font.Bold = True

        # down 1 and left 1 By Route Number title
        start_of_route_nums = rev_by_route_num_title.offset(
            row_offset=1, column_offset=1)
        start_of_route_nums.value = route_nums
        # ======================================================
        # Money figures Offset Left 4 by the starting of
        # To make 100% sure the figure is matching the route
        # use for loop or list comp to each out the money figure
        # correspond it to the route number
        # but I will just list it out, as time constriant
        start_of_route_nums_figure = start_of_route_nums.offset(
            column_offset=4)
        start_of_route_nums_figure.value = route_nums_figure
        # ======================================================

    def routes_rev_display_horizontal(
            self,
            wb,
            ws_name: str,
            route_nums=[],
            route_nums_figure=[],
            anchor_cell: str = "B4"):

        # col 9
        ws = wb.sheets[ws_name]
        # anchor_cell => Income Label
        anchor_cell_loc = ws.range(anchor_cell)
        # Left 9
        rev_by_route_num_title = anchor_cell_loc.offset(column_offset=9)
        rev_by_route_num_title.value = "By Route Number"
        rev_by_route_num_title.api.Font.Bold = True

        # down 1 and left 1 By Route Number title
        start_of_route_nums = rev_by_route_num_title.offset(row_offset=1)
        start_of_route_nums.value = route_nums
        # ======================================================
        # Money figures Offset Left 4 by the starting of
        # To make 100% sure the figure is matching the route
        # use for loop or list comp to each out the money figure
        # correspond it to the route number
        # but I will just list it out, as time constriant
        start_of_route_nums_figure = start_of_route_nums.offset(row_offset=1)
        start_of_route_nums_figure.value = route_nums_figure
        # ======================================================

    # Adapt it to column format
    # type as list of str
    def transform_list_to_nested_list(list_of_values):
        nested_lst = [[i] for i in list_of_values]
        return nested_lst

# ================================================================================
    # Temporary Display
#   anchor Cell in B4
    def display_rev_type_in_total_sheet(
            self,
            wb,
            rev_type_name: str,
            total_revenue: float = 0.00,
            anchor_cell: str = "B4"):

        # total sheet
        ws = wb.sheets["total"]
        anchor_cell_loc = ws.range(anchor_cell)
        # left 1 down 3 => start with it
        first_rev_type_title_cell = anchor_cell_loc.offset(
            row_offset=3, column_offset=1)

        # if has value down 1
        # When rev_type_title cell has value it moves down
        # refractor
        def check_empty_cell(
                rev_name: str,
                target_cell: object):
            #  starts from 0
            if target_cell.value is None:
                target_cell.value = rev_name
                return target_cell
            else:
                new_target_cell = target_cell.offset(row_offset=1)
                return check_empty_cell(rev_name, new_target_cell)

        target_rev_title = check_empty_cell(
            rev_type_name, first_rev_type_title_cell)

        # Left 5 => revenue amount
        rev_figure = target_rev_title.offset(column_offset=5)
        rev_figure.value = total_revenue

    # Format by Route number

    # Format by Truck number

    # Format by Bin Vol

    # Test offset
    # Test lIST Values in column
