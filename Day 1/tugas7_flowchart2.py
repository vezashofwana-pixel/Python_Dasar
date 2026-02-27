#1. Input Nama dan Gaji Pokok
nama = input("Masukkan nama: ")
gaji_pokok = float(input("Masukkan gaji Pokok: "))

#2. proses Perhitungan
#Tunjangan = 20% dari Gaji Pokok
tunjangan = 0.20 * gaji_pokok

#Pajak = 15% dari (Gaji Pokok + Tunjangan)
pajak = 0.15 * (gaji_pokok + tunjangan)

#Gaji Bersih = Gaji Pokok + Tunjangan - Pajak
gaji_bersih = gaji_pokok + tunjangan - pajak

#3. Output Nama, Gaji Pokok, dan Gaji Bersih
print("--- Slip Gaji ---")
print(f"Nama          : {nama}")
print(f"Gaji Pokok    : Rp{gaji_pokok:,.0f}")
print(f"Gaji Bersih   : Rp{gaji_bersih:,.0f}")
