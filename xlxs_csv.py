import pandas as pd

read_file = pd.read_excel (r'/Users/james/Desktop/ASX 200 (XJO).xlsx')
read_file.to_csv (r'/Users/james/Desktop/asx200.csv', index = None, header=True)
