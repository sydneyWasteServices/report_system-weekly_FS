# Revenue class => critera get DF and rev figure
# WatedpIt is categorise based on the runn

# main => init
import pandas as pd
import typing
# from typing import *

from enum import Enum

# Rev types are constant  
class Rev_type(Enum):
    GENERAL_WASTE = 'general_waste'
    CARDBOARD = 'card_board'
    COMINGLED = 'comingled'
    SUBCONTRACTED = 'subcontracted'
    UOS = 'UOS'


class Revenue:
    def __init__(
        self,
        route: str,
        truck_num: str,
        Rev_type: Rev_type,
        source_csv_path: str,
        source_db_path: str
    ):
        self.route = route
        self.truck_num = truck_num
        self.waste_type = waste_type
        self.Rev_type = Rev_type
        self.source_csv_path = source_csv_path 
        self.source_db_path = source_db_path

    # return -> List[str]
    # def rev_type_db(Rev_type : Rev_type):
        # odbc connection for particular revenue type
        # return array of route number  
        # pass

    #***************** The Key should be constant, fix it later *****************
    def rev_type_hardcode(rev_type : str):
        switcher = {
            'total' : 'total',
            'general_waste' : ['BR1','BR2','BR3','DOY','FL2','FLG','RL1','RL2','RL4','RL7','RL9','RLD','RLE','RLH','RLI','RLJ','RLK','SWG'],
            'cardboard' : ['FLP','HYG','RED','RL5','RL6','RL8','RLP','RLR','SWP'],
            'comingled' : ['CBK','RLC','RLG'],
            'subContractor' : ['ALLMED','BIN','CKG','CLN','GRACE','JJR','OWE','REM','REP','REQ','RRNW','RRR','SHR','SPD','SUE','URM','VEO','VEOACT','VTG'],
            'uos' : ['UOSCB','UOSCO','UOSGW','CMDCB','CMDGW','CUMCB','CUMGW','NEPGW']
        }
        rev_routes = switcher.get(rev_type, "invalid entry")
        return rev_routes
         
    # Filter the Data frame by revenue routes 
    # rev_type => List of Route name => str
    # df => dataframe obj 
    def filter_df_by_rev_routes(df : object, rev_type):
        df = df[df['Route number'].isin(rev_type)]
        return df 




# UOS =>  UOSCB	UOSCO	UOSGW	CMDCB	CMDGW	CUMCB	CUMGW	NEPGW
# Subcontractors => ALLMED	BIN	CKG	CLN	GRACE	JJR	OWE	REM	REP	REQ	RRNW	RRR	SHR	SPD	SUE	URM	VEO	VEOACT	VTG


