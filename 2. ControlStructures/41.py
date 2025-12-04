###
# A program that convert time
#
time_24 = input("Enter time (24-hour format): ")
parts = time_24.split(":")
hours = int(parts[0])
minutes = int(parts[1])

# ustalenie am/pm
if hours >= 12:
    am_pm = "pm"
else:
    am_pm = "am"

# konwersja godzin do formatu 12h
if hours == 0:
    hours = 12
elif hours > 12:
    hours -= 12

print(f"Time in 12-hour format: {hours}:{minutes:02d}{am_pm}")


