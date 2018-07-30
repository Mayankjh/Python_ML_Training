import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree,svm



df=pd.read_csv('PerpData1.csv')
# print(df.head())
features=list(df.columns[1:6])
y=df['Hired']
x=df[features]
# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)



def logiDB(p,b,i,f,c):
    model=LogisticRegression()
    model.fit(x,y)
    return (model.predict([[p,b,i,f,c]])[0])
    
def deciDB(p,b,i,f,c):
    model=tree.DecisionTreeClassifier()
    model=model.fit(x,y)
    return (model.predict([[p,b,i,f,c]])[0])

def rafoDB(p,b,i,f,c):
    clf=RandomForestClassifier(n_estimators=10)
    clf=clf.fit(x,y)
    return (clf.predict([[p,b,i,f,c]])[0])

def svmDB(p,b,i,f,c):
    clf=svm.SVC(kernel='linear',C=2.0).fit(x,y)
    return (clf.predict([[p,b,i,f,c]])[0])

def finalDB(n,p,b,i,f,c,h):
    global df
    df.loc[len(df)] = [n,p,b,i,f,c,h]
    df.to_csv('PerpData1.csv',encoding='utf-8', index=False)
    
#     return 1

# deciDB(0,0,0,0,0)