import sqlalchemy
import pandas as pd
#from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text
import os

#This class is to connect to the database
# it should be run in an exception handler 
#   - specifically catch 
class DbCon:
    def __init__(self):
            self.m_Server = os.environ['SERVER']
            self.m_Driver = os.environ['DRIVER']
            self.m_Db = os.environ['DATABASE']
            self.m_Instance = os.getenv('INSTANCE', '')
            self.m_UserName = None
            self.m_Password = None
            self.m_bConnected = False
    def Connect(self):
        conn_str = f"mssql+pyodbc://@{self.m_Server}{self.m_Instance}/{self.m_Db}?driver={self.m_Driver}"
        self.o_engine = create_engine(conn_str, fast_executemany=True)
     #   s = 'mssql+pyodbc://@' + self.m_Server + '/' + self.m_Db + '?trusted_connection=yes&driver='+self.m_Driver
      #  self.o_engine = sqlalchemy.create_engine(s)        #engine = sqlalchemy.create_engine('mssql+pyodbc://{}/{}?driver={}'.format(self.m_sServer, self.m_sDb, driver))
        self.o_Conn = self.o_engine.connect()
     #   self.o_Conn = self.o_engine.raw_connection()

        self.m_bConnected = True
        
        self.o_Conn.execute(text("CREATE TABLE test"))

    def Disconnect(self):
        if self.m_bConnected:
            self.m_oConn.cursor().close()
            self.m_oSession.close_all()
            self.m_engine.dispose()
            self.m_oConn.close()
            self.m_bConnected = False
    def ReadSqlQuery(self, sQuery):
        if (self.m_bConnected == False):
            print('Error: db found disconnected and will try to connect again while tryng to run a query')
            self.Connect()
            if (self.m_bConnected == False):
                print('Error: db disconnected while tryng to run a query')
        df = pd.read_sql_query(sQuery,self.m_engine)
        return df
    def insert_df(self, df_to_insert, s_table_name):
        #__init__() got multiple values for argument 'schema'
        df_to_insert.to_sql(s_table_name, con=self.m_engine, if_exists='append', index=False, chunksize=1000) #,
        self.m_oConn.cursor().commit()
   