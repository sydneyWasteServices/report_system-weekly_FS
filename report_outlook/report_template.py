import xlwings as xw
import typing
from report_outlook.report_outlook_positioning import Report_outlook_positioning


class Report_template(Report_outlook_positioning):
    def __init__(self):
        # python 3
        super().__init__()
        

    def paul_weekly_fr1(wb: object, start_date="dd/mm/yyyy"):
        # Add one more sheet
        wb.sheets.add()
        # point to the last sheet
        wb.sheets[-1].name = "weekly_summary"

        # make sure I am working in worksheet weekly_summary
        ws_name = "weekly_summary"

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
        super().format_weekly_fr1_header(wb, start_date)

        # Refractor to class feature code
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




    # ================================================
    # Revenue Report template as Vectical
    def report_templates_vertical1(wb: object, rev_type_name: str, series: object, df_start_date: str):
        total_income = 0
        route_num = []
        route_incomes = []

        print(rev_type_name)
        if rev_type_name == 'total':
            total_income = series.Price.sum()

            route_nums = series.groupby('Route number').Price.sum()

            route_nums_keys = route_nums.keys()

            route_nums_keys = rop.transform_list_to_nested_list(
                route_nums_keys)
            [route_incomes.append(route_income) for route_income in route_nums]
            route_incomes = rop.transform_list_to_nested_list(route_incomes)

        else:
            list_of_route_num = rev.rev_type_hardcode(rev_type_name)
            series_per_rev_type = rev.filter_df_by_rev_routes(
                series, list_of_route_num)
            total_income = series_per_rev_type.Price.sum()

            route_nums = series_per_rev_type.groupby(
                'Route number').Price.sum()

            route_nums_keys = route_nums.keys()

            route_nums_keys = rop.transform_list_to_nested_list(
                route_nums_keys)

            [route_incomes.append(route_income) for route_income in route_nums]
            route_incomes = rop.transform_list_to_nested_list(route_incomes)

            # route number and income

        rop.format_ws_font_style_to_arial(wb, rev_type_name)
        rop.format_headers(wb, rev_type_name, df_start_date)
        rop.format_left_columns(wb, rev_type_name)
        rop.format_report_content_total_income(wb, rev_type_name, total_income)
        rop.routes_rev_display_vertical(
            wb, rev_type_name, route_nums_keys, route_incomes)

    # ======================================================


# Revenue Report template as Horizontal
# ======================================================
    def report_templates_horizontal(wb: object, rev_type_name: str, series: object, df_start_date: str):
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
        #    route_nums_keys = rop.transform_list_to_nested_list(route_nums_keys)
            [route_incomes.append(route_income) for route_income in route_nums]

    # ===============================================
        # build by each page
    # ===============================================
        else:

            list_of_route_num = rev.rev_type_hardcode(rev_type_name)
            series_per_rev_type = rev.filter_df_by_rev_routes(
                series, list_of_route_num)
            total_income = series_per_rev_type.Price.sum()

            route_nums = series_per_rev_type.groupby('Route number').Price.sum()

            # convert index List to list
            route_nums_keys = route_nums.keys()
            route_nums_keys = route_nums_keys.tolist()
            # route_nums_keys = rop.transform_list_to_nested_list(route_nums_keys)

            [route_incomes.append(route_income) for route_income in route_nums]
            #    ============================================================================
            # populate all rev (Need to refactor)
            rop.display_rev_type_in_total_sheet(wb, rev_type_name, total_income)

            #    ============================================================================
    # ===============================================
            # route_incomes = rop.transform_list_to_nested_list(route_incomes)

            # route number and income

        rop.format_ws_font_style_to_arial(wb, rev_type_name)
        rop.format_headers(wb, rev_type_name, df_start_date)
        rop.format_left_columns(wb, rev_type_name)
        rop.format_report_content_total_income(wb, rev_type_name, total_income)
        rop.routes_rev_display_horizontal(
            wb, rev_type_name, route_nums_keys, route_incomes)
