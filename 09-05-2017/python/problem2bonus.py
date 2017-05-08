result = 0

def isPalindrome(value):
    for i in range(len(value)/2):
        if value[i] != value[len(value) - i - 1]:
            return False
    return True

for counter in range(10, 100000):
    if isPalindrome(str(counter)):
        result = result + 1
        
        
print("Number of palindromes in between 10 & 99999 is:")
print(result)