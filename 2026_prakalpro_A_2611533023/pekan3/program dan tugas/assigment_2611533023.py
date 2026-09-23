angka1_3023 = int(input("input angka-1_3023: "))
angka2_3023 = int(input("input angka-2_3023: "))

print("\nNilai awal angka1_3023 =", angka2_3023)
print("nilai angka2_3023 =", angka2_3023)

# Assignment biasa
hasil_3023 = angka1_3023
print("\nAssignment biasa (=)")
print("Hasil =", hasil_3023)

#Assignment penambahan
hasil_3023 = angka1_3023
hasil_3023+= angka2_3023
print("\nAssignment penambahan (+=)")
print("Hasil =", hasil_3023)

#Assignment pengurangan
hasil_3023 = angka1_3023
hasil_3023 -= angka2_3023
print("\nAssignment pengurangan (-=)")
print("Hasil =", hasil_3023)

#Assignment perkalian
hasil_3023 = angka1_3023
hasil_3023 *= angka2_3023
print("\nAssigment perkalian (*=)")
print("Hasil =", hasil_3023)

#assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_3023 != 0:
    hasil_3023 = angka1_3023
    hasil_3023 /= angka2_3023
    print("\nAssignment pembagian bulat (//=)")
    print("hasil_3023 =", hasil_3023)
    #Operator tambahan
    hasil_3023 = angka1_3023
    hasil_3023 //= angka2_3023
    print("\nAssignment pembagian bulat (//=)")
    print("hasil_3023 =", hasil_3023)
    hasil_3023 = angka1_3023
    hasil_3023 %= angka2_3023
    print("\nAssignment sisa bagi (%=)")
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka keduka tidak boleh bernilai 0.")

#Operator tambahan: assignment perpangkatan
hasil_3023 = angka1_3023
hasil_3023 **= angka2_3023
print("\nAssignment perpangkatan (**=)")
print("hasil_3023 =", hasil_3023)
