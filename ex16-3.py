import csv
from datetime import datetime

from matplotlib import pyplot as plt 

filename = 'sitka_weather_2014.csv'

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	precepitations1, dates1 = [], []
	for row in reader:
		print(row[19])
		try:
			current_date = datetime.strptime(row[0], "%Y-%m-%d")
			precepitation = float(row[19])
		except ValueError:
			print(current_date, 'missing data')
		else:
			precepitations1.append(precepitation)
			dates1.append(current_date)

filename = 'death_valley_2014.csv'

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	precepitations2, dates2 = [], []
	for row in reader:
		print(row[19])
		try:
			current_date = datetime.strptime(row[0], "%Y-%m-%d")
			precepitation = float(row[19])
		except ValueError:
			print(current_date, 'missing data')
		else:
			precepitations2.append(precepitation)
			dates2.append(current_date)



fig = plt.figure(dpi=128, figsize=(10, 6))

plt.plot(dates1, precepitations1, label='Sitka')
plt.plot(dates2, precepitations2, label='Death Valley')
plt.legend()
title = 'Daily Precipation - 2014'
plt.title(title, fontsize=31)

plt.show()