import mysql.connector ## ensure mysql-connector-python is installed
import pandas as pd
import numpy as np

mydb = mysql.connector.connect(
     host = "mdsi-dsp-spr-2020.cehiwpryiego.ap-southeast-2.rds.amazonaws.com",
     port = "3306",
     user = "james", ## Change as required
     password = "utsmdsi2020",
     database = "asx")

mycursor = mydb.cursor()

print('Database Open')

df = pd.read_sql_query("SELECT * FROM asx.cashrate", con=mydb)

## insert python code here to execute

print(df.head(20)) ## example of the information in the cashrate table in the database ASX


## this command can be used to access the database from $bash
## mysql -h mdsi-dsp-spr-2020.cehiwpryiego.ap-southeast-2.rds.amazonaws.com -p3306 -u james -p
