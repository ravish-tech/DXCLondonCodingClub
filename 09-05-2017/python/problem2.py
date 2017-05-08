input = "madam"

start = 0
end = len(input) - 1

palindrome = True

for i in range(len(input)/2):
    if input[start + i] != input[end - i]:
        # It is not a palindrom
        palindrome = False
        break;

print(input)

if palindrome:
    print("Is a palindrome")
else:
    print("Is not a palindrome")