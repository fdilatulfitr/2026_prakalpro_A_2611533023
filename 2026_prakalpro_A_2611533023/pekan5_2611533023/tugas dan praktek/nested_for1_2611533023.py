batas_3023 = int(input("masukan nilai batas: "))
for line in range(1, batas_3023 + 1):
    for j in range(1, (-1 * line + batas_3023) + 1):
        print(".", end="")
    print(line)