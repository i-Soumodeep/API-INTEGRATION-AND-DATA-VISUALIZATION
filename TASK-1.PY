import matplotlib.pyplot as plt

# Sample Kolkata weather data (hardcoded)
weather_data = {
    'temperature': 32.5,  # in °C
    'humidity': 78,       # in %
    'wind_speed': 4.2,    # in m/s
    'pressure': 1012,     # in hPa
    'condition': 'Partly Cloudy'
}

# Prepare data for bar chart
categories = ['Temperature (°C)', 'Humidity (%)', 'Wind Speed (m/s)', 'Pressure (hPa)']
values = [
    weather_data['temperature'],
    weather_data['humidity'],
    weather_data['wind_speed'],
    weather_data['pressure']
]
colors = ['#FF7F50', '#4682B4', '#3CB371', '#9370DB']  # Coral, SteelBlue, MediumSeaGreen, MediumPurple

# Create figure and axis
plt.figure(figsize=(10, 6))
bars = plt.bar(categories, values, color=colors, edgecolor='black')

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.1f}' if bar.get_x() != 3 else f'{height}',  # No decimal for pressure
             ha='center', va='bottom', fontsize=12)

# Customize the chart
plt.title('Current Weather in Kolkata', fontsize=16, pad=20)
plt.ylabel('Measurement Value', fontsize=12)
plt.xticks(fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add weather condition annotation
plt.annotate(f"Weather Condition: {weather_data['condition']}",
             xy=(0.5, -0.15), xycoords='axes fraction',
             ha='center', fontsize=12, style='italic')

plt.tight_layout()
plt.show()
