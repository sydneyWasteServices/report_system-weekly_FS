# Revenue class => critera get DF and rev figure
# summarised data - income , dataset etc
# WatedpIt is categorise based on the runn

# main => init
import pandas as pd
import typing


from enum import Enum

# Rev types are constant


# class Rev_type(Enum):
#     GENERAL_WASTE = 'general_waste'
#     CARDBOARD = 'card_board'
#     COMINGLED = 'comingled'
#     SUBCONTRACTED = 'subcontracted'
#     UOS = 'UOS'


class Revenue:
    def __init__(self, df: object):
        self.df = df

    # return -> List[str]
    # def rev_type_db(Rev_type : Rev_type):
        # odbc connection for particular revenue type
        # return array of route number
        # pass

    # ***************** The Key should be constant, fix it later *****************
    def rev_type_hardcode(self, rev_type: str):
        switcher = {
            'total': 'total',
            'general_waste': ['HOOK1', 'BR1', 'BR2', 'BR3', 'FL2', 'FLG', 'RL1', 'RL2', 'RL4', 'RL7', 'RL9', 'RLD', 'RLE', 'RLH', 'RLI', 'RLJ', 'RLK', 'SWG', 'AUSSKIP'],
            'cardboard': ['GRIMA', 'APR', 'FLP', 'HYG', 'RED', 'RL5', 'RL6', 'RL8', 'RLP', 'RLR', 'SWP'],
            'comingled': ['CBK', 'RLC', 'RLG', 'DOY'],
            'subContractor': ['SUB', 'JJT', 'ALLMED', 'BIN', 'CKG', 'CLN', 'GRACE', 'JJR', 'OWE', 'REM', 'REP', 'REQ', 'RRNW', 'RRR', 'SHR', 'SPD', 'SUE', 'URM', 'VEO', 'VEOACT', 'VTG'],
            'uos': ['NEPCB', 'UOSCB', 'UOSCO', 'UOSGW', 'CMDCB', 'CMDGW', 'CUMCB', 'CUMGW', 'NEPGW']
        }
        rev_routes = switcher.get(rev_type, "invalid entry")
        return rev_routes

    # Filter the Data frame by revenue routes
    # rev_type => List of Route name => str
    # df => dataframe obj
    # Msut pass transformed dataframe
    def get_dates(self):
        series = self.df.resample('7D', kind='period')
        series_date = series.Price.sum().keys()
        return series_date

    def get_dataset(self, date: str = "dd/mm/yy"):
        series = self.df.resample('7D', kind='period')
        df = series.get_group(date)
        return df

    def get_routes(self, rev_type: str):
        list_of_route_num = self.rev_type_hardcode(rev_type)
        # return list of string
        return list_of_route_num

        # list of route number

    def filter_df_by_rev_routes(self, df: object, list_of_routes):
        df = df[df['Route number'].isin(list_of_routes)]
        return df

    def get_trucks(self):
        pass

        # category income
    def get_income_by_rev_type(
        self, 
        rev_type: str, 
        date: str = "dd/mm/yy"):

        series = self.df.resample('7D', kind='period')
        series_by_date = series.get_group(date)

        if rev_type != "total":

            list_of_routes = self.get_routes(rev_type)

            df_by_rev_type = self.filter_df_by_rev_routes(
                series_by_date, list_of_routes)

            income_by_rev_type = df_by_rev_type.Price.sum()

        else:

            income_by_rev_type = series_by_date.Price.sum()

        return income_by_rev_type

    # returns dict route : key, income_figure : value

    def get_income_per_route_by_rev_type(self, rev_type: str, date: str = "dd/mm/yy"):
        series = self.df.resample('7D', kind='period')
        series_by_date = series.get_group(date)

        if rev_type != "total":
            list_of_routes = self.get_routes(rev_type)
            df_by_rev_type = self.filter_df_by_rev_routes(
                series_by_date, list_of_routes)
            income_per_route_by_rev_type = df_by_rev_type.groupby(
                'Route number').Price.sum()
        else:
            income_per_route_by_rev_type = series_by_date.groupby(
                'Route number').Price.sum()
        return income_per_route_by_rev_type

        # income_by_rev_type = df_by_rev_type.Price.sum()
        # return income_by_rev_type

    def get_income_by_truck(self, rev_type: str, date: str = "dd/mm/yy"):
        pass


# Temporary - try to build query for
class WE_income_items:
    def __init__(
            self,
            total: float,
            gw: float,
            cb: float,
            cm: float,
            sub: float,
            uos: float,
            fx : float = 0):
        self.total = total
        self.gw = gw
        self.cb = cb
        self.cm = cm
        self.sub = sub
        self.uos = uos
        self.fx = fx
    