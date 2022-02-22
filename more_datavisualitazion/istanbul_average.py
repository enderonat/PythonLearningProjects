import csv
from datetime import datetime

import matplotlib.pyplot as plt


filename = 'data/istanbul_2020_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	# Get dates and high temperatures from this file.
	dates, averages = [], []
	for row in reader:
		current_date = datetime.strptime(row[1], '%Y-%m-%d')
		try:
			average = (int(row[2])-32) * (5/9)
		except ValueError:
			print(f"Missing data for {current_date}")
		else:
			dates.append(current_date)
			averages.append(average)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, averages, c='green', alpha=0.5)

# Format plot.
plt.title("Daily temperatures İstanbul, 2020", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()