#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from matplotlib import pyplot


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
start_time = time()
print start_time


##slice the training dataset down to 1% of its original size, tossing out 99% of the training data.
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 


from sklearn.svm import SVC
#clf = SVC(kernel='linear')
clf = SVC(kernel='rbf', C=10000.0)
#clf = SVC(C=1.0, gamma=1000, kernel='linear')
clf.fit(features_train, labels_train) 

pred=clf.predict(features_test)
print pred

elapsed_time=time()-start_time
print elapsed_time

print clf.score(features_test, labels_test)
print pred[10], pred[26], pred[50]

###print out the score of prediction
from sklearn.metrics import accuracy_score
print accuracy_score(pred, labels_test)
###print out number of correct prediction
print accuracy_score(pred, labels_test, normalize=False)
#########################################################
j=0
for i in pred:
 if i==1:
  j+=1
print j
#plot(features_test)
#########################################################


