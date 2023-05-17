from pathlib import Path 
import csv 
from datetime import datetime

import matplotlib.pyplot as plt 

path = Path('weather_data/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extract dates, precipitation.
dates, precip = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    precipitation = (float(row[5]))
    dates.append(current_date)
    precip.append(precipitation)

# Plot Precipitation.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, precip, color='blue')

# Formatting
title = "Daily Precipitation in Sikta, 2021"
ax.set_title(title, fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Precipitation (mm)", fontsize=16)
ax.tick_params(labelsize=14)

plt.show()