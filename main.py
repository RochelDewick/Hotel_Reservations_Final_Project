
import config.config_setup as cfg
from os import environ
import db.database_actions as dbc
import pandas as pd

def main():
    cfg.init_setup()
    print("Initialized")


    df = pd.DataFrame()
 
    Db = dbc.DBActions()
 
    Db.create_tables_from_df(df)
  

    
if __name__ == "__main__":
    main()