from revenue.rev_types import Rev_types
import typing
import pandas as pd
import sys
import os
import numpy as np
sys.path.append(sys.path[0] + "/..")


class Routing_tipping:
    def __init__(self, tipping_df: object = {}):
        self.tipping_df = tipping_df

    def transform(self, df: object):
        df['Route No'] = df['Route No'].astype('str')
        df[['Route No', 'weekday']] = df['Route No'].str.split(
            '-', 1, expand=True)

        df['Route Date'] = pd.to_datetime(df['Route Date'], format='%d-%b-%Y')
        df['Disposal Date'] = pd.to_datetime(
            df['Disposal Date'], format='%d-%b-%Y')

        return df

    def drop_no_docket(self, df: object):
        df = df.dropna(subset=['Docket No'])
        return df

    def total_weight_rebateOrExp(self, rev_type: str, rate : float):
        routes = Rev_types[rev_type].value

        result = (self.tipping_df
                  .pipe(lambda data: data.groupby('Route No').Weight.sum())
                  .pipe(lambda data: data.filter(routes))
                  .pipe(lambda data: data.transform([lambda x : x,lambda x : x * rate]))
                  .pipe(lambda data: data.sum())
                  )
        result.index = ["weight", "expOrRebate" ]
        return result


    def routes_diff(self, rev_type: str):

        routes = Rev_types[rev_type].value

        routes_tipping = (self.tipping_df
                          .pipe(lambda data: data.groupby('Route No').Weight.sum())
                          .pipe(lambda data: data.filter(routes))
                          .pipe(lambda data: data.index)
                          )

        diff = len(routes) - len(routes_tipping)

        if diff == 0:
            return f"{routes} - all routes are included in Tipping"
        else:
            a = np.array(routes)
            b = np.array(routes_tipping)

            diff_elem = np.setdiff1d(a, b)
            return diff_elem
    

    def routes_weight_expOrRebate(self, rev_type: str, rate : float):
        
        routes = Rev_types[rev_type].value
        
        result = (self.tipping_df
                  .pipe(lambda data: data.groupby('Route No').Weight.sum())
                  .pipe(lambda data: data.filter(routes))
                  .pipe(lambda data: data.transform([lambda x : x,lambda x : x * rate]))
                  .pipe(lambda data: data.rename(columns={data.columns[0] : 'weight_expOrRebate'}))
                  )
        # return routes -key : route Number, value : Array of [weight, weight * rate]
        # Return data frame   key : value [weight, Rebate/Exp]
        return result


