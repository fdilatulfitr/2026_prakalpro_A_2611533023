tinggi_3023 = int(input("masukan tinggi pola (bilangan genap, misal 10): "))

if tinggi_3023 % 2 != 0:
    print("tinggi harus bilangan genap!")
else: 
    a = tinggi_3023
    c = a
    lebar_3023 = (2 * tinggi_3023) - 2

    for i in range(1, tinggi_3023 + 1):
        b = c + 1

        for j in range(1, lebar_3023 + 1):

            #baris atas dan bawah
            if i == 1 or i == tinggi_3023:
                if j == 1 or j == lebar_3023:
                    print("#", end="")
                else:
                    print("=", end="")
            #baris isi
            else:
                if j == 1 or j == lebar_3023:
                    print("|", end="")
                else:
                    if j == c:
                        print("<", end="")
                    elif j == b:
                        print(">", end="")
                    elif j == (lebar_3023 - c):
                        print("<", end="")
                    elif j == (lebar_3023 - c + 1):
                        print(">", end="")
                    elif j > b and j < (lebar_3023 - c):
                        print(".", end="")
                    else:
                        print(" ", end="")
        print()
        # logika asli java
        a -= 2
        if a <= 0:
            c = (-a) + 2
        else:
            c = a
