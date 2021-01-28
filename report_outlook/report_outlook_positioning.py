import xlwings as xw
import typing 
# from collections.abc import Sized, Iterable, Iterator


# Type interface
# List_route_num = list[str]

class Report_outlook_positioning:
    def __init__(self):
        pass
     
    #  Create worksheets for the workbooks 
     # wb as xlwings workbook, list_of_route - List of str
    def create_and_name_ws_by_routes(wb, list_of_rev_types):
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
    def format_ws_font_style_to_arial(wb, ws_name : str):
        ws = wb.sheets[ws_name]
        ws.range("A:DA").api.Font.Name = "Arial"

    # Format Report Headers 
    # date index / date string or date object
    def format_headers(wb, ws_name : str, date = "dd/mm/yyyy"):
        report_title = wb.sheets[ws_name].range('A1')
        report_date = wb.sheets[ws_name].range('A2') 
        report_title.value = f"Weekly Financial Management Report - {ws_name}"
        report_date.value = f"Start at : {date}"
        report_title.api.Font.Size = 13
        report_date.api.Font.Size = 13
        report_title.api.Font.Bold = True
        report_date.api.Font.Bold = True
    
    # Left 2 columns width format 
    def format_left_columns(wb, ws_name : str):
        ws = wb.sheets[ws_name]
        ws.range('A1').column_width = 1.0 
        ws.range('B1').column_width = 3.14
        ws.range('C1').column_width = 3.14


    def format_report_content_total_income(wb, ws_name : str, total_revenue : float = 0.00 ):
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
        wb, 
        ws_name : str,
        route_nums = [],
        route_nums_figure = [],
        anchor_cell : str = "B6"):

        ws = wb.sheets[ws_name]
        # anchor_cell => Revenue label 
        anchor_cell_loc = ws.range(anchor_cell)
        # down 1 and left 1 By B6
        rev_by_route_num_title = anchor_cell_loc.offset(row_offset=1, column_offset=1)
        rev_by_route_num_title.value = "By Route Number"
        rev_by_route_num_title.api.Font.Bold = True
        
        # down 1 and left 1 By Route Number title 
        start_of_route_nums = rev_by_route_num_title.offset(row_offset=1, column_offset=1)
        start_of_route_nums.value = route_nums
        # ======================================================
        # Money figures Offset Left 4 by the starting of 
        # To make 100% sure the figure is matching the route 
        # use for loop or list comp to each out the money figure
        # correspond it to the route number
        # but I will just list it out, as time constriant
        start_of_route_nums_figure = start_of_route_nums.offset(column_offset=4)
        start_of_route_nums_figure.value = route_nums_figure
        # ======================================================

    def routes_rev_display_horizontal(           
        wb, 
        ws_name : str,
        route_nums = [],
        route_nums_figure = [],
        anchor_cell : str = "B4"):

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

#   anchor Cell in B4
    def display_rev_type_in_total_sheet(
        wb,
        rev_type_name : str,
        total_revenue : float = 0.00, 
        anchor_cell : str = "B4"):

        # total sheet
        ws = wb.sheets["total"]
        anchor_cell_loc = ws.range(anchor_cell)
        # left 1 down 3 => start with it
        first_rev_type_title_cell = anchor_cell_loc.offset(row_offset=3,column_offset=1)

        # if has value down 1
        # When rev_type_title cell has value it moves down

        def check_empty_cell(rev_name:str, target_cell:object):
            #  starts from 0
            if target_cell.value is None:
                target_cell.value = rev_name
                return target_cell
            else:
                new_target_cell = target_cell.offset(row_offset=1)
                return check_empty_cell(rev_name, new_target_cell)

        target_rev_title = check_empty_cell(rev_type_name,first_rev_type_title_cell)
        
        # Left 5 => revenue amount 
        rev_figure = target_rev_title.offset(column_offset=5)
        rev_figure.value = total_revenue





    # Format by Route number

    # Format by Truck number 

    # Format by Bin Vol

    
    # Test offset 
    # Test lIST Values in column