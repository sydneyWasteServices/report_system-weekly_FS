class Routes_info:
    def __init__(
        self,
        total_operating_inc : float,
        total_operating_exp : float = 0,
        total_rebate : float = 0,
        routes_number : list = [],
        routes_inc : list = [],
        routes_exp : list = [],
        routes_rebate : list = [],
        trucks_number : list = [],
        drivers_salary : list =[]):

        self.total_operating_inc = total_operating_inc
        self.total_operating_exp = total_operating_exp
        self.total_rebate = total_rebate
        self.routes_number = routes_number
        self.routes_inc = routes_inc
        self.routes_exp = routes_exp
        self.routes_rebate = routes_rebate
        self.trucks_number = trucks_number
        self.drivers_salary = drivers_salary
    


    # strategy => Extract information from Df tunck it to object Info
    # Report template parse info object Position Figure in report
    # Build Info Object ?
    # Total Operating Income by Type 
    # Total Rebate / Total Operating Expense 

    # List of Routes Number
    # List of Routes Operating Income
    # List of Routes Operating Expense / Income => if Cardboard Inc, other than that expense
    # List of Truck Number
    # List of Drivers Salary