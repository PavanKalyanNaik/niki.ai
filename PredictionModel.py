import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import pickle as p
from sklearn.metrics import accuracy_score
f=open("C:/Users/A Pavan Kalyan Naik/OneDrive/Documents/Python Scripts/niki.ai_task/LabelledData .txt",'r')
lines=f.readlines()
qlist=[]
tylist=[]
for line in lines:
    stline=line.strip()
    a=stline.split(",,,")
    tylist.append(a[1])
    b=a[0].split(" ")
    if a[0].find("who") == 0:
        qlist.append(0)
    elif a[0].find("what") == 0:
        qlist.append(1)
    elif a[0].find("when") == 0:
        qlist.append(2)
    elif b[0] == "is" or b[0] == "are":
        qlist.append(3)
    else:
        qlist.append(4)
    
ds={'Question':qlist,'QuestionType':tylist}
df=pd.DataFrame(ds)
print(df.head())
feature=df.iloc[:,0:1]
label=df.iloc[:,1]
feature_train,feature_test,label_train,label_test=train_test_split(feature,label,test_size=0.25)
dt=DecisionTreeClassifier()
dt=dt.fit(feature_train,label_train)
pred=dt.predict(feature_test)
accuracy=accuracy_score(label_test,pred)
print("DTC",accuracy)

rf=RandomForestClassifier(n_estimators=50)
rf=rf.fit(feature_train,label_train)
pred=rf.predict(feature_test)
accuracy=accuracy_score(label_test,pred)
print("RFC",accuracy)

p.dump(rf,open("final_quest.pickle",'wb'))
