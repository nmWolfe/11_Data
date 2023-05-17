"""
Yes, this is difficult to read - it was for practice purposes
"""

from pathlib import Path 
import csv
from datetime import datetime

import matplotlib.pyplot as plt 

# Sitka 
path_1 = Path('weather_data/sitka_weather_2021_simple.csv')
lines_1 = path_1.read_text().splitlines()

reader_1 = csv.reader(lines_1)
header_row_1 = next(reader_1)

# Death Valley
path_2 = Path('weather_data/death_valley_2021_simple.csv')
lines_2 = path_2.read_text().splitlines()

reader_2 = csv.reader(lines_2)
header_row_2 = next(reader_2)

# Sitka
for index, column_header in enumerate(header_row_1):
    print(index, column_header)

# Death Valley
for index, column_header in enumerate(header_row_2):
    print(index, column_header)

# Extract dates, and high/low temps for Sitka
dates_1, highs_1, lows_1 = [], [], []
for row in reader_1:
    current_date_1 = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high_1 = int(row[4])
        low_1 = int(row[5])
    except ValueError:
        print(f"Missing daata for {current_date_1}")
    else:
        dates_1.append(current_date_1)
        highs_1.append(high_1)
        lows_1.append(low_1)

# Extract dates and high/low temps for Death Valley
dates_2, highs_2, lows_2 = [], [], []
for row in reader_2:
    current_date_2 = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high_2 = int(row[3])
        low_2 = int(row[4])
    except ValueError:
        print(f"Missing data for {current_date_2}")
    else:
        dates_2.append(current_date_2)
        highs_2.append(high_2)
        lows_2.append(low_2)

plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(16,8))

# Plot high/low temps for Death Valley
ax.plot(dates_2, highs_2, color='red', alpha=0.5, label='Death Valley (High)')
ax.plot(dates_2, lows_2, color='blue', alpha=0.5, label='Death Valley (Low)')
# ax.fill_between(dates_2, highs_2, lows_2, facecolor='blue', alpha=0.1)

# Plot high/low temps for Sitka. 
ax.plot(dates_1, highs_1, color='crimson', alpha=0.5, label='Sitka (High)')
ax.plot(dates_1, lows_1, color='royalblue', alpha=0.5, label='Sitka (Low)')
# ax.fill_between(dates_1, highs_1, lows_1, facecolor='blue', alpha=0.1)

# Show the difference between the two temperatures
ax.fill_between(dates_1, highs_1, highs_2, facecolor='blue', alpha=0.1)
ax.fill_between(dates_1, lows_1, lows_2, facecolor='red', alpha=0.1)

# Format Plot
title = "Daily Temperatures Difference Between Sitka and Death Valley\n2021"
ax.set_title(title, fontsize=24)
ax.set_xlabel('Dates', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

# Add labels
leg = plt.legend()

# Display the graph
plt.show()