import xlwings as xw
import typing
from report_outlook.component.complex_component import Complex_component


class Report_template(Complex_component):
    def __init__(self):
        super().__init__()
        return

    def weekly_op_summary(
            self,
            wb: object,
            ws_name: list,
            date: str,
            op_inc: object = {},
            op_exp: object = {},
            op_salary: object = {},
            mv_exp: object = {},
            admin_exp: object = {},
            bins_exp: object = {}):

        super().report_headers(
            wb,
            ws_name,
            date,
            "Weekly Financial Report Summary")

    # Anchor Cell at B6
    # Operating Income
    # Table Headers

        op_tb_header = ["Ton", "Rate per Ton", "% of Total Operating Inc"]
        no_tb_header = []

        super().report_formating(
            wb,
            ws_name)

        # Anchor at B10
        # Operating Income
        if op_inc:
            super().session(
                wb,
                ws_name,
                "Operating Income",
                True,
                op_tb_header,
                op_inc,
                10)
        else:
            print("Operating income items is empty")
            return 0

    # Anchor at B24
    # Operating Expense
        if op_exp:
            super().session(
                wb,
                ws_name,
                "Operating Expense",
                True,
                op_tb_header,
                op_exp,
                24)
        else:
            print("Operating Expense items is empty")
            return 0

        if op_salary:
            super().session(
                wb,
                ws_name,
                "Operating Salary",
                True,
                no_tb_header,
                op_salary,
                36)
        else:
            print("Operating Salary items is empty")
            return 0

        if mv_exp:
            super().session(
                wb,
                ws_name,
                "Motor Vehicle Expense",
                True,
                no_tb_header,
                mv_exp,
                43)
        else:
            print("Motor Vehicle expense items is empty")
            return 0

        if admin_exp:
            super().session(
                wb,
                ws_name,
                "General & Administration",
                True,
                no_tb_header,
                admin_exp,
                59)
        else:
            print("Admin expense items is empty")
            return 0

        if bins_exp:
            super().session(
                wb,
                ws_name,
                "Bins Purchase",
                True,
                no_tb_header,
                bins_exp,
                24)
        else:
            print("Admin expense items is empty")
            return 0

        pass

    def by_rev_type(self,
                    wb: object,
                    ws_name: list,
                    date: str,
                    route_op_inc: object = {}):

        print(route_op_inc.keys())
        # print(route_op_inc.values())

        super().report_formating(
            wb,
            ws_name)

        super().report_headers(
            wb,
            ws_name,
            date,
            "Weekly Financial Report Summary")
