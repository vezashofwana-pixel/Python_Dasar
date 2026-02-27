import tkinter as tk
from tkinter import messagebox

def simpan_data():
    messagebox.showinfo("Sukses", "Data berhasil disimpan!")

root = tk.Tk()
root.title("Program Data Siswa")
root.geometry("450x650")
root.configure(bg="#add8e6") # Warna biru muda

# Header
header = tk.Label(root, text="DATA SISWA BARU", font=("Arial", 16, "bold"), bg="#add8e6")
header.pack(pady=20)

# Container untuk form agar rapi
form_frame = tk.Frame(root, bg="#add8e6")
form_frame.pack(padx=20, fill="x")

fields = [
    "Nama Lengkap", "Tanggal Lahir", "Asal Sekolah", 
    "NISN", "Nama Ayah", "Nama Ibu", "Nomor Telepon / HP"
]

entries = {}

for field in fields:
    lbl = tk.Label(form_frame, text=field, bg="#add8e6", anchor="w")
    lbl.pack(fill="x")
    ent = tk.Entry(form_frame)
    ent.pack(fill="x", pady=(0, 10))
    entries[field] = ent

# Khusus Alamat (Text Box)
lbl_alamat = tk.Label(form_frame, text="Alamat", bg="#add8e6", anchor="w")
lbl_alamat.pack(fill="x")
txt_alamat = tk.Text(form_frame, height=5)
txt_alamat.pack(fill="x", pady=(0, 20))

# Tombol
btn_frame = tk.Frame(root, bg="#add8e6")
btn_frame.pack(side="bottom", pady=20)

btn_hapus = tk.Button(btn_frame, text="Hapus", bg="#e67e22", fg="white", width=10)
btn_hapus.pack(side="left", padx=10)

btn_simpan = tk.Button(btn_frame, text="Simpan", bg="#e67e22", fg="white", width=10, command=simpan_data)
btn_simpan.pack(side="left", padx=10)

root.mainloop()