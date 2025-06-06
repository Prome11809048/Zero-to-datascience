# -*- coding: utf-8 -*-
"""Numerical Dataset Pre-processing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_8oarS__gHyO9vJCKbrFw5MVSfl1TpCl

Importing the dependencies

Scikit-learn (sklearn) is a powerful and easy-to-use Python library for machine learning. It provides simple tools for data mining and data analysis, and is built on top of NumPy, SciPy, and matplotlib. Scikit-learn includes a wide range of algorithms for classification, regression, clustering, dimensionality reduction, model selection, and preprocessing, making it ideal for both beginners and experts in machine learning.
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

"""Data collection and Data-Pre-processing"""

# loading csv file into pandas dataframe
diabetes_data = pd.read_csv('diabetes.csv')

# first five rows of the dataframe
diabetes_data.head()

# number of rows and columns
diabetes_data.shape

# For analysis
diabetes_data.describe()

"""Separating Features and Target"""

X = diabetes_data.drop(columns= 'Outcome', axis = 1)
Y = diabetes_data['Outcome']

print(X)

print(Y)

"""Data Standardization"""

scaler = StandardScaler()

standardized_data = scaler.fit_transform(X)

print(standardized_data)

X = standardized_data

print(X)

"""Splitting the dataset into Training data and Testing data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, stratify = Y, random_state = 2)

print(X.shape, X_train.shape, X_test.shape)

print(Y.shape, Y_train.shape, Y_test.shape)