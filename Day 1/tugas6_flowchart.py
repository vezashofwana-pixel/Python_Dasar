#Inisialisasi variabel untuk memulai perulangan
ulang = "Ya"

while ulang == "Ya":
    #1. Input nilai siswa
    nilai_siswa = float(input("Masukkan nilai siswa: "))

    #2. Cek apakah nilai >= 75
    if nilai_siswa >= 75:
        print("Tuntas")
        # Jika tuntas, kita hentikan perulangan
        break
    else:
        #3. Jika tidak >= 75, tanya apakah mau mengulang
        ulang = input("Apakah ingin mengulang? (Ya/Tidak): ")

        #4. Cek jawaban mengulang
        if ulang == "Ya":
            #Jika Ya, program akan kembali ke atas (input nilai)
            continue
        else:
            #5. Jika Tidak, cetak Tidak Tuntas dan selesai
            print("Tidak Tuntas")
            break

    print("--- Program Selesai ---")