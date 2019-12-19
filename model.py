import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import requests
import json
print("Succesfully Imported")

#import data set, look at head of dataframe for data accuracy confirmation
df = pd.read_csv(r'C:\Users\dveras\Downloads\countries.csv')
df.head()


#set variables
X = df[['lifeExpectancy']]
y = df['gdpPerCapita']


#split set into training and test 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size= 0.3,random_state=101)

##print("Check One")
from sklearn.linear_model import LinearRegression

##print("2")

#fit simple linear regression to training set
lm = LinearRegression()
lm.fit(X_train, y_train)


#predict test set results
predictions = lm.predict(X_test)


#save model to disk
pickle.dump(lm, open('model.pkl','wb'))

#loading model to compare results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[1.8]]))
