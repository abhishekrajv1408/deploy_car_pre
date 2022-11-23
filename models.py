import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler



def predict_di(data):
    originaldf = pd.read_csv('car.csv')
    df = originaldf
    df.drop('name', axis = 1, inplace = True) #name column is of no use
    df = df[df['fuel'] != 'Electric']
    df['fuel'] = df['fuel'].map({'Diesel':1,'Petrol':2,'CNG':3,'LPG':4}) #converting string object to integer object
    df['seller_type'] = df['seller_type'].map({'Individual':1,'Dealer':2,'Trustmark Dealer':3})
    df['transmission'] = df['transmission'].map({'Manual':1,'Automatic':2})
    df['owner'] = df['owner'].map({'First Owner':1,'Second Owner':2,'Third Owner':3,'Fourth & Above Owner':4,'Test Drive Car':5})
    df = df[df['owner']!=5]
    df = df[df['fuel']!=4]
    df = df[df['fuel']!=3]
    df = df[df['owner']!=4]
    df.drop('km_driven', axis =1, inplace = True) #dropping columns with less affect
    x = df[['year', 'fuel', 'seller_type',
          'transmission', 'owner']]
    y = df['selling_price']
    from sklearn.model_selection import train_test_split
    xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size = 0.3,random_state =90) 
    from sklearn.neighbors import KNeighborsRegressor #importing the algorithm
    from sklearn.metrics import mean_squared_error #importing library for evaluating the model  
    model1 = KNeighborsRegressor(n_neighbors = 4) #making the model
    model1.fit(xtrain,ytrain) #Trained the model
    pre = model1.predict(data)
    return pre