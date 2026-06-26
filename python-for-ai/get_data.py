import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os


# 1st step:Get weather data with dates
# Calculate dates
today = datetime.now()
print(today)
week_ago = today - timedelta(days=7)
print(week_ago)

# Format dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
print(start_date)
end_date = today.strftime("%Y-%m-%d")
print(end_date)

# Get Paris weather for past week
url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
print(f"\n{data}\n")


# 2nd step: Load into pandas
# Extract the daily data
daily_data = data['daily']
print(daily_data)

# Create a DataFrame
df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})

# Convert date strings to datetime
df['date'] = pd.to_datetime(df['date'])

print(f"{df}\n\n")



# 3rd step: Visualize the data with matplotlib
# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Paris Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('weather_chart.png')
plt.show()



# 4th step - Save to CSV

# Create data folder if it doesn't exist
if not os.path.exists('weather-data'):
    os.makedirs('weather-data')

# Save to CSV
df.to_csv('weather-data/paris_weather.csv', index=False)
print("Data saved to weather-data/paris_weather.csv")