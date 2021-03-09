

class Routes_analysis_component:
    def __init__(self):
        self._routes_number_loc = {}

    def income_session(
            self,
            wb: object,
            ws_name: str,
            routes_info: object = {},
            anchor_row: int = 6):

        income_title = routes_info.rev_type
        total_income = routes_info.total_inc

        if anchor_row == 6:
            print(f"Income Session title {income_title} Cell in B6")

        # Anchor cell in B6
        # Income title at second column and down 6 rows
        income_title_cell = wb.sheets[ws_name].range((anchor_row, 2))
        income_title_cell.value = income_title

        # Income figure - left at 6 columns
        total_income_cell = income_title_cell.offset(column_offset=5)
        total_income_cell.value = total_income

        # Routes number & Income figures

        routes_number_start_cell = total_income_cell.offset(
            row_offset=-1, column_offset=3)
        routes_number_figure_start_cell = routes_number_start_cell.offset(
            row_offset=1)
        routes_number = routes_info.booking_price_series.index
        routes_number_figure = routes_info.booking_price_series.values
        routes_number_figure_start_cell.value = routes_number_figure

        route_number_list = list(routes_number)

        routes_number_start_cell.value = route_number_list

        # Create route Location objects
        # route_obj => is to clean recursive function state _get_cells_loc(object state)
        route_obj = {}

        self._routes_number_loc = self._get_cells_loc(
            routes_number_start_cell,
            route_obj)

        # Rate
        routes_portion = [
            figure/total_income for figure in routes_number_figure]
        routes_portion_start_cell = routes_number_figure_start_cell.offset(
            row_offset=1)
        routes_portion_start_cell.value = routes_portion
        
        return self

        # print(f"this is      {self._routes_number_loc}")

    def weight_session(
            self,
            wb: object,
            ws_name: str,
            routes_info: object = {},
            anchor_row: int = 6,
            routes_obj :):

        rotues_position = anchor_row - 5

        title = routes_info.rev_type
        total_weight = routes_info.total_weight

        if anchor_row == 6:
            print(f"Weight session title {title} Cell in B6")

        weight_title_cell = wb.sheets[ws_name].range((anchor_row, 2))
        weight_title_cell.value = "Weight in Tons"

        # total weight figure
        weight_title_cell.offset(column_offset=5).value = total_weight

        tipping_routes_number = routes_info.tipping_weight_series.index

        print(self._routes_number_loc)
# =========================
    # Routes income position  
        # not_exist_routes = [num for num in tipping_routes_number if num not in self._routes_number_loc]
        # exist_routes = [num for num in tipping_routes_number if num in self._routes_number_loc]
        
        # # print(f"{not_exist_routes} in {ws_name} Tipping but not in {ws_name} Route Booking")
        # # print(exist_routes)

        # def fill_weight(route_num):
        #     route_weight = self._routes_number_loc[route_num].offset(row_offset=rotues_position)
        #     route_weight_portion = self._routes_number_loc[route_num].offset(row_offset=rotues_position+1)
             
        #     route_weight.value = routes_info.tipping_weight_series[route_num] 
        #     route_weight_portion.value = routes_info.tipping_weight_series[route_num] / total_weight


        # [fill_weight(num) for num in exist_routes]
        # [print(self._routes_number_loc[number]) for number in tipping_routes_number]
        return self
# =============================

    def _get_cells_loc(
            self,
            target_cell: object,
            routes_id_loc_dict={}):

        if target_cell.value is None:
            return routes_id_loc_dict
        else:

            route_number = target_cell.value
            routes_id_loc_dict[route_number] = target_cell

            new_target_cell = target_cell.offset(column_offset=1)
            return self._get_cells_loc(new_target_cell, routes_id_loc_dict)


# def list_routes_cells_position(myDict : dict, target_cell : object):
#     if target_cell.value is None:
#         return myDict
#     else:
#         myDict[target_cell.value] = target_cell
#         new_target_cell = target_cell.offset(column_offset=1)
#         return list_routes_cells_position(myDict, new_target_cell)

# dicts = list_routes_cells_position(dict1,a1_cell)


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
