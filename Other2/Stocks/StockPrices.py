import requests
import math

# ex, get_raw_dict('GOOG', '2009-09-11', '2010-03-10') i.e. date is yyyy-mm-dd, most recent date first in list
def get_raw_dict(ticker, st, end):
	site = "http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.historicaldata%20where%20symbol%20%3D%20%22" + ticker + "%22%20and%20startDate%20%3D%20%22" + st + "%22%20and%20endDate%20%3D%20%22" + end + "%22&format=json&env=http%3A%2F%2Fdatatables.org%2Falltables.env"
	raw_data = requests.get(site)
	raw_json = raw_data.json()
	# list of dictionaries of the form Volume, Adj_Close, High, Date (yyyy-mm-dd), Low, date, Close, Open
	return raw_json['query']['results']['quote']

# return a list of tuples of the form (date, closing price), with most recent date first in output list
def get_closes_tup(input_dict):
	ans = []
	for day in input_dict:
		ans.append((day['Date'], day['Close']))
	return ans

# return a list of closing prices, with the most recent close first
def get_closes(input_dict):
	ans = []
	for day in input_dict:
		ans.append(float(day['Close']))
	return ans

# returns the mean of a list of floats (just the prices)
def mean(lst):
	return sum(lst)/len(lst)

def standard_dev(lst):
	avg = mean(lst)
	variance = map(lambda x: (x-avg)**2, lst)
	return math.sqrt(sum(variance)/(len(variance)-1))


