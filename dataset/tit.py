import pandas as pd 
import sqlite3
import matplotlib.pyplot as plt
# 1. نعمل اتصال بقاعدة البيانات ونرفع فيها الداتا الأصلية
conn=sqlite3.connect("m.db") 
df=pd.read_csv("titanic.txt")
df.to_sql("m",conn,if_exists="replace")
# نستكشف الداتا ونشوف تفاصيلها قبل التنظيف
print(df["Sex"].value_counts())
print(df.isnull().sum())
print(df.describe())
print(df.groupby("Sex")["Survived"].mean())

# مرحلة تنظيف الداتا
df=df.drop_duplicates() #حذف المتكرر
df=df.rename(columns={"Sex":"gender","Fare":"ticket_price"}) # تغير الاسم لاسامي ابسط خطوه اختياريه

df["Age"]=df["Age"].fillna(df["Age"].mean())   # نملي الاعمار الفاضيه بالعمر المتوسط
df=df.sort_values(by="Age",ascending=True) # نرتب الجدول بناء علي الاعمار وده برضو اختياري ولكن جمالي 

df=df.drop(columns=["Cabin"]) # العمود ده معظمه فاضي ومش مهم فبنحذفه

df=df[df["Age"]>0]  # ده بنشيل اي عمر بالسالب ولكن في الداتا مفيش اي عمر بالسالب فاذن ملهاش لازمه 
df=df.dropna(subset=["Embarked"]) # بيشيل الصفوف الفاضيه الي االعمود ده فها فاضيه
# ده رسم بياني بيوضح العلاقات بين المتغيرات لو احتجناه
survival_by_gender = df.groupby("gender")["Survived"].mean()

survival_by_gender.plot(kind="bar", color=["pink", "blue"])
plt.title("Survival Rate by Gender") 
plt.xlabel("Gender")                
plt.ylabel("Survival Rate")  
plt.show()                        
# data reproccing نخلي الداتا معظمها ارقام وايضا نوحد النظام العددي لارقام
df["sex_code"]=df["gender"].map({"male":0,"female":1})
df["fare_normalized"]=df["ticket_price"]/df["ticket_price"].max()
#make a new table which save the clean table inside it
df.to_sql("n",conn, if_exists="replace")
# يناخد جزء من الداتا نطبعه عشان نتاكد انه موافق للشروط 
sample=df.sample(n=3,random_state=42)
print(sample)
conn.close()