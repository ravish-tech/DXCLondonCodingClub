f1 = 1
f2 = 1
f3 = f1 + f2

result = 2 # As the third number is 2 and its even, we will start with this.

def isEven(num):
    if num%2 == 0:
        return True
    return False

for count in range(4,101):
    f1 = f2
    f2 = f3
    f3 = f1 + f2
    if isEven(f3):
        result = result + f3
        
print("Sum of all even numbers in series of 100 fibnocci numbers is:")
print(result)