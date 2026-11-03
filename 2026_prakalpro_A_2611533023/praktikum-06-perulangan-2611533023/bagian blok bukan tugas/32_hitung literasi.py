#kode a berapa kali tanda bintang ditampilkan
for row in range(1, 4):
    for column in range(1, 6):
        print("*", end="")
    print()

#kode b berapa kali tanda bintang ditampilkan
for row in range(1, 5):
    for column in range (row):
        print("*", end="")
    print()

#kode c berapa nilai yang ditampilkan
count = 0

for first in range(2):
    for second in range(3):
        count += 1

    count += 10

print(count)

    