# This class is to transform and clean dataframe before we ever start extracting
import pandas as pd
import numpy as np
import re
import typing
from enum import Enum


class Rev_type(Enum):
    GENERAL_WASTE = 'general_waste'
    CARDBOARD = 'card_board'
    COMINGLED = 'comingled'
    SUBCONTRACTED = 'subcontracted'
    UOS = 'UOS'


# WE stands for WasteEdge 
# df : dataFrame
class WE_transform():
    def __init__(
        self,
        df : object = {}
    ):
        self.df = df

    def transform_and_clean_Route_num(self, df : object):
        df['Route number'] = df['Route number'].astype('str')
        df[['Route number', 'weekday']] = df['Route number'].str.split('-',1,expand=True)
        return df


    # dataframe type with   DATE column 
    # transform date into date time index for resample 
    def transform_date(self, df: object):
        df['Date_idx'] = pd.to_datetime(df['Date'],format='%d/%m/%y')
        df['Date'] = pd.DatetimeIndex(df['Date'])
        df.set_index(df['Date'], inplace=True)
        return df
    
    # Sort by date Desc
    def sort_by_date_desc(self, df):
        return df.sort_values(by=['Date'], inplace=True, ascending=False)
         

    
