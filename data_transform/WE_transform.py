# This class is to transform and clean dataframe before we ever start extracting
import pandas as pd
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
class WE_transform:
    def __init__(
        self,
        df : object
    ):
        self.df = df

# Extracting the weekday from Route number, as it is like BR1-1
    def extract_weekday(df : object):
        
        def split_weekday(route_num : str):
            weekday = route_num.split('-')[1]
            return weekday

        df['weekday'] = df['Route number'].apply(split_weekday)
        return df
        
# Clean the Route number e.g. From BR1-1 to BR1
    def clean_route_num_column(df : object):

        def clean_route_number(route_num : str):
            cleaned_route_num = re.sub(r'-.', '',route_num)
            return cleaned_route_num

        df['Route number'] = df['Route number'].apply(clean_route_number)
        return df

    # dataframe type with   DATE column 
    # transform date into date time index for resample 
    def transform_date_format(df: object):
        df['Date_idx'] = pd.to_datetime(df['Date'],format='%d/%m/%Y')
        df = df.set_index(pd.DatetimeIndex(df['Date_idx']))
        return df
    
    # Sort by date Desc
    def sort_by_date_desc(df):
        return df.sort_values(by=['Date'], inplace=True, ascending=False)
         

    