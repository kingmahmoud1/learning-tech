import sqlite3
import pandas as pd
conn=sqlite3.connect("ch1.db")
df=pd.read_sql_query("select * from tb1",conn)
print(df.describe())
print(df.isnull().sum())
df=df[(df["price"]<100000)&(df["price"]>0)|df["price"].isna()]
df["price"]=df["price"].fillna(df["price"].mean())
df.dropna(subset="city")
df.drop_duplicates()
df=df[(df["discount_pct"]>=0)&(df["discount_pct"]<=100)]

