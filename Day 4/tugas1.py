import tkinter as tk
from tkinter import ttk

def hitung_total():
    try:
        # Mengambil nilai dari input dan menghitung total
        harga = float(entry_harga.get())
        kuantitas = float(entry_kuantitas.get())
        total = harga * kuantitas
        # Memperbarui label total dengan format dua angka di belakang koma
        label_total_hasil.config(text=f"Total: Rp.{total:,.2f}")
    except ValueError:
        # Pesan jika input bukan angka
        label_total_hasil.config(text="Input tidak valid!")

# Inisialisasi jendela utama
root = tk.Tk()
root.title("Program Kasir")
root.geometry("300x250")

# Label dan Entry untuk Harga
label_harga = tk.Label(root, text="Harga:")
label_harga.pack(pady=(20, 0))
entry_harga = tk.Entry(root, justify='center')
entry_harga.pack(pady=5)

# Label dan Entry untuk Kuantitas
label_kuantitas = tk.Label(root, text="Kuantitas:")
label_kuantitas.pack(pady=5)
entry_kuantitas = tk.Entry(root, justify='center')
entry_kuantitas.pack(pady=5)

# Tombol Hitung Total
btn_hitung = tk.Button(root, text="Hitung Total", command=hitung_total)
btn_hitung.pack(pady=10)

# Label untuk menampilkan hasil Total
label_total_hasil = tk.Label(root, text="Total: Rp.0.00")
label_total_hasil.pack(pady=5)

# Menjalankan aplikasi
root.mainloop()