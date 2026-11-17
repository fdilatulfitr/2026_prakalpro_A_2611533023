# Nama: Fadilatul fitri
# Nim: 2611533023
# Question bonus

kalimat = input("Kalimat: ")
bersih = kalimat.replace(" ", "").lower()

if bersih == bersih[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")