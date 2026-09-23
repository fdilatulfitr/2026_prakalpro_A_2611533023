print("\n===================================")
print("3. OPERATOR BITWISE")
print("===================================")

angka1_3023 = int(input("masukan angka bitwise-1:"))
angka2_3023 = int(input("masukan angka bitwise-2:"))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1_3023 =", angka1_3023, "| biner =", bin(angka1_3023))
print("angka2_3023 =", angka2_3023, "| biner =", bin(angka2_3023))

# Bitwise AND
hasil_3023 = angka1_3023 & angka2_3023
print("\nBitwise AND (&)")
print(angka1_3023, "&", angka2_3023, "=", hasil_3023)
print("biner hasil_3023 =", bin(hasil_3023))
print("biner hasil_3023 (8 bit) =", format(hasil_3023, "08b"))

#Bitwise OR
hasil_3023 = angka1_3023 | angka2_3023
print("\nBitwise OR (|)")
print(angka1_3023, "|", angka2_3023, "=", hasil_3023)
print("biner hasil =", bin(hasil_3023))
print("biner hasil (8 bit) =", format(hasil_3023, "08b"))

#Bitwise XOR
hasil_3023 = ~angka1_3023 ^ angka2_3023
print("\nBitwise XOR (^)")
print(angka1_3023, "^", angka2_3023, "=", hasil_3023)
print("Biner hasil =", bin(hasil_3023))
print("Biner hasil (8 bit) =", format(hasil_3023, "08b"))

#Bitwise NOT
hasil_3023 = ~angka1_3023
print("\nBitwise NOT (~)")
print("~", angka1_3023, "=", hasil_3023)
print("biner hasil =", bin (hasil_3023))
print("biner hasil (8 bit) =", format(hasil_3023, "08b"))

#bitwise gaser kiri
jumlah_geser_3023 = int(input("\nMasukan jumlah pergeseran bit: "))

hasil_3023 = angka1_3023 << jumlah_geser_3023
print("\nBitwise geser kiri (<<)")
print(angka1_3023, "<<", jumlah_geser_3023, "=", hasil_3023)
print("biner hasil =", bin(hasil_3023))
print("biner hasil (8 bit) =", format(hasil_3023, "08b"))

#Bitwise geser kanan
hasil_3023 = angka1_3023 >> jumlah_geser_3023
print("\nBitwise geser kanan (>>)")
print(angka1_3023, ">>", jumlah_geser_3023, "=", hasil_3023)
print("biner hasil =", bin(hasil_3023))
print("biner hasil (8 bit) =", format(hasil_3023, "08b"))