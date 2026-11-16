# Make Data or GEt Data
import pandas as pd
raw_list={"name":["mahmoud","ALi","mona","salma","mahmoud"],
          "age":[21,-12,None,32,21],
          "gender":["male","male","famale","famale","male"]
          ,"score":[13,98,-10,19,13]}


df=pd.DataFrame(raw_list)
print(df)
#clean
 #نزيل المتكرر
df=df.drop_duplicates()

print(df)
 #مفيش بيانات فبعمل المتوقع انه المتوسط
df["age"]=df["age"].fillna(df["age"].mean())

print(df)
 #العمر بالسالب
df=df[df["age"]>0]
df=df[df["score"]>0]
print(df)
#prepare data for com
df["gander_code"]=df["gender"].map({"male":0,"famale":1})
df["score_normalized"]=df["score"]/100

print(df)

#choose random data 
sample=df.sample(n=1,random_state=42)

print(sample)