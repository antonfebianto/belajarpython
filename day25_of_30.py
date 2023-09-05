import pandas as pd


print(3*"=","Exercise 25",3*"=")
dframe = pd.read_csv('data/hacker_news.csv')
print(dframe)

dt_top = dframe.head()
dt_bot = dframe.tail()
dt_len = len(dframe)
dt_col = dframe.columns
dt_len_col = len(dt_col)
print("5 Data Pertama :")
print(dt_top)
print("\n5 Data Terakhir")
print(dt_bot)
print("Banyak data : ",dt_len)
print("Banyak Kolom :", dt_len_col)
#filter_py = dframe[dframe.str.contains('python', case=False)]
#print(filter_py)