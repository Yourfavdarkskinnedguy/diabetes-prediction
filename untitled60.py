# -*- coding: utf-8 -*-
"""Untitled60.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1A7dVO4fu8UzpohnnUSs6swCO4dRaanIt
"""

import numpy as np
import pandas as pd
from sklearn.utils import resample
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

!unzip "/content/archive (25).zip"

data= pd.read_csv("/content/diabetes_dataset.csv")

data.head()

data.shape

data.describe()

data.info()

data['Outcome'].value_counts()

minority_data= data[data['Outcome']==1]
majority_data= data[data['Outcome']==0]

minority_data.shape

majority_data.shape

resample?

minority_data_resampled= resample(minority_data,
                                  replace=True,
                                  n_samples=len(majority_data),
                                  random_state=42)

minority_data.describe()

minority_data_resampled.head()

new_data= pd.concat([majority_data, minority_data_resampled])

new_data.head()

new_data.groupby('Outcome')

new_data.reset_index(drop=True, inplace=True)



from sklearn.utils import shuffle

new_data= shuffle(new_data, random_state=2)

new_data.reset_index(drop=True, inplace=True)

new_data.head()

new_data.shape

new_data.describe()

data.describe()

X= new_data.drop(['Outcome'], axis=1)
Y= new_data['Outcome']

X_train, X_test, Y_train, Y_test= train_test_split(X, Y, test_size=0.25, random_state=2)

Y_train.shape

model= RandomForestClassifier(n_estimators=100, random_state=42)

from sklearn.metrics import accuracy_score

class model_trainer_and_evaluator():

  def train_model(model, X_train, Y_train):
    model.fit(X_train, Y_train)
    return model

  def evaluate_model(metric, model, X_test, Y_test):
    y_pred= model.predict(X_test)
    acc_score= metric(Y_test, y_pred)
    return acc_score

model1= model_trainer_and_evaluator.train_model(model, X_train, Y_train)

acc_score= model_trainer_and_evaluator.evaluate_model(accuracy_score, model1, X_test, Y_test)
print(acc_score)

import pickle

pickle.dump(model1, open("diabetes_model", "wb"))

pickle.dump(model1, open("diabetes_model.pkl", "wb"))

