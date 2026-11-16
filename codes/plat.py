# Make Data or GEt Data
import pandas as pd
raw_list={"name":["mahmoud","ALi","mona","salma","mahmoud"],
          "age":[21,-12,None,32,21],
          "gender":["male","male","famale","famale","male"]
          ,"score":[13,98,-10,19,13]}
import sqlite3
conn=sqlite3.connect("students.db")
df2=pd.read_sql_query("SELECT*FROM raw_list",conn)
print(df2)

df=pd.DataFrame(raw_list)
#print(df)
#clean
 #نزيل المتكرر
df=df.drop_duplicates()
df2=df2.drop_duplicates()
#print(df)
 #مفيش بيانات فبعمل المتوقع انه المتوسط
df["age"]=df["age"].fillna(df["age"].mean())
df2["age"]=df2["age"].fillna(df2["age"].mean())
#print(df)
 #العمر بالسالب
df=df[df["age"]>0]
df=df[df["score"]>0]
df2=df2[df2["age"]>0]
df2=df2[df2["score"]>0]
#print(df)
#prepare data for com
df["gander_code"]=df["gender"].map({"male":0,"famale":1})
df["score_normalized"]=df["score"]/100
df2["gander_code"]=df2["gender"].map({"male":0,"famale":1})
df2["score_normalized"]=df2["score"]/100
#print(df)
df2.to_sql("clean_stu",conn,if_exists="replace",index=False)
#choose random data 
sample=df.sample(n=1,random_state=42)
sample2=df2.sample(n=2,random_state=42)
print(sample2)
conn.close()

#print(sample)