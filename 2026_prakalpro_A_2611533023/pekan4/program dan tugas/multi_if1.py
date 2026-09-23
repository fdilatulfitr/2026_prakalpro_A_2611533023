umur_3023 = int(input("input umur anda: "))
sim_3023 = input("apakah anda sudah punya sim C (y/t): ")[0]

if umur_3023 >= 17 and sim_3023 == 'y':
    print("anda sudah dewasa dan boleh bawa motor")
if umur_3023 >= 17 and sim_3023 != 'y':
    print("anda sudah dewasa tetapi tidak boleh bawa motor")
if umur_3023 < 17 and sim_3023 != 'y':
    print("anda belum cukup umur bawa motor")
if umur_3023 < 17 and sim_3023 == 'y':
    print("anda belum cukup umur punya SIM")