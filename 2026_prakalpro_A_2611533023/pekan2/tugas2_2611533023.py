print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")
nama_3023 = input('Masukan Nama Mahasiswa:')
jenis_kelamin_3023 = input('Jenis Kelamin (L/P):')
umur_3023 = int(input('Masukan Umur:'))
skor_tes_awal_3023 = float(input('Masukan Skor Tes Awal:'))
alamat_3023 = """
    Kampus Unand
    Kecamatan Pauh
    Kota Padang
"""
id_token_sinyal_3023 = 100+3j
print("=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa : ", nama_3023, " | tipe:", type(nama_3023))
print("Jenis Kelamin : ", jenis_kelamin_3023, " | tipe:", type(jenis_kelamin_3023))
print("alamat domisili : ", alamat_3023, "|tipe:", type(alamat_3023))
print("Umur :",umur_3023, "Tahun|tipe:", type(umur_3023))
print("skor tes awal :", skor_tes_awal_3023, "|tipe:", type(skor_tes_awal_3023))
print("id token awal :", id_token_sinyal_3023, "|tipe:", type(id_token_sinyal_3023))
print("=== STATUS KELULUSAN ===")
batas_3023 = 75.0
if skor_tes_awal_3023 >= batas_3023:
    hasil_3023 = True
else:
    hasil_3023 = False
print("Batas Minimum Nilai:", batas_3023 )
print("Apakah Dinyatakan Lulus?:", hasil_3023, "|tipe:", type(hasil_3023))