class Routes_analysis_component:
    def __init__(self):
        return

    def income_session(self,
                wb: object,
                ws_name: str,
                income_title: str = "",
                items: object = {},
                anchor_row: int = 6):

        if anchor_row == 6:
                print(f"Please item title {income_title} Cell in B6 ")
        
        # Anchor cell in B6
        item_title_cell = wb.sheets[ws_name].range((anchor_row, 2))

        
        


    def get_routes_income_cell_location(self):
        
        pass


#     session_title_cell.value = session_header
#     session_title_cell.api.Font.Bold = True
#     session_title_cell.api.Font.Size = 13
#               is_inc: bool = True,
#               is_inc: bool = True,
#                 table_headers: list = [],
#                 items: object = {},
#                 anchor_row: int = 6):


# item_title_name = f"Income - {item_title}"
#         item_title_cell.value = item_title_name
#         # Left ward of 6

#         item_figure_cell = item_title_cell.offset(column_offset=6)
#         # dummy figure
#         item_figure_cell.value = items.figure
#         routes_item_start_cell = item_title_cell.offset(column_offset=8)

#         # dummy routes figure
#         routes_item_start_cell.value = items.route_items

#         # Percentage one down and
#         items_percentage_cell = item_title_cell.offset(row_offset=1)
#         items_percentage_cell.value = f"Income % - {item_title}"

#         routes_item_percentage_start_cell = items_percentage_cell.offset(
#             column_offset=8)
#         routes_item_percentage_start_cell.value = items.route_items_percentage