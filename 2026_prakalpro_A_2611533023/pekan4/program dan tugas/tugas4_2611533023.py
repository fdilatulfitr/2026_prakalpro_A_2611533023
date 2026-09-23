print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")
# input data pengunjung
nama_3023 = input("Masukkan nama pengunjung: ")
umur_3023 = int(input("Masukkan umur pengunjung: "))
sim_input_3023 = input("Apakah pengunjung sudah punya SIM C? (ya/tidak): ")
sim_3023 = sim_input_3023[0] if sim_input_3023 else 't'

#tampilan data pengunjung
print("\nPilihan paket wahana (1-5):")
print("1. safari rimba          (Rp 50,000)")
print("2. arung jeram           (Rp 75,000)")
print("3. motor atv ekstrim     (Rp 120,000)")
print("4. roller coaster kilat  (Rp 100,000)")
print("5. wwahana all-access VIP(Rp 220,000)")

paket_3023 = int(input("masukan nomor paket (1-5)   : "))
jumlah_tiket_3023 = int(input("masukan jumlah tiket yang dibeli: :"))

#validasi kelogisan tiket menggunakan if
if jumlah_tiket_3023 <= 0:
    print("Jumlah tiket tidak valid. Harap masukkan jumlah tiket yang lebih besar dari 0.")
is_member_3023 = input("apakah member? (y/t) : ").strip().lower()
kode_promo_valid_3023 = input("apakah kode promo valid? (y/t) : ").strip().lower()
#pemilihan wahana dengan match-case

match paket_3023:
    case 1:
        nama_paket_3023 = "safari rimba"
        harga_satuan_3023 = 50000
    case 2:
        nama_paket_3023 = "arung jeram"
        harga_satuan_3023 = 75000
    case 3:
        nama_paket_3023 = "motor atv ekstrim"
        harga_satuan_3023 = 120000
    case 4:
        nama_paket_3023 = "roller coaster kilat"
        harga_satuan_3023 = 100000
    case 5:
        nama_paket_3023 = "wwahana all-access VIP"
        harga_satuan_3023 = 220000
    case _:
        print("Paket wahana tidak valid.")
        exit()

# validasi izin kendali wahana menggunakan if - elif - else
print("\n--- KELAYAKAN PENGENDARA WAHANA ---")
if paket_3023 == 3:
    if umur_3023 >= 17 and sim_3023 == 'y':
        print("status akses: anda sudah dewasa dan boleh mengendarai ATV sendiri")
    elif umur_3023 >= 17 and sim_3023 != 'y':
        print("status akses: anda sudah dewasa tapi tidak boleh bawa motor ATV sendiri (harus didampingi instruktur)")
    elif umur_3023 < 17 and sim_3023 == 'y':
        print("status akses: identitas tidak valid: belum cukup umur untuk memiliki SIM")
    else:
        print("status akses: anda belum cukup umur untuk mengendarai ATV")
else:
    if umur_3023 >= 10:
        print("status akses: pengunjung memenuhi syarat umur minimal wahana")
    else:
        print("status akses: mengunjung belum memiliki syarat umur minimal wahana (min. 10 tahun)")

#kasih diskon menggunakan multi if
subtotal_3023 = harga_satuan_3023 * jumlah_tiket_3023
total_diskon_persen_3023 = 0

if subtotal_3023 >= 200000:
    total_diskon_persen_3023 += 10

if is_member_3023 in ['y', 'ya']:
    total_diskon_persen_3023 += 5

if kode_promo_valid_3023 in ['y', 'ya']:
    total_diskon_persen_3023 += 15

if jumlah_tiket_3023 >= 5:
    total_diskon_persen_3023 += 5

#evaluasi kelulusan dan perhitungan akhir
nominal_diskon_3023 = subtotal_3023 * (total_diskon_persen_3023 / 100)
total_bayar_3023 = subtotal_3023 - nominal_diskon_3023
print("\n--- RINCIAN PEMBAYARAN ---")
print(f"subtotal belanja : Rp {subtotal_3023:,.0f}")
print(f"total diskon     : {total_diskon_persen_3023}% (Rp {nominal_diskon_3023:,.0f})")
print(f"total bayar      : Rp {total_bayar_3023:,.0f}")

#evaluasi bonus
if total_bayar_3023 > 300000:
    print("catatan layanan: selamat! anda berhak mendapatkan souvenir gratis")
else:
    print("catatan layanan: terimakasih telah berkunjung")

print("program selesai")