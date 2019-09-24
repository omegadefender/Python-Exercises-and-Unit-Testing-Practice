arr = [1, 4, 2, 3, 0 , 5]
number = 7

x = min(arr)
y = max(arr)

while x < y:
    if x + y > sum:
        y -= 1
    elif x + y < sum:
        x += 1
    else:
        print("(", x, y, ")")
        x += 1