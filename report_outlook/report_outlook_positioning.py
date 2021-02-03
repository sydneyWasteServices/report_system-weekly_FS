import xlwings as xw
import typing
# from collections.abc import Sized, Iterable, Iterator
# Type interface
# List_route_num = list[str]


class Report_outlook_positioning:
    def __init__(self):
        return

    #  Create worksheets for the workbooks
     # wb as xlwings workbook, list_of_route - List of str
    def create_and_name_ws_by_routes(self, wb, list_of_rev_types):
        num_rev_types = len(list_of_rev_types)
        num_sheets = len(wb.sheets)

        if num_rev_types > num_sheets:
            add_num_sheets = num_rev_types - num_sheets
            for n in range(add_num_sheets):
                wb.sheets.add()

        for (i, rev_type) in enumerate(list_of_rev_types):
            wb.sheets[i].name = rev_type

    # Format sheets font style
    # How type object, wb as xlwings workbook

    def format_ws_font_style_to_arial(self, wb, ws_name: str):
        ws = wb.sheets[ws_name]
        ws.range("A:DA").api.Font.Name = "Arial"

    # Format Report Headers
    # date index / date string or date object
    def format_headers(self, wb, ws_name: str, date="dd/mm/yyyy"):
        report_title = wb.sheets[ws_name].range('A1')
        report_date = wb.sheets[ws_name].range('A2')

        report_title.value = f"Weekly Financial Management Report - {ws_name}"
        report_date.value = f"Start at : {date}"

        report_title.api.Font.Size = 13
        report_date.api.Font.Size = 13
        report_title.api.Font.Bold = True
        report_date.api.Font.Bold = True

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
        operating_inc_header.value = [
            'Ton', 'Rate per Ton', '% of Percentage']
# Income Items Content
        # Should be refractor
        # switch object

        def switch_rev_type(key):

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
        cardboard_rebate_rate.value = 100

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
        operating_exp_header.value = [
            'Ton', 'Rate per Ton', '% of Percentage']

# Exp Item Content

        def switch_exp_items(key):
            switcher = {
                'gw': ['Expense - General Waste', 275],
                'cm': ["Expense - Comingled", 190],
                'org': ["Expense - Organics", 240],
                'cws': ["Contracting Waste Service", 0.03],
                'cgt': ["Contracting Grease Trap", 0.0132],
                'others': ["Expense - Others", 0.003]
            }
            exp_item = switcher.get(key, "invalid entry")
            return exp_item

        def inspect_fill_empty_cell(
                target_cell: object,
                exp_items_key,
                exp_item_figure: float = 0):

            if target_cell.value is None:

                if exp_items_key == 'gw' or exp_items_key == 'cm' or exp_items_key == 'org':

                    exp_item_attrs = switch_exp_items(exp_items_key)
                    target_cell.value = exp_item_attrs[0]
                    target_cell.offset(
                        column_offset=6).value = exp_item_attrs[1]
                    return target_cell

                else:

                    exp_item_attrs = switch_exp_items(exp_items_key)
                    target_cell.value = exp_item_attrs[0]
                    target_cell.offset(
                        column_offset=7).value = exp_item_attrs[1]
                    target_cell.offset(column_offset=8).value = exp_item_figure
                    return target_cell

            else:
                target_cell = target_cell.offset(row_offset=1)
                return inspect_fill_empty_cell(target_cell, exp_items_key, exp_item_figure)

        # Operating expense Items content
        exp_items_list = ['gw', 'cm', 'org', 'cws', 'cgt', 'others']
        # left 1 down 1 and check has value
        op_exp_content_anchor_cell = subtitle.offset(
            row_offset=1, column_offset=1)

        exp_items_cell = [inspect_fill_empty_cell(
            op_exp_content_anchor_cell, exp_item) for exp_item in exp_items_list]

# Total Operating expense
        last_of_exp_item = exp_items_cell[-1]

        total_exp = last_of_exp_item.offset(row_offset=2)
        total_exp.value = "Total Expense"
        total_exp.api.Font.Bold = True
# ========================================================================

    def employment_exp(
            self,
            wb: object,
            ws_name: str,
            salary_exp: float = 0,
            anchor_cell: str = "B4"):

        employment_exp = wb.sheets[ws_name].range(
            anchor_cell).offset(row_offset=32)

# Main employment Expense title
        employment_exp.value = "Employment Expense"
        employment_exp.api.Font.Size = 13
        employment_exp.api.Font.Bold = True
# Sub title
        subtitle = employment_exp.offset(row_offset=1)
        subtitle.value = "Less:"
# Exp Item Content
        salary_exp = subtitle.offset(
            row_offset=1, column_offset=1)
        salary_exp.value = "Salary Expense"

        salary_exp_pc = salary_exp.offset(column_offset=7)
        salary_exp_pc.value = 0.303
# ===============================================================

    def mv_exp(
            self,
            wb: object,
            ws_name: str,
            mv_exp_items: object = {},
            anchor_cell: str = "B4"):

        mv_expense = wb.sheets[ws_name].range(
            anchor_cell).offset(row_offset=37)

# Main MV Expense title
        mv_expense.value = "Motor Vehicle Expense"
        mv_expense.api.Font.Size = 13
        mv_expense.api.Font.Bold = True
# Sub title
        subtitle = mv_expense.offset(row_offset=1)
        subtitle.value = "Less:"
