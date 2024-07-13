import turtle
def hexagon(side_length):
    for _ in range(6):
        turtle.forward(side_length)
        turtle.right(60)
def hexagons(rows, columns,side_length):
    turtle.speed(0)
    turtle.penup() 
    start_x = -columns*side_length*0.75
    start_y = rows*side_length*(3**0.5)/2
    for col in range(columns):
        max_rows = rows if col % 2 == 0 else rows - 1
        for row in range(max_rows):
            x = start_x+col*1.5*side_length
            y = start_y - row*(side_length*(3**0.5))-(0.5*side_length*(3**0.5) if col % 2 == 1 else 0)
            turtle.goto(x, y)
            turtle.pendown()
            hexagon(side_length)
            turtle.penup()
    turtle.hideturtle()
    turtle.done()
turtle.clearscreen()
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
side_length = 30  
hexagons(rows, columns, side_length)
