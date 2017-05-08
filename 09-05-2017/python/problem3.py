## To find x + y = 100. It is clear that x <= 100 & y <= 100
result = 0

for x in range(0, 101):
    for y in range(0,101):
        if x + y == 100:
            print(x,y)
            result = result + 1


print(result)