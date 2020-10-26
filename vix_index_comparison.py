import mysql.connector
import pandas as pd
mydb = mysql.connector.connect(
     host = "mdsi-dsp-spr-2020.cehiwpryiego.ap-southeast-2.rds.amazonaws.com",
     port = "3306",
     user = "min", ## Change as required
     password = "utsmdsi2020",
     database = "asx")

mycursor = mydb.cursor()
print('Database Open')

#join vix index to asx200 index monthly
df = pd.read_sql_query("SELECT * FROM asx.vix where Date > 2004-01-02", con=mydb)
print(df)
df_asx = pd.read_sql_query("SELECT * FROM asx.asx_s_and_p where date > '2004-01-02'", con=mydb)
print(df_asx)
df_comparison = pd.merge(df_asx,df,left_on='date', right_on='Date')
print(df_comparison)

#select 3 column - date, asx_open and vix close
df_comparison = df_comparison[["date","asx_open","Close"]]
print(df_comparison)

#test correlation of date matched two indexes, cor = -0.27965
import scipy.stats as stats
print(stats.pearsonr(df_comparison.asx_open,df_comparison.Close))


#test whether correlation is stronger if taking vix month n increase vs. asx month n+1 increase, result is cor = -0.0311
#correlation is close to none
df_comparison["asx_increase"] = (df_comparison.asx_open - df_comparison.asx_open.shift(1))/df_comparison.asx_open.shift(1)
df_comparison["vix_increase"] = (df_comparison.Close.shift(1) - df_comparison.Close.shift(2))/df_comparison.Close.shift(2)
df_comparison = df_comparison.dropna()
print(stats.pearsonr(df_comparison.asx_increase,df_comparison.vix_increase))