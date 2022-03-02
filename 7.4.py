# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 10:39:26 2022

@author: bl4an
"""

import pandas as pd
import seaborn as sns

df = sns.load_dataset('titanic')
print(df.head())
print('\n')

pd.set_option('display.max_columns', 15)
print(df.head())

print(df.info())

rdf = df.drop(['deck', 'embark_town'], axis = 1)
print(rdf.columns.values)

rdf = rdf.dropna(subset = ['age'], how = 'any', axis = 0)
print(len(rdf))

most_freq = rdf['embarked'].value_counts(dropna=True).idxmax()
print(most_freq)
print('\n')

print(rdf.describe(include='all'))
print('\n')

rdf['embarked'].fillna(most_freq, inplace=True)

ndf = rdf[['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'embarked']]
print(ndf.head())

onehot_sex = pd.get_dummies(ndf['sex'])
ndf = pd.concat([ndf, onehot_sex], axis=1)

onehot_embarked = pd.get_dummies(ndf['embarked'], prefix = 'town')
ndf = pd.concat([ndf, onehot_embarked], axis = 1)

ndf.drop(['sex', 'embarked'], axis = 1, inplace = True)
print(ndf.head())

X = ndf[['pclass', 'age', 'sibsp', 'parch', 'female', 'male',
         'town_C', 'town_Q', 'town_S']]
y = ndf['survived']

from sklearn import preprocessing
X = preprocessing.StandardScaler().fit(X).transform(X)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 10)

print('train data 개수: ', X_train.shape)
print('test data 개수: ', X_test.shape)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

y_hat = knn.predict(X_test)
print(y_hat[0:10])
print(y_test.values[0:10])

from sklearn import metrics
knn_matrix = metrics.confusion_matrix(y_test, y_hat)
print(knn_matrix)

knn_report = metrics.classification_report(y_test, y_hat)
print(knn_report)