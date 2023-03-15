import sqlalchemy
import pandas as pd
#from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import close_all_sessions

import os

#This class is to connect to the database
# it should be run in an exception handler 
#   - specifically catch KeyError
class DbCon:
    def __init__(self):
            self.Server = os.environ['DB_SERVER']
            self.Driver = os.environ['DB_DRIVER']
            self.Db = os.environ['DB_DATABASE']
            self.Instance = os.getenv('INSTANCE', '')
            self.UserName = None
            self.Password = None
            self.bConnected = False
    def Connect(self):
        conn_str = f"mssql+pyodbc://@{self.Server}{self.Instance}/{self.Db}?driver={self.Driver}"
        self.Engine = create_engine(conn_str, fast_executemany=True)
     #   s = 'mssql+pyodbc://@' + self.m_Server + '/' + self.m_Db + '?trusted_connection=yes&driver='+self.m_Driver
      #  self.o_engine = sqlalchemy.create_engine(s)        #engine = sqlalchemy.create_engine('mssql+pyodbc://{}/{}?driver={}'.format(self.m_sServer, self.m_sDb, driver))
        self.Cursor = self.Engine.connect()
     #   self.o_Conn = self.o_engine.raw_connection()

        self.m_bConnected = True
        
        return self.m_bConnected
    
    def getEngine(self):
        return self.Engine
        
    def Disconnect(self):
        if self.m_bConnected:
            close_all_sessions()
            self.m_bConnected = False
            

   