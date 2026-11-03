total = 0

while True:
    num = int(input("enter a number: "))
    if num < 0:
        break
    if num == 0:
        continue
    print("Positive number:", num)
    total += num
print("total:", total)
