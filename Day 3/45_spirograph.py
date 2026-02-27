import turtle as tt

# curve as 10(relative)
tt.bgcolor('black')
tt.pensize(2)
tt.speed(10)

# Iterate six times in total
for i in range(6):

    # choose your color combination
    for color in ('red', 'magenta', 'blue',
                  'cyan', 'green', 'white',
                  'yellow'):
        tt.color(color)

        # Draw a circle at chosen size, 100 here
        tt.circle(100)

        # Move 10 pixels left to draw another circle
        tt.left(10)

# Hide the cursor(or turtle) wich drew the circle
tt.hideturtle()