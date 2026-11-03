def main ():
    # varian digit nim akhir: 3
    PASS_SCORE = 60

    #input jumlah siswa
    n_students = int(input("number of students: "))
    if n_students < 1:
        print("invalid student count!")
        return

    #inisialisasi akumulator dan variabel
    total_score = 0
    passed_count = 0
    highest_score = -1

    for i in range(1, n_students + 1):
        print(f"student {i}")
        score = int(input("enter score: "))

        #validasi nilai (1-100)
        while score < 0 or score > 100:
            print("Invalid score!")
            score = int(input("enter score: "))

        #akumulasi total nilai
        total_score += score

        #hitung mahasiswa lulus (score >= 60)
        if score >= PASS_SCORE:
            passed_count += 1

        #cek nilai tertinggi
        if score > highest_score:
            highest_score = score

    #output

    #tampilkan total dan rata rata
    average_score = round(total_score / n_students, 2)
    print("Total score:", total_score)
    print("Average score:", average_score)

    #tampilkan jumlah mahasiswa lulus
    print("Passed:", passed_count)

    #tampilkan nilai tertinggi
    print("Highest score:", highest_score)

if __name__ == "__main__":
    main()