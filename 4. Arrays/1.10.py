# 1.8 - Temperature report
temperatures = [
 3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
 4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
 -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
]
num_measurements = len(temperatures)
avg_temp = sum(temperatures)/num_measurements
min_temp = min(temperatures)
max_temp = max(temperatures)
neg_days = sum(1 for t in temperatures if t<0)

print("TEMPERATURE REPORT")
print("Month: March")
print("Number of measurements:", num_measurements)
print("Average temperature in the month:", avg_temp)
print("Minimum temperature:", min_temp)
print("Maximum temperature:", max_temp)
print("Number of days with negative temperature:", neg_days)
