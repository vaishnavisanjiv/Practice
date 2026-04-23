# date temp dew_point wind_speed
weather_data = [
    "2026-04-01 30 20 10",
    "2026-04-02 32 22 12",
    "2026-04-03 28 19 8"
]

temp_sum = 0
dew_sum = 0
wind_sum = 0
count = 0

for line in weather_data:
    parts = line.split()
    
    temp = int(parts[1])
    dew = int(parts[2])
    wind = int(parts[3])
    
    temp_sum += temp
    dew_sum += dew
    wind_sum += wind
    count += 1

avg_temp = temp_sum / count
avg_dew = dew_sum / count
avg_wind = wind_sum / count

print("Average Temperature:", avg_temp)
print("Average Dew Point:", avg_dew)
print("Average Wind Speed:", avg_wind)