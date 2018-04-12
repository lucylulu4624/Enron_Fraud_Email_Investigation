#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print len(enron_data)
print len(enron_data['METTS MARK'])
key=enron_data.keys()
#print key
print enron_data['METTS MARK']['poi']

i=0
for name in enron_data:
	if enron_data[name]['poi'] ==True:
		i+=1
print i

print enron_data['PRENTICE JAMES']['total_stock_value']
print enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print enron_data['SKILLING JEFFREY K']['exercised_stock_options']
print enron_data['SKILLING JEFFREY K']['total_payments']
print enron_data['LAY KENNETH L']['total_payments']
print enron_data['FASTOW ANDREW S']['total_payments']

###Quiz 27
i=0
for name in enron_data:
	if enron_data[name]['salary'] =='NaN':
		i+=1
print len(enron_data)-i

j=0
for name in enron_data:
	if enron_data[name]['email_address'] =='NaN':
		j+=1
print len(enron_data)-j

###Quiz 29
i=0
for name in enron_data:
	if enron_data[name]['total_payments'] =='NaN':
		i+=1
print i, i*1.0/len(enron_data)