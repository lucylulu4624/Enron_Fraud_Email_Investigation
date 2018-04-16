#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (errorerence between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    from itertools import izip 
    
    #print'Pass data good'
    cleaned_data = []

    ### your code goes here
    counter=0
    error= [abs(x-y) for x, y in izip(predictions, net_worths)]
    for counter in range(0,4):
		max_pos=0
		for max_error in error:
			if max_error==max(error):
				max_pos=error.index(max_error)
				print max_error,max_pos
				counter=counter+1
				print counter
				error.remove(error[max_pos])
				predictions.remove(predictions[max_pos])
				ages.remove(ages[max_pos])
				net_worths.remove(net_worths[max_pos])
			
    
    cleaned_data=[list(x) for x in izip(ages, net_worths, error)]
    print len(predictions)
    print len(ages)
    print len(net_worths)
    return cleaned_data

##Testing data:	
#pred=[4,9,2,6,8]
#net_worths=[1,6,4,2,7]
#ages=[1,2,3,4,5]
#cleaned=outlierCleaner(pred, ages, net_worths)
#print pred
#print net_worths
#print ages
#print cleaned