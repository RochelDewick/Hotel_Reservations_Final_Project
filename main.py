
import config.config_setup as cfg
import db.database_actions as dbc
import clean_dataframe

def main():
    cfg.init_setup()
 
    Db = dbc.DBActions()
    # Db.create_tables_from_df(clean_dataframe.hotel_bookings)
    Db.query('Select * from reservation')
    
    
if __name__ == "__main__":
    main()