import math

#1.Tabung
r = float(input("Jari-jari tabung: "))
t_tabung = float(input("Tinggi tabung: "))
volume_tabung = math.pi * r**2 * t_tabung
print(f"Volume Tabung: {volume_tabung:.2f}")

#2.Balok
p = float(input("Panjang balok: "))
l = float(input("Lebar balok: "))
t_balok = float(input("Tinggi balok: "))
print(f"Volume Balok: {p * l * t_balok}")