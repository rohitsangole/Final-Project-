import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB


class Model:

    def __init__(self):
        self.name = ''
        path = 'dataset/depressionDataset.csv'
        df = pd.read_csv(path)
        df = df[['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'class']]

        
        df['q1'] = df['q1'].fillna(df['q1'].mode()[0])
        df['q2'] = df['q2'].fillna(df['q2'].mode()[0])
        df['q3'] = df['q3'].fillna(df['q3'].mode()[0])
        df['q4'] = df['q4'].fillna(df['q4'].mode()[0])
        df['q5'] = df['q5'].fillna(df['q5'].mode()[0])
        df['q6'] = df['q6'].fillna(df['q6'].mode()[0])
        df['q7'] = df['q7'].fillna(df['q7'].mode()[0])
        df['q8'] = df['q8'].fillna(df['q8'].mode()[0])
        df['q9'] = df['q9'].fillna(df['q9'].mode()[0])
        df['q10'] = df['q10'].fillna(df['q10'].mode()[0])
        df['class'] = df['class'].fillna(df['class'].mode()[0])

        self.split_data(df)

    def split_data(self,df):
        x = df.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]].values
        y = df.iloc[:, 10].values
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=24)
        self.x_train = x_train
        self.x_test = x_test
        self.y_train = y_train
        self.y_test = y_test

    def svm_classifier(self):
        self.name = 'Svm Classifier'
        classifier = SVC()
        return classifier.fit(self.x_train, self.y_train)
        y_pred = classifier.predict(x_test)

    def decisionTree_classifier(self):
        self.name = 'Decision tree Classifier'
        classifier = DecisionTreeClassifier()
        return classifier.fit(self.x_train,self.y_train)

    def naiveBayes_classifier(self):
        self.name = 'Naive Bayes Classifier'
        classifier = GaussianNB()
        return classifier.fit(self.x_train,self.y_train)

   
  