import pandas as pd
import sqlite3 
conn=sqlite3.connect("students.db")
df=pd.read_sql_query("SELECT*FROM raw_list",conn)
df=df.drop_duplicates()
df=df[df["age"]>0]
df=df[df["score"]>0]
df["age"]=df["age"].fillna(df["age"].mean())
df["gender_code"]=df["gender"].map({'"male"':0,'"female"':1})
df["score_simple"]=df["score"]/100
df.to_sql("clean_stu",conn,if_exists="replace",index=False)
sample=df.sample(n=2,random_state=42)
print(sample)
conn.close()