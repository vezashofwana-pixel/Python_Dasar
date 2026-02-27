import turtle
import math

# Konfigurasi Layar
screen = turtle.Screen()
screen.setup(700, 700)
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0) # Kecepatan maksimal

def draw_filled_circle(radius, color, x=0, y=0):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_text_curved(text, radius, start_angle, step, font_size):
    t.penup()
    angle = start_angle
    for char in text:
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        t.goto(x, y)
        t.setheading(angle - 90 if start_angle > 0 else angle + 90)
        t.forward(10 if start_angle > 0 else -20) # Penyesuaian posisi huruf
        t.pencolor("black")
        t.write(char, align="center", font=("Arial", font_size, "bold"))
        angle += step

def draw_star(x, y, size):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.color("black")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

# 1. Lingkaran Putih Luar (Border)
draw_filled_circle(260, "black")
draw_filled_circle(255, "white")

# 2. Lingkaran Biru Tengah
draw_filled_circle(200, "#1a316c")

# 3. Garis Putih tipis di dalam Biru
t.penup()
t.goto(0, -190)
t.pendown()
t.color("white")
t.width(2)
t.circle(190)
t.width(1)

# 4. Teks Melingkar
draw_text_curved("SEKOLAH MENENGAH KEJURUAN", 225, 160, -8.5, 14)
draw_text_curved("PRESTASI PRIMA", 225, -135, 10, 18)

# 5. Bintang Samping
draw_star(-235, 10, 20)
draw_star(215, 10, 20)

# 6. Menggambar Ikon Tangan (Sederhana)
t.penup()
t.goto(-40, -80)
t.color("white")
t.begin_fill()
# Lengan bawah
t.setheading(90)
t.forward(100)
# Jari-jari
t.right(90)
t.forward(80)
t.right(90)
t.forward(100)
t.right(90)
t.forward(80)
t.end_fill()

# Bagian Merah Tangan
t.penup()
t.goto(-35, -75)
t.color("red")
t.begin_fill()
t.setheading(90)
t.forward(120) # Jari telunjuk lebih tinggi
t.right(90)
t.forward(25)
t.right(90)
t.forward(40)
t.left(90)
t.forward(45) # Jari lainnya
t.right(90)
t.forward(80)
t.right(90)
t.forward(70)
t.end_fill()

# Lingkaran kecil di atas jari telunjuk
t.penup()
t.goto(-22, 60)
t.pendown()
t.color("black")
t.width(5)
t.circle(25)

t.hideturtle()
turtle.done()