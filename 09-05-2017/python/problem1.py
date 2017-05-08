f1 = 1
f2 = 1
f3 = f1 + f2

for count in range(4,39):
    f1 = f2
    f2 = f3
    f3 = f1 + f2
print("39th Fibnocci number is:")
print(f3)