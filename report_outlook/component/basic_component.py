import xlwings as xw


class Basic_component:
    def __init__(self):
        pass

    def open_wb(self):
        return xw.Book()

    def add_sheets(
            self,
            wb: object,
            ws_names: list):

        num_req_ws = len(ws_names)
        num_exist_sheets = len(wb.sheets)

        if num_req_ws > num_exist_sheets:
            add_num_sheets = num_req_ws - num_exist_sheets
            [wb.sheets.add() for n in range(add_num_sheets)]

        for i, wsname in enumerate(ws_names):
            wb.sheets[i].name = wsname

    def fonts_arialify(
            self,
            wb: object,
            ws_name: str):

        ws = wb.sheets[ws_name]
        ws.range("A:DA").api.Font.Name = "Arial"

    def header_title(
            self,
            wb: object,
            ws_name: str,
            title: str = "Weekly Financial Report Summary",
            cell_loc: str = "A1"):

        title_cell = wb.sheets[ws_name].range(cell_loc)
        title_cell.value = f"{title} - {ws_name}"
        title_cell.api.Font.Size = 13
        title_cell.api.Font.Bold = True

    def date_title(
            self,
            wb: object,
            ws_name: str,
            date: str,
            date_descr: str = "Start at :",
            cell_loc: str = "A2"):

        date_cell = wb.sheets[ws_name].range(cell_loc)
        datdate_cell.value = f"{date_descr} : {date}"

        date_cell.api.Font.Size = 13
        date_cell.api.Font.Bold = True

    def beautify_left_columns(self, wb, ws_name: str):
        ws = wb.sheets[ws_name]
        ws.range('A1').column_width = 1.0
        ws.range('B1').column_width = 3.14
        ws.range('C1').column_width = 3.14

    # Anchor cell => The first Bold title (Start Income Session)
    # Anchor cell =>B5

    # session_title_cell => pointing to wb.sheets[ws_name].range(cell_loc)
    # cell_loc should be type string or Object( wb.sheets[ws_name].offset() )
    # cell_loc => string | .offset()
    def session_title(
            self,
            wb: object,
            ws_name: str,
            session_title: str,
            cell_loc: str):

        session_title_cell = wb.sheets[ws_name].range(cell_loc)
        session_title_cell.value = session_title

        session_title_cell.api.Font.Size = 13
        session_title_cell.api.Font.Bold = True

# cell_loc => string | .offset()
    def subtitle(
            self,
            wb: object,
            ws_name: str,
            subtitle: str,
            cell_loc: str):

        subtitle_cell = wb.sheets[ws_name].range(cell_loc)
        subtitle_cell.value = f"{subtitle} :"

        subtitle_cell.api.Font.Size = 11
        subtitle_cell.api.Font.Bold = True

    # table_headers => list of string
    # y , x
    # row, column
    def table_headers(
            self,
            wb: object,
            ws_name: str,
            table_headers: list,
            cell_loc: str):

        start_cell = wb.sheets[ws_name].range(cell_loc)
        start_cell.value = table_headers
        self.table_headers_format(cell_loc)

    def table_headers_format(
            self,
            wb: object,
            ws_name: str,
            start_cell_loc: str):

        ws = wb.sheets[ws_name]
        start_cell = ws.range(start_cell_loc)

        start_cell_row = start_cell.row
        start_cell_col = start_cell.column

        end_cell_col = start_cell.end("right").column

        # +1 to print that much times of the column(x)
        for i in range(start_cell_col, end_cell_col+1):
            ws.range((start_cell_row, i)).api.Font.Bold = True

    def fill_items(
            self,
            wb: object,
            ws_name: str,
            items: object = {},
            cell_loc: str =""):
        pass
