# input dari user
total_belanja_3023 = float(input("masukan total belanja (Rp): "))

#input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_3023 = input("apakah anda member? (y/t): ").strip().lower()
is_member_3023 = input_member_3023 in ["y", "ya"]

#input status kode promo (mengecek apakah user mengetik 'y' ayau 'ya')
input_promo_3023 = input("apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_3023 = input_promo_3023 in ["y", "ya"]
total_diskon_persen_3023 = 0

#multi-if terpisah: setia kondisi diperiksa secara independen
#diskon bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus

if total_belanja_3023 > 1000000:
    total_diskon_persen_3023 += 10 #diskon belanja besar

if is_member_3023:
    total_diskon_persen_3023 +=5 #diskon member

if kode_promo_valid_3023:
    total_diskon_persen_3023 +=15 #diskon voucher

#menghitung nominal diskon dan total bayar
nominal_diskon_3023 = total_belanja_3023 * (total_diskon_persen_3023 / 100)
total_bayar_3023 = total_belanja_3023 - nominal_diskon_3023

#output hasil
print("\n--- rincian pembeyaran ---")
print(f"total diskon : {total_diskon_persen_3023}% (rp {nominal_diskon_3023:,.0f})")
print(f"total bayar :rp {total_bayar_3023:,.0f}")

print(f"total diskon yang anda dapatkan: {total_diskon_persen_3023}%")
# output: total diskon yang anda dapatkan: 30% jika belanja > 1 juta,member,dan kode promo valid