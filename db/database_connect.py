import pandas as pd
#from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import close_all_sessions
from sqlalchemy.engine import URL
import operator
import os

#This class is to connect to the database
# it should be run in an exception handler 
#   - specifically catch KeyError
class DbCon:
    def __init__(self):
        self.Server = os.environ['DB_SERVER']
        self.Driver = os.environ['DB_DRIVER']
        self.Db = os.environ['DB_DATABASE']
        
        # if has instance name must have port number
        self.Instance = os.getenv('DB_INSTANCE', '')
        self.Port = os.getenv('DB_PORT','')
        
        self.UserName = None
        self.Password = None
        
        self.bConnected = False

            
    Server = property(operator.attrgetter('_Server'))
    @Server.setter
    def Server(self, d):
        if not d: raise Exception("Server cannot be empty - check settings.ini file.")
        self._Server = d
        
    Driver = property(operator.attrgetter('_Driver'))
    @Driver.setter
    def Server(self, d):
        if not d: raise Exception("Driver cannot be empty - check settings.ini file.")
        self._Driver = d
        
    def Connect(self):
        instance = '' if not self.Instance else '//'+self.Instance
        port = '' if not self.Port else ':'+self.Port
        server = self.Server + instance + port
        #query = f"mssql+pyodbc://@{self.Server}{instance}{port}/{self.Db}?trusted_connection=yes&driver={self.Driver}"
        connection_string = (
            fr"Driver={self.Driver};"
            fr"Server={server};"
            fr"Database={self.Db};"
            fr"Trusted_Connection=yes;"
        )
        connection_url = URL.create(
            "mssql+pyodbc", 
            query={"odbc_connect": connection_string}
        )
  #      connection_url = URL.create(
  #  "mssql+pyodbc",
  #  query={
  #      "odbc_connect": f"DRIVER={{{self.Driver}}};SERVER={{{server}}};DATABASE={{{db}}};UID={{{user}}};PWD={{{password}}}"
  #  }
#)
        self.Engine = create_engine(connection_url, fast_executemany=True)
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
            

   