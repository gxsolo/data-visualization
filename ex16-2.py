import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get dates, high and lows temperatures from file.
filename = 'death_valley_2014.csv'

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	mean_temperature1, dates1 = [], []
	for row in reader:
		try:
			current_date = datetime.strptime(row[0], "%Y-%m-%d")
			mean = (int(row[2])-32)/(9/5)
		except ValueError:
			print(current_date, 'missing data')
		else:
			dates1.append(current_date)
			mean_temperature1.append(mean)


filename = 'sitka_weather_2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	mean_temperature2, dates2 = [], []
	for row in reader:
		try:
			current_date = datetime.strptime(row[0], "%Y-%m-%d")
			mean = (int(row[2])-32)/(9/5)
		except ValueError:
			print(current_date, 'missing data')
		else:
			dates2.append(current_date)
			mean_temperature2.append(mean)



# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))

plt.plot(dates2, mean_temperature2, label='Death Valley')
plt.plot(dates1, mean_temperature1, label='Sitka')
plt.legend()


#plt.plot(dates, mean_temperature2, c='blue', alpha=0.5)

# Format plot.
title = "Daily mean temperatures - 2014"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
#fig.autofmt_xdate()
plt.ylabel("Temperature (C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
