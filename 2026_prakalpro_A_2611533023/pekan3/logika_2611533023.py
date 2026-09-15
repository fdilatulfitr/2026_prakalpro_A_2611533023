a1_3023 = input("Input nilai boolean-1 (true/false): ").strip().lower() == "true"
a2_3023 = input("input nilai boolean-2 (true/false): ").strip().lower()

print("\nA1 =", a1_3023)
print("A2 =", a2_3023)

# Konjungsi: bernilai true jika keduanya true
hasil_3023 = a1_3023 and a2_3023
print("\nKonjungsi (AND)")
print("A1_3023 and A2 =", hasil_3023)

#disjungsi: bernilai true jika salah satunya true
hasil_3023 =  a1_3023 or a2_3023
print("\nDisjungsi (or)")
print("A1_3023 or A2_3023 =", hasil_3023)

#negasi A1_3023: membalik nilai A1_3023
hasil_3023 = not a1_3023
print("\nNegasi A1_3023 (NOT)")
print("not A1_3023 =", hasil_3023)

#Negasi A2_3023: membalik nilai A2_3023
hasil_3023 = not a2_3023
print("\nNegasi A2_3023 (NOT)")
print("not A2 =", hasil_3023)

#XOR: bernilai true jika kedua nilai berbeda
hasil_3023 = a1_3023 != a2_3023
print("\nDisjungsi Eksklusif (XOR)")
print("A1_3023 XOR A2_3023", hasil_3023)