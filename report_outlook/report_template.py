import xlwings as xw
import typing
from report_outlook.report_outlook_positioning import Report_outlook_positioning


class Report_template(Report_outlook_positioning):
    def __init__(self):
        super().__init__()
        return
    # list_of_wsname  = list[str]

    def add_sheets(
            self,
            wb: object,
            list_of_wsname=[]):
        # print(list_of_wsname)
        num_list_of_wsname = len(list_of_wsname)
        num_sheets = len(wb.sheets)

        if num_list_of_wsname > num_sheets:
            add_num_sheets = num_list_of_wsname - num_sheets
            [wb.sheets.add() for n in range(add_num_sheets)]

        for i, wsname in enumerate(list_of_wsname):
            wb.sheets[i].name = wsname

# For each of Worksheet
    def paul_weekly_fr1(
            self,
            wb: object,
            ws_name: str = "weekly_fr",
            start_date: str = "dd/mm/yyyy",
            we_income_items: object = {},
            service_income_items: object = {},
            fix_income: float = 0,
            cb_weight: float = 0,
            gw_weight: float = 0,
            cm_weight: float = 0,
            org_weight: float = 0):

        ws = wb.sheets[ws_name]

        # report formating
        # ========================
        super().format_ws_font_style_to_arial(wb, ws_name)
        super().format_left_columns(wb, ws_name)
        # ========================

        # Financial Report Headers
        # =======================
        # Header title
        # start date
        # finish date
        super().format_weekly_fr1_header(wb, ws_name, start_date)

        # B4 Anchor Shell
        # Assume report contents are start with B4
        # service income session
        super().format_weekly_fr1_service_income(wb, ws_name)

        # Down B4 of 6 cell, will be change to dynamic 
        # When there are more service income item 
        super().format_weekly_fr1_operating_income(wb, ws_name, we_income_items)

        # Must be refractor as picking object key
        # point to the value
        # operating expense 
        super().format_weekly_fr1_operating_expense(wb, ws_name)



         



    # Revenue Report template as Vectical

    def report_templates_vertical1(self, wb: object, rev_type_name: str, series: object, df_start_date: str):
        total_income = 0
        route_num = []
        route_incomes = []

        print(rev_type_name)
        if rev_type_name == 'total':
            total_income = series.Price.sum()

            route_nums = series.groupby('Route number').Price.sum()

            route_nums_keys = route_nums.keys()

            route_nums_keys = super().transform_list_to_nested_list(
                route_nums_keys)
            [route_incomes.append(route_income) for route_income in route_nums]
            route_incomes = super().transform_list_to_nested_list(route_incomes)

        else:
            list_of_route_num = rev.rev_type_hardcode(rev_type_name)
            series_per_rev_type = rev.filter_df_by_rev_routes(
                series, list_of_route_num)
            total_income = series_per_rev_type.Price.sum()

            route_nums = series_per_rev_type.groupby(
                'Route number').Price.sum()

            route_nums_keys = route_nums.keys()

            route_nums_keys = super().transform_list_to_nested_list(
                route_nums_keys)

            [route_incomes.append(route_income) for route_income in route_nums]
            route_incomes = super().transform_list_to_nested_list(route_incomes)

            # route number and income

        super().format_ws_font_style_to_arial(wb, rev_type_name)
        super().format_headers(wb, rev_type_name, df_start_date)
        super().format_left_columns(wb, rev_type_name)
        super().format_report_content_total_income(wb, rev_type_name, total_income)
        super().routes_rev_display_vertical(
            wb, rev_type_name, route_nums_keys, route_incomes)

    # ======================================================


# Revenue Report template as Horizontal
# ======================================================

    def report_templates_horizontal(self, wb: object, rev_type_name: str, series: object, df_start_date: str):
        total_income = 0
        route_num = []
        route_incomes = []

    # ===============================================
        # Building the total_sheet
        if rev_type_name == 'total':
            total_income = series.Price.sum()

            route_nums = series.groupby('Route number').Price.sum()
        # convert index List to list
            route_nums_keys = route_nums.keys()
            route_nums_keys = route_nums_keys.tolist()
        #    route_nums_keys = super().transform_list_to_nested_list(route_nums_keys)
            [route_incomes.append(route_income) for route_income in route_nums]

    # ===============================================
        # build by each page
    # ===============================================
        else:

            list_of_route_num = rev.rev_type_hardcode(rev_type_name)
            series_per_rev_type = rev.filter_df_by_rev_routes(
                series, list_of_route_num)
            total_income = series_per_rev_type.Price.sum()

            route_nums = series_per_rev_type.groupby(
                'Route number').Price.sum()

            # convert index List to list
            route_nums_keys = route_nums.keys()
            route_nums_keys = route_nums_keys.tolist()
            # route_nums_keys = super().transform_list_to_nested_list(route_nums_keys)

            [route_incomes.append(route_income) for route_income in route_nums]
            #    ============================================================================
            # populate all rev (Need to refactor)
            super().display_rev_type_in_total_sheet(wb, rev_type_name, total_income)

            #    ============================================================================
    # ===============================================
            # route_incomes = super().transform_list_to_nested_list(route_incomes)

            # route number and income

        super().format_ws_font_style_to_arial(wb, rev_type_name)
        super().format_headers(wb, rev_type_name, df_start_date)
        super().format_left_columns(wb, rev_type_name)
        super().format_report_content_total_income(wb, rev_type_name, total_income)
        super().routes_rev_display_horizontal(
            wb, rev_type_name, route_nums_keys, route_incomes)
