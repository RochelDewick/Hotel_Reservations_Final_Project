from db.database_connect import DbCon
#from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import text
import sqlalchemy
import pandas as pd

class DBActions:
    
    isConnected = False
    Cursor = None
    dbConnect = None

    def __init__(self):
        if self.isConnected == False:
            self.isConnected = self.connect()
            if self.isConnected:
                self.Cursor = self.dbConnect.Cursor
            else:
                raise ConnectionError
            
    def connect(self):  
        try:
            self.dbConnect = DbCon()
        except KeyError:
            print(f"Missing database connection data in configuration file settings.ini")
            exit()

        return self.dbConnect.Connect()
          

    def create_tables_from_df(self, df_reservations):
        engine = self.dbConnect.getEngine()
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
        
            self.Cursor.execute(text("""DROP TABLE IF EXISTS Reservation"""))
            self.Cursor.execute(text("""DROP TABLE IF EXISTS Guest"""))
            self.Cursor.commit()
            
    #   df_guests = self.split_df_reservations(df_reservations)
        #db.insert_df(df_guests, "Guest")
        #db.insert_df(df_reservations, "Reservation")

    def split_df_reservations(df_reservations):
        df_reservations.insert(0, 'ReservationId', range(0, 0 + len(df_reservations)))
        #first arg len(df_reservations) instead of 0 untested. did this so GuestId is at end instead of beg.
        df_reservations.insert(len(df_reservations.axes[1]), 'GuestId', range(0, 0 + len(df_reservations)))
        df_guests = df_reservations[['GuestId', 'adults','children', 'babies', 'country']]
        df_reservations = df_reservations.drop(columns=['adults','children', 'babies', 'country'])
        return df_guests

    def ReadSqlQuery(self, sQuery):
        if (self.m_bConnected == False):
            print('Error: db found disconnected and will try to connect again while tryng to run a query')
            self.Connect()
            if (self.m_bConnected == False):
                print('Error: db disconnected - reconnection failed')
        df = pd.read_sql_query(sQuery,self.m_engine)
        return df

    def insert_df(conn, df_to_insert, s_table_name):
        #__init__() got multiple values for argument 'schema'
        df_to_insert.to_sql(s_table_name, conn, if_exists='append', index=False, chunksize=1000) #,
        conn.commit()
        
    def ReadSqlQuery(self, sQuery):
        if (self.m_bConnected == False):
            print('Error: db found disconnected and will try to connect again while tryng to run a query')
            self.Connect()
            if (self.m_bConnected == False):
                print('Error: db disconnected while tryng to run a query')
        df = pd.read_sql_query(sQuery,self.m_engine)
        return df

    # the above is for dataframe
    # general query below
    # move both to another file?
    #from sqlalchemy.sql import text
    #s = text("select students.name, students.lastname from students where students.name between :x and :y")
    #conn.execute(s, x = 'A', y = 'L').fetchall()

    def insert_df(self, df_to_insert, s_table_name):
        #__init__() got multiple values for argument 'schema'
        df_to_insert.to_sql(s_table_name, con=self.m_engine, if_exists='append', index=False, chunksize=1000) #,
        self.m_oConn.cursor().commit()