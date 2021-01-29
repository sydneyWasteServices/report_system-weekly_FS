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
class WE_transform:
    def __init__(
        self,
        df : object
    ):
        self.df = df

# Extracting the weekday from Route number, as it is like BR1-1
    def extract_weekday(df : object):
        
        def split_weekday(route_num : str):
            weekday = route_num.split('-')
    # ==============================================================================
            # Since some route number is empty need to use if to catch it 
            # need further investigation to prevent empty Cell 
            if len(weekday) < 2:
                return 0
            else:
                return weekday[1]
            
        df['weekday'] = df['Route number'].apply(split_weekday)
        return df

    
    
        
# Clean the Route number e.g. From BR1-1 to BR1
    def clean_route_num_column(df : object):

        def clean_route_number(route_num : str):
        # ==============================================================================
        # Declare cleaned_route_num as nothing until it has str to split and clean 
        # catch the empty route number row 
            cleaned_route_num = 0
            if route_num is np.nan:
                    return cleaned_route_num
            else:
                cleaned_route_num = re.sub(r'-.', '',route_num)

            return cleaned_route_num

        df['Route number'] = df['Route number'].apply(clean_route_number)
        return df

    # dataframe type with   DATE column 
    # transform date into date time index for resample 
    def transform_date_format(df: object):
        df['Date_idx'] = pd.to_datetime(df['Date'],format='%d/%m/%y')
        df = df.set_index(pd.DatetimeIndex(df['Date_idx']))
        return df
    
    # Sort by date Desc
    def sort_by_date_desc(df):
        return df.sort_values(by=['Date'], inplace=True, ascending=False)
         

    def drop_invalid_cols(df):
        # Sch Time End and PO are not that useful and many empty cell
        return df.drop(columns=['Schd Time Start','PO'])
        