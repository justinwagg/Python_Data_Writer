#import libraries
import random
import pprint as p
import csv
import numpy
import plotly.plotly as py
import plotly.graph_objs as go

squares = []

#append 1000 random values random.gauss(mean,stdev)
for i in range(1000):
	squares.append(random.gauss(100,50))

#open and write values to a csv file
# with open('test2.csv' , 'w') as csvfile:
# 	test = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
# 	for i in range(len(squares)):
# 		test.writerow([squares[i]])

# hist, bin_edges = numpy.histogram(squares, bins = 100)

# p.pprint(hist)

data = [go.Histogram(x = squares)]
plot_url = py.plot(data, filename = 'histogram')
