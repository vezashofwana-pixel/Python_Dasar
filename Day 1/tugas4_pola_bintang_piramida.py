baris = int(input("Masukkan jumlah baris: "))
for i in range(1, baris + 1):
    # Print spasi agar rata tengah
    print(" " * (baris - i), end="")
    # Print bintang
    print("* " * i)