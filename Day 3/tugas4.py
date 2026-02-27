import turtle

def draw_tree(branch_len, t):
    if branch_len > 5:
        # Gambar dahan utama
        t.forward(branch_len)
        t.right(20)
        # Rekursi untuk dahan kanan
        draw_tree(branch_len - 15, t)
        t.left(40)
        # Rekursi untuk dahan kiri
        draw_tree(branch_len - 15, t)
        t.right(20)
        t.backward(branch_len)

def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    t.speed(0) # Kecepatan maksimal
    draw_tree(75, t)
    my_win.exitonclick()

main()