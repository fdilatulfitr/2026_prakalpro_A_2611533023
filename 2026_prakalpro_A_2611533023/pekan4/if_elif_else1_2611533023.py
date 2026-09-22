umur_3023 = int(input("input umur anda: "))
sim_3023 = input("apakah anda sudah punya sim C: ")[0]

if umur_3023 >= 17 and sim_3023 == 'y':
    print("anda sudah dewasa dan boleh bawa motor")
elif umur_3023 >= 17 and sim_3023 != 'y':
    print("anda sudah dewasa tapi tidak boleh bawa motor")
else:
    print("anda belum cukup umur dan tidak boleh bawa motor")
print("program selesai")