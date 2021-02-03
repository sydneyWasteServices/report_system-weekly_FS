from revenue.revenue import Revenue
from revenue.rev_types import Rev_types


# pass current resampled df  resampled_df[date_key]
class Revenue_by_type(Revenue):
    def __init__(self,
                 select_date_df: object):
        super.__init__()
        self.select_date_df = select_date_df

    def df(
            self,
            rev_type: str):

        routes = Rev_types[rev_type].value
        routes_row = self.select_date_df['Route number'].isin(routes)
        return self.select_date_df[routes_row]

    def total_inc(
            self,
            rev_type: str):

            routes = Rev_types[rev_type].value
            result = (self.select_date_df
                  .pipe(lambda data: data.groupby('Route number').Price.sum())
                  .pipe(lambda data: data.filter(routes))
                  .pipe(lambda data : data.sum())
            )

    def routes_inc(
            self,
            rev_type: str):

            routes = Rev_types[rev_type].value
            result = (self.select_date_df
                  .pipe(lambda data: data.groupby('Route number').Price.sum())
                  .pipe(lambda data: data.filter(routes))
            )
            

        #  def rev_type_hardcode(self, rev_type: str):
        #         switcher = {
        #             'total': 'total',
        #             'general_waste': ['HOOK1', 'BR1', 'BR2', 'BR3', 'FL2', 'FLG', 'RL1', 'RL2', 'RL4', 'RL7', 'RL9', 'RLD', 'RLE', 'RLH', 'RLI', 'RLJ', 'RLK', 'SWG', 'AUSSKIP'],
        #             'cardboard': ['GRIMA', 'APR', 'FLP', 'HYG', 'RED', 'RL5', 'RL6', 'RL8', 'RLP', 'RLR', 'SWP'],
        #             'comingled': ['CBK', 'RLC', 'RLG', 'DOY'],
        #             'subContractor': ['SUB', 'JJT', 'ALLMED', 'BIN', 'CKG', 'CLN', 'GRACE', 'JJR', 'OWE', 'REM', 'REP', 'REQ', 'RRNW', 'RRR', 'SHR', 'SPD', 'SUE', 'URM', 'VEO', 'VEOACT', 'VTG'],
        #             'uos': ['NEPCB', 'UOSCB', 'UOSCO', 'UOSGW', 'CMDCB', 'CMDGW', 'CUMCB', 'CUMGW', 'NEPGW']
        #         }
        #         rev_routes = switcher.get(rev_type, "invalid entry")
        #         return rev_routes