# MV Expense Item Content

        def switch_mv_exp_items(key):
            switcher = {
                'mv-f': ['MV - Fuel', 0.03],
                'mv-r': ["MV - Rego", 0.0046],
                'mv-t': ["MV - Tolls", 0.0086],
                'mv-i': ["MV - Insurance", 0.0122],
                'rm-cc': ["Repair & Maintenance - Cab & Chassic", 0.0178],
                'rm-cb': ["Repair & Maintenance - Compactor / Body", 0.013],
                'rm-mc': ["Repair & Maintenance - Misc. Cosumables", 0.0006],
                'rm-t': ["Repair & Maintenance - Tyres", 0.0039],
                'wcl': ["Workshop Contractor Labour", 0.012],
                'others': ["MV exp - Others", 0.0024],
            }
            exp_item = switcher.get(key, "invalid entry")
            return exp_item

        def inspect_fill_empty_cell(
                target_cell: object,
                exp_items_key,
                exp_item_figure: float = 0):

            if target_cell.value is None:

                exp_item_attrs = switch_mv_exp_items(exp_items_key)
                target_cell.value = exp_item_attrs[0]
                target_cell.offset(
                    column_offset=7).value = exp_item_attrs[1]

                target_cell.offset(column_offset=8).value = exp_item_figure
                return target_cell

            else:
                target_cell = target_cell.offset(row_offset=1)
                return inspect_fill_empty_cell(target_cell, exp_items_key, exp_item_figure)

        mv_exp_items_anchor_cell = subtitle.offset(
            row_offset=1, column_offset=1)
# MV expense Items

        mv_exp_items_list = ['mv-f', 'mv-r', 'mv-t', 'mv-i',
                             'rm-cc', 'rm-cb', 'rm-mc', 'rm-t', 'wcl', 'others']

        mv_exp_items_cell = [inspect_fill_empty_cell(
            mv_exp_items_anchor_cell, exp_item) for exp_item in mv_exp_items_list]

        # Total Operating expense
        last_of_mv_exp_item = mv_exp_items_cell[-1]

        total_exp = last_of_mv_exp_item.offset(row_offset=2)
        total_exp.value = "Total Motor Vehicle Expense"
        total_exp.api.Font.Bold = True
# ==============================================================
# General Expense Session

    def general_exp(
            self,
            wb: object,
            ws_name: str,
            gen_exp_items: object = {},
            anchor_cell: str = "B4"):

        # General Expense Header
        general_expense = wb.sheets[ws_name].range(
            anchor_cell).offset(row_offset=53)

        general_expense.value = "General Expense"
        general_expense.api.Font.Size = 13
        general_expense.api.Font.Bold = True
# Subtitle
        subtitle = general_expense.offset(row_offset=1)
        subtitle.value = "Less:"

        def switch_gen_exp_items(key):
            switcher = {
                'gen': ["General & Administration", 0.0218],
                'bp': ["Business Promotion", 0.011],
                'oc': ["Occupancy Cost", 0.0243]
            }
            exp_item = switcher.get(key, "invalid entry")
            return exp_item

        def inspect_fill_empty_cell(
                target_cell: object,
                exp_items_key,
                exp_item_figure: float = 0):

            if target_cell.value is None:

                exp_item_attrs = switch_gen_exp_items(exp_items_key)
                target_cell.value = exp_item_attrs[0]
                target_cell.offset(
                    column_offset=7).value = exp_item_attrs[1]

                target_cell.offset(column_offset=8).value = exp_item_figure
                return target_cell

            else:
                target_cell = target_cell.offset(row_offset=1)
                return inspect_fill_empty_cell(target_cell, exp_items_key, exp_item_figure)

# General Expense Items
        gen_exp_items_anchor_cell = subtitle.offset(
            row_offset=1, column_offset=1)

        gen_exp_items_list = ['gen', 'bp', 'oc']

        gen_exp_items_cell = [inspect_fill_empty_cell(
            gen_exp_items_anchor_cell, exp_item) for exp_item in gen_exp_items_list]

# Total Operating expense
        last_of_gen_exp_item = gen_exp_items_cell[-1]

        total_exp = last_of_gen_exp_item.offset(row_offset=2)
        total_exp.value = "Total General Expense"
        total_exp.api.Font.Bold = True


# ==============================================================
# Purchase Session

    def purchase(
            self,
            wb: object,
            ws_name: str,
            purchase_items: object = {},
            anchor_cell: str = "B4"):
# Purchase Header
        purchase_expense = wb.sheets[ws_name].range(
            anchor_cell).offset(row_offset=61)

        purchase_expense.value = "General Expense"
        purchase_expense.api.Font.Size = 13
        purchase_expense.api.Font.Bold = True
# SubTitle
        subtitle = purchase_expense.offset(row_offset=1)
        subtitle.value = "Less:"
# Purchase item
        bin_exp = subtitle.offset(
            row_offset=1, column_offset=1)
        bin_exp.value = "Bins"

        bin_exp_pc = bin_exp.offset(column_offset=7)
        bin_exp_pc.value = 0.0132

# =============================================================================

    def format_left_columns(self, wb, ws_name: str):
        ws = wb.sheets[ws_name]
        ws.range('A1').column_width = 1.0
        ws.range('B1').column_width = 3.14
        ws.range('C1').column_width = 3.14

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
