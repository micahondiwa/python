'''
* Receives miles and converts to kilometers
* Converts miles to a float
* Determines Kilometers = miles * 1.60934
'''
miles = input('Enter distance in miles:')
miles = float(miles)
kilometers = miles * 1.60934
print("Distance in Kilometers: {}".format(kilometers),"KM")