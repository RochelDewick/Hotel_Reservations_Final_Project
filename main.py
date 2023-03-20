
import config.config_setup as cfg
import db.database_actions as dbc

def main():
    cfg.init_setup()
 
    Db = dbc.DBActions()
 
    
if __name__ == "__main__":
    main()