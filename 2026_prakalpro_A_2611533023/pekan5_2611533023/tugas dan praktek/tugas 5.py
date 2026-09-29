# === PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===

print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")
n_3023 = int(input("Masukkan ukuran skala jam pasir (N): "))

# --------------------------------------------------
# 1. Bingkai Pembatas Horizontal Atas
# --------------------------------------------------
print("#", end="")
for i_3023 in range(4 * n_3023 + 5):
    print("=", end="")
print("#")

# --------------------------------------------------
# 2. Fase 1: Jam Pasir Atas (Reduksi Angka Menurun: N turun s.d. 1)
# --------------------------------------------------
for baris_3023 in range(n_3023, 0, -1):
    print("| ", end="")
    
    # Spasi penyeimbang kiri
    for spasi_3023 in range(2 * (n_3023 - baris_3023)):
        print(" ", end="")
        
    # Deret angka mundur dari baris turun ke 1
    for angka_3023 in range(baris_3023, 0, -1):
        print(angka_3023, end="")
        print(" ", end="")
            
    # Poros kristal tengah
    print("<*>", end="")
    
    # Deret angka maju dari 1 naik ke baris
    for angka_3023 in range(1, baris_3023 + 1):
        print(" ", end="")
        print(angka_3023, end="")
        
    # Spasi penyeimbang kanan
    for spasi_3023 in range(2 * (n_3023 - baris_3023)):
        print(" ", end="")
        
    print(" |")

# --------------------------------------------------
# 3. Fase 2: Poros Titik Pusat Jam Pasir (Titik Nol / Singularity)
# --------------------------------------------------
print("|", end="")
for spasi_3023 in range(2 * n_3023 + 1):
    print(" ", end="")
print("<*>", end="")
for spasi_3023 in range(2 * n_3023 + 1):
    print(" ", end="")
print("|")

# --------------------------------------------------
# 4. Fase 3: Jam Pasir Bawah (Ekspansi Angka Menaik: 1 naik s.d. N)
# --------------------------------------------------
for baris_3023 in range(1, n_3023 + 1):
    print("| ", end="")
    
    # Spasi penyeimbang kiri
    for spasi_3023 in range(2 * (n_3023 - baris_3023)):
        print(" ", end="")
        
    # Deret angka mundur dari baris turun ke 1
    for angka_3023 in range(baris_3023, 0, -1):
        print(angka_3023, end="")
        print(" ", end="")
            
    # Poros kristal tengah
    print("<*>", end="")
    
    # Deret angka maju dari 1 naik ke baris
    for angka_3023 in range(1, baris_3023 + 1):
        print(" ", end="")
        print(angka_3023, end="")
        
    # Spasi penyeimbang kanan
    for spasi_3023 in range(2 * (n_3023 - baris_3023)):
        print(" ", end="")
        
    print(" |")

# --------------------------------------------------
# 5. Bingkai Pembatas Horizontal Bawah
# --------------------------------------------------
print("#", end="")
for i_3023 in range(4 * n_3023 + 5):
    print("=", end="")
print("#")