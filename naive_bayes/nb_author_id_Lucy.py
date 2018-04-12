#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""    
import sys
from time import time
#sys.path.append("../tools/")
sys.path.append("C:\Users\binglu\Documents\py_code\ML_Class\ud120-projects\tools")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
y_pred = clf.fit(features_train, labels_train).predict(features_test)
print y_pred

###print out the score of prediction
from sklearn.metrics import accuracy_score
print accuracy_score(y_pred, labels_test)
###print out number of correct prediction
print accuracy_score(y_pred, labels_test, normalize=False)
#########################################################


