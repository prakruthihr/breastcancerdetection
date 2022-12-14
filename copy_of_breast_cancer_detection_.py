# -*- coding: utf-8 -*-
"""Copy of breast cancer detection .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1541UfHDPoZRXX3ci6iNYJ5Lf_zlI-3Qe
"""

import numpy as np

import sklearn.datasets

breast_cancer=sklearn.datasets.load_breast_cancer()
print(breast_cancer)



x=breast_cancer.data
y=breast_cancer.target
print(x,y)
print(x.shape,y.shape)

import pandas as pd
data=pd.DataFrame(breast_cancer.data,columns=breast_cancer.feature_names)
data['class']=breast_cancer.target
data.head()
data.describe()

print(data['class'].value_counts())

print(breast_cancer.target_names)
data.groupby('class').mean()

from os import X_OK

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1,stratify=y,random_state=1)
print(x.mean(),x_test.mean(),x_train.mean())
print(y.mean(),y_test.mean(),y_train.mean())

#logistic regression
from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression()
classifier.fit(x_train,y_train)

from sklearn.metrics import accuracy_score
prediction_on_training_data= classifier.predict(x_train)
accuracy_on_training_data=accuracy_score(y_train,prediction_on_training_data)
print("acuracy",accuracy_on_training_data)

prediction_on_test_data= classifier.predict(x_test)
accuracy_on_test_data=accuracy_score(y_test,prediction_on_test_data)
print("accuracy test",accuracy_on_test_data)

#detection of cancer
import numpy as np
input_data=(17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189)
input_data_as_array=np.asarray(input_data)
print(input_data_as_array)
#reshape
input_reshaped=input_data_as_array.reshape(1,-1)
prediction=classifier.predict(input_reshaped)
print(prediction)
if prediction[0]==0:
  print("breast cancer is malignant")
else:
  print("breast cancer is benign")