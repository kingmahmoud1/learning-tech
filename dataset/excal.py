import pandas as pd
df=pd.read_excel("Book1.xlsx")
df=df.drop_duplicates()
df=df[df["age"]>0]
df=df[df["score"]>0]
df["age"]=df["age"].fillna(df["age"].mean())
df["gender_code"]=df["gender"].map({'male':0,'female':1})
df["score_simple"]=df["score"]/100
df.to_excel("clean_stu.xlsx",index=False)
sample=df.sample(n=2,random_state=42)
print(sample)