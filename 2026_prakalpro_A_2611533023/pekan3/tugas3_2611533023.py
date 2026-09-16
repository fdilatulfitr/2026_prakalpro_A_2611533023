print("=== SISTEM TRANSAKSI TOKO ===")
nama_pelanggan_3023 = input('masukan nama pelanggan:')
status_pelanggan_3023 = input('masukan status pelanggan (member/non member):')
total_belanja_3023 = int (input('masukan total belanja:'))
jumlah_barang_3023 = int (input('masukan jumlah barang:'))
kode_promo_3023 = input('masukan kode promo:')

print("=== DATA TRANSAKSI ===")
print("Nama Pelanggan :", nama_pelanggan_3023)
print("Status Pelanggan :", status_pelanggan_3023)
print("Total Belanja :", total_belanja_3023)
print("Jumlah Barang :", jumlah_barang_3023)
print("Kode Promo :", kode_promo_3023)

print("=== HASIL VALIDASI ===")
hasil_total_belanja_3023 = total_belanja_3023 >= 200000
print("belanja>=Rp200000", hasil_total_belanja_3023)
hasil_jumlah_barang_3023 = jumlah_barang_3023 >= 3
print("jumlah barang>=3", hasil_jumlah_barang_3023)
hasil_status_member_3023 = status_pelanggan_3023.lower () == "member"
print("status pelanggan", hasil_status_member_3023)
hasil_kode_promo_3023 = kode_promo_3023 != ""
print("kode promo tersedia", hasil_kode_promo_3023)
hasil_mendapatkan_diskon_3023 = (
    hasil_total_belanja_3023
    or hasil_jumlah_barang_3023
    or hasil_status_member_3023
)
print("mendapatkan diskon", hasil_mendapatkan_diskon_3023)
hasil_mendapatkan_promo_3023 = hasil_kode_promo_3023
print("mendapatkan promo", hasil_mendapatkan_promo_3023)

print("=== HASIL PERHITUNGAN ===")
# jika diskon diberikan kalau ' hasil_memberikan_diskon_3023'bernilai True (misal 10%)
if hasil_mendapatkan_diskon_3023:
    diskon_3023 = int (total_belanja_3023 * 0.1) # 10% dari total belanja
else:
    diskon_3023 = 0
print("Diskon               : Rp" + str(diskon_3023))
total_pembayaran_3023 = total_belanja_3023 - diskon_3023
print("total pembayaran     : Rp" + str(total_pembayaran_3023))
rata_rata_harga_3023 = int (total_pembayaran_3023 / jumlah_barang_3023)
print("rata rata harga barang: Rp" + str(rata_rata_harga_3023))

print("=== HAK AKSES PELANGGAN ===")

print("kode hak akses:",)
member_acces_3023 = hasil_status_member_3023
print("member acces:", member_acces_3023)
promo_acces_3023 = hasil_mendapatkan_promo_3023
print("promo acces:", promo_acces_3023)

print("Free Shipping Access:",)

print("=== OPERASI BITWISE===")
print("=== KODE STATUS TRANSAKSI ===")
#nilai bit dalam bentuk biner
bit_member_3023 = 0b0001
bit_belanja_3023 = 0b0010
bit_barang_3023 = 0b0100
bit_promo_3023 = 0b1000
#penggabungan dengan operator OR (|)
kode_status_3023 = bit_member_3023|bit_belanja_3023|bit_barang_3023|bit_promo_3023
bin_status_str_3023 = bin(kode_status_3023)[2:]

print("0001 | 0010 | 0100 | 1000")
print("kode biner   :",bin_status_str_3023)
print("kode desimal:", kode_status_3023)

print("=== PEMERIKSAAN STATUS ===")
print("cek member")

#Bitwise AND (&)
cek_member_3023 = kode_status_3023 & 0b0001
bin_cek_member_str_3023 = bin(cek_member_3023)[2:]
print(bin_status_str_3023, "& 0001")
print("hasil biner  :", bin_cek_member_str_3023)
print("hasil desimal:", cek_member_3023)

print("cek promo")
cek_promo_3023 = kode_status_3023 & 0b1000
bin_cek_promo_str_303 = bin(cek_promo_3023)

print("1111 & 1000")
print("hasil biner  : 1000")
print("hasil desimal:", cek_promo_3023)

print("=== PERBANDINGAN STATUS ===")
kode_referensi_3023 = 0b1011

#Operator Bitwise XOR (^)
hasil_xor_3023 = kode_status_3023 ^ kode_referensi_3023

print("Kode Transaksi : 1111")
print("Kode Referensi : 1011")
print("1111 ^ 1011")
print("Hasil Biner  : 0100")
print("hasil desimal:", hasil_xor_3023)

print("=== SHIFT ===")
hasil_shift_3023 = kode_status_3023 << 1

print("1111 << 1")
print("Hasil Biner : 11110")
print("Hasil Desimal :", hasil_shift_3023)

print("=== SELESAI ===")