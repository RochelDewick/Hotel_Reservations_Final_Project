import pandas as pd
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
        self.Server = os.getenv('DB_SERVER', '')
        self.Driver = os.getenv('DB_DRIVER', '')
        self.Db = os.getenv('DB_DATABASE', '')
        
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
    def Driver(self, d):
        if not d: raise Exception("Driver cannot be empty - check settings.ini file.")
        self._Driver = d
        
    Db = property(operator.attrgetter('_Db'))
    @Db.setter
    def Db(self, d):
        if not d: raise Exception("Database cannot be empty - check settings.ini file.")
        self._Db = d
        
    def Connect(self):
        instance = '' if not self.Instance else '\\'+self.Instance
        port = '' if not self.Port else ','+self.Port
        server = self.Server + instance + port

        connection_string = (
            fr"Driver={self.Driver};"
            fr"Server={server};"
            fr"Database={self.Db};"
            fr"Trusted_Connection=yes;"
            fr"TrustServerCertificate=yes;"
        )
        connection_url = URL.create(
            "mssql+pyodbc", 
            query={"odbc_connect": connection_string}
        )
  
        self.Engine = create_engine(connection_url, fast_executemany=True)
        #import urllib.parse
        #print(urllib.parse.unquote(repr(self.Engine.url)))
  
        self.Cursor = self.Engine.connect()

        self.m_bConnected = True
        print("Succesfully connected.")
        
        return self.m_bConnected
    
    def getEngine(self):
        return self.Engine
        
    def Disconnect(self):
        if self.m_bConnected:
            close_all_sessions()
            self.m_bConnected = False
            

   