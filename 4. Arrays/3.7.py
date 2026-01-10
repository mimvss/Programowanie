# Longest name
names = ["Genowefa","Onufry","Celestyna","Alojzy","Pankracy"]
longest = names[0]
for n in names:
    if len(n) > len(longest):
        longest = n
print("Names:", *names)
print("Longest name:", longest)
