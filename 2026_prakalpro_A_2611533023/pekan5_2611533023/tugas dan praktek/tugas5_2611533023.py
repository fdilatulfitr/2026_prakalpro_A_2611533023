# === program jam pasir kristal palindromik (pekan 5) ===
print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")
n_3023 = int(input("masukan ukuran skala jam pasir (N): "))

#-------------------------------------------------------
# 1. bingkai pembatas horizontal atas
#-------------------------------------------------------
print("#", end="")
for i_3023 in range(4 * n_3023 + 5):
    print("=", end="")
print("#")
#-------------------------------------------------------
#2. fase 1: jam pasir atas (reduksi angka menurun: N turun s.d. 1)
#-------------------------------------------------------
for baris_3023 in range (n_3023, 0, -1):
    #sisi kiri dibatasi garis tegak (|) dan satu spasi padding
    print(" ", end="")
#deret angka mundur dari baris turun ke 1
for angka_3023 in range(baris_3023, 0, -1):
    print(angka_3023, end="")
    print(" ", end="")

#poros kristal tengah
print("<*>", end="")

#deret angka maju dari 1 naik ke baris
for angka_3023 in range (1, baris_3023 + 1):
    print(" ", end="")
    print(angka_3023, end="")

#spasi penyeimbang kanan
for spasi_3023 in range (2 * (n_3023 - baris_3023)):
    print(" ", end="")

    #sisi kanan
    print(" |")

#------------------------------------------------------
#3. fase 2: poros titik pusat jam pasir (titik nol / singularity)
#------------------------------------------------------
print("|", end="")
for spasi_3023 in range(2 * n_3023 + 1):
    print(" ", end="")
print("<*>", end="")
for spasi_3023 in range(2 * n_3023 + 1):
    print(" ", end="")
print("|")

#-------------------------------------------------------
# 4. fase 3: jam pasir bawah (ekspansi angka menaik: 1 naik s.d. N) 
#-------------------------------------------------------
for baris_3023 in range(1, n_3023 + 1):
    #sisi kiri dibatsai garis tegak(|) dan satu spasi padding 
    print("| ", end="")

    #spasi penyeimbang kiri: 2 * (N - baris)
    for spasi_3023 in range (2 * (n_3023 - baris_3023)):
        print(" ", end="")

    #deret angka mundur dari baris turun ke 1
    for angka_3023 in range(baris_3023, 0, -1):
        print(angka_3023, end="")
        print(" ", end="")

    #poros kristal tengah
    print("<*>", end="")

    #deret angka maju dari 1 naik ke baris
    for angka_3023 in range(1, baris_3023 + 1):
        print(" ", end="")
        print(angka_3023, end="")

    #spasi penyeimbang kanan
    for spasi_3023 in range(2 * (n_3023 - baris_3023)):
        print(" ", end="")

    # sisi kanan
    print(" |")

#----------------------------------------------------------
# 5. bingkai pembatas horizontal bawah
#----------------------------------------------------------
print("#", end="")
for i_3023 in range(4 * n_3023 + 5):
    print("=", end="")
print("#")