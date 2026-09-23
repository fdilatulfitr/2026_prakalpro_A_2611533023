print("==================================")
print("1. OPERATOR KEANGGOTAAN")
print("==================================")

#input beberapa dsata yang dipisahkan dengan koma
input_data_3023 = input("masukan beberapa angka, pisahkan dengan koma: ")

# mengubah input menjadi list integer
data_3023 = [int(angka.strip()) for angka in input_data_3023.split(",")]

nilai_dicari_3023 = (input("masukan angka yang ingin dicari: "))

#Operator in
hasil_3023 = nilai_dicari_3023 in data_3023
print("\nOperator keanggotaan IN")
print(nilai_dicari_3023, "not in", data_3023, "=", hasil_3023)

print("\n===================================")
print("2. OPERATOR IDENTITAS")
print("=====================================")

# objek1 menggunakan list dari input pengguna
objek1_3023 = data_3023

# objek2 merujuk pada objek yang sama dengan objek1
objek2_3023 = objek1_3023

#objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_3023 = data_3023.copy()

print("objek1_3023 =", objek1_3023)
print("objek2_3023 =", objek2_3023)
print("objek3_3023 =", objek3_3023)

#Operator is
hasil_3023 = objek1_3023 is objek2_3023
print("\nOperator identitas IS")
print("objek2_3023 =", hasil_3023)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1_3023 is objek3_3023 =", objek1_3023 is objek3_3023)
print("objek1_3023 == objek3 =", objek1_3023 == objek3_3023)
