import pandas as pd 
import sqlite3
conn=sqlite3.connect("m.db")
#import matplotlib.pyplot as plt
df=pd.read_csv("titanic.txt")
df.to_sql("m",conn,if_exists="replace")
print(df.describe())
df=df.drop_duplicates()
df=df.rename(columns={"Sex":"gender","Fare":"ticket_price"})
print(df["gender"].value_counts())
df["Age"]=df["Age"].fillna(df["Age"].mean())
df=df.sort_values(by="Age",ascending=True)

survival_by_gender = df.groupby("gender")["Survived"].mean()

# survival_by_gender.plot(kind="bar", color=["pink", "blue"])
# plt.title("Survival Rate by Gender") 
# plt.xlabel("Gender")                
# plt.ylabel("Survival Rate")  
# plt.show()                        
print(df.groupby("gender")["Survived"].mean())
df=df.drop(columns=["Cabin"])

df=df[df["Age"]>0]
df=df.dropna(subset=["Embarked"])
df["sex_code"]=df["gender"].map({"male":0,"female":1})
df["fare_normalized"]=df["ticket_price"]/df["ticket_price"].max()
df.to_sql("n",conn, if_exists="replace")
print(df.isnull().sum())
sample=df.sample(n=3,random_state=42)
print(sample)
conn.close()