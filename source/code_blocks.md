```python
import mysql.connector
import mysql

db = mysql.connector.connect(option_files='james.conf') ## separate file for connecting to DB with secure info
print(f"Connection ID: {db.connection_id}")
print(f"DB: {db}")
cursor = db.cursor()

df = pd.read_sql('SELECT * FROM asx_s_and_p', con = db)

print(df.head)
```

    Connection ID: 3171
    DB: <mysql.connector.connection.MySQLConnection object at 0x7f9ac301a790>
    <bound method NDFrame.head of            date     asx_open  s_and_p_open
    0    1992-12-01  1452.300049    431.350006
    1    1993-01-01  1576.099976    435.700012
    2    1993-02-01  1538.300049    438.779999
    3    1993-03-01  1652.800049    443.380005
    4    1993-04-01  1676.400024    451.670013
    ..          ...          ...           ...
    331  2020-07-01  5897.899902   3105.919922
    332  2020-08-01  5927.799805   3288.260010
    333  2020-09-01  6060.500000   3507.439941
    334  2020-10-01  5815.899902   3385.870117
    335  2020-10-12  6102.200195   6102.200195
    
    [336 rows x 3 columns]>


Inspect the df for column labels and data integrity


```python
plt.title('ASX200 compared with S&P 500 1992 - Present', fontsize = 13, fontweight = 'bold')
plt.plot('date', 'asx_open', data = df, label = 'ASX 200') ## ASX 200 open data
plt.plot('date', 's_and_p_open', data = df, label = 'S&P 500') ## S&P 500 open data
plt.legend()
plt.xlabel('Time')
plt.ylabel('Price')
```




    Text(0.5, 1.0, 'ASX200 compared with S&P 500 1992 - Present')






    [<matplotlib.lines.Line2D at 0x7f9ac315dfa0>]






    [<matplotlib.lines.Line2D at 0x7f9ac317a5e0>]






    <matplotlib.legend.Legend at 0x7f9ac315dbe0>






    Text(0.5, 0, 'Time')






    Text(0, 0.5, 'Price')




    
![png](output_2_6.png)
    


Findings and Questions for further investigation:
 - The period 2007 to mid 2008 need investigation - what happened in Australia compared with the US markets?
 - It appears the ASX200 is more volatile than the S&P500 across the period. 


```python

```
