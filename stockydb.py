# connecting to the sql database
# insert information into database

import pyodbc 

server = 'stockyserver.database.windows.net' 
database = 'Stockydb'
username = 'srivas60@msu.edu' 
password = 'Hearts@12'
driver = '{ODBC Driver 17 for SQL Server}'

try:
    cnxn = pyodbc.connect('DRIVER=' + driver + 
                      ';SERVER=' + server + 
                      ';DATABASE=' + database + 
                      ';UID=' + username + 
                      ';PWD=' + password)

    cursor = cnxn.cursor()
    print('Connection established')
except:
    print('Cannot connect to SQL server')