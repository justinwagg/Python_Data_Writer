#import libraries
import random
import pprint as p
import csv

squares = []

#append 1000 random values with mean of 1 and stdev of .2
for i in range(1000):
	squares.append(random.gauss(1,.2))

#open and write values to a csv file
with open('test2.csv' , 'w') as csvfile:
	test = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for i in range(len(squares)):
		test.writerow([squares[i]])
