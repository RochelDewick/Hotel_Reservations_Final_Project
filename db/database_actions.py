from db.database_connect import DbCon
from sqlalchemy import text
import sqlalchemy
import pandas as pd

class DBActions:
    
    isConnected = False
    Cursor = None
    dbConnect = None

    def __init__(self):
        if DBActions.isConnected == False:
            DBActions.isConnected = self.connect()
            if DBActions.isConnected:
                DBActions.Cursor = self.dbConnect.Cursor
            else:
                raise ConnectionError
            
    def connect(self):  
        try:
            DBActions.dbConnect = DbCon()
        except KeyError:
            raise Exception(f"Missing database connection data in configuration file settings.ini")
        except Exception as e:
            raise Exception(e)

        return DBActions.dbConnect.Connect()
          

    def create_tables_from_df(self, df_allreservations):
        engine = DBActions.dbConnect.getEngine()
        table_guest_exists = sqlalchemy.inspect(engine).has_table("Guest")
        table_reservation_exists = sqlalchemy.inspect(engine).has_table("Reservation")

        if table_guest_exists or table_reservation_exists:
            while True:
                delete_tables = input("Reservation/Guest tables already exist. Delete tables and recreate?").lower()
                if delete_tables == 'yes':
                    print("Deleting tables and recreating.")
                    break
                elif delete_tables == 'no':
                    print("Returning out - not proceeding.")
                    return
                else:
                    print("You have to choose Yes or No")    
        
            DBActions.Cursor.execute(text("""DROP TABLE IF EXISTS Reservation"""))
            DBActions.Cursor.execute(text("""DROP TABLE IF EXISTS Guest"""))
            DBActions.Cursor.commit()
        self.df_reservations = df_allreservations
        self.split_df_reservations()
        self.insert_df(self.df_guests, "Guest")
        self.insert_df(self.df_reservations, "Reservation")
 
    def split_df_reservations(self):
        self.df_reservations.insert(0, 'ReservationId', range(0, 0 + len(self.df_reservations)))
        #first arg len(df_reservations) instead of 0 untested. did this so GuestId is at end instead of beg.
        self.df_reservations.insert(len(self.df_reservations.axes[1]), 'GuestId', range(0, 0 + len(self.df_reservations)))
        self.df_guests = self.df_reservations[['GuestId', 'adults','children', 'babies', 'country']]
        # the above insert on the dataframe works without reassigning
        # however the drop below doesn't change the original and has to be reassigned
        # why I don't know     
        self.df_reservations = self.df_reservations.drop(columns=['adults','children', 'babies', 'country'])

    def insert_df(self, df_to_insert, s_table_name):
        engine = DBActions.dbConnect.getEngine()
        #__init__() got multiple values for argument 'schema'
        df_to_insert.to_sql(s_table_name, engine, if_exists='append', index=False, chunksize=1000) #,
        DBActions.Cursor.commit()
        
    def df_query(self, qry):
        engine = DBActions.dbConnect.getEngine()
        df = pd.read_sql_query(text(qry),engine)
        return df
    
    def query(self, qry):
        return DBActions.Cursor.execute(text(qry)).fetchall()
    
    def rawquery(self, qry):
        return DBActions.Cursor.execute(qry).fetchall()
 

