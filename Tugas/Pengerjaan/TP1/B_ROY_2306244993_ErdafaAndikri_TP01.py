""" Nama: Erdafa Andikri
    NPM: 2306244993
    Kode Asdos: ROY

    Program ini dibuat untuk memenuhi tugas TP 1.

    Program dimulai dengan meminta input user berupa spesifikasi tower yang user inginkan.
    Program ini akan mengvalidasi input user sesuai kriteria TP 1.
    
    Setelah user input, maka program akan membuat tower sesuai spesifikasi user.
    Turtle akan membuat tower-tower yang center di layar.
    Turtle membuat keliling tower, lapisan tower horizontal, lapisan tower vertikal, atap tower, dan jamur.
    Turtle akan membuat tower-tower sebanyak yang diinginkan user, ditambahkan tinggi tower setiap iterasi, dan jarak antar tower.
    Turtle akan menghitung dan menulis total brick yang digunakan untuk membuat tower-tower.
"""

from turtle import *
from tkinter import messagebox as tk
screen = Screen()

# Meminta input dari user
screen.title("Super Mario Tower Builder")

valid = False
while valid == False:
    amount_tower = screen.numinput("Tower to Build", "Enter the amount of tower you want to build (integer)", minval=1)
    if amount_tower != int(amount_tower):
        tk.showerror("Error", "Tower amount must be an integer")
    else:
        valid = True
valid = False

# Declare variable jika user input 1 tower
distance_between_towers = 0
tower_layer_differences = 0


# Meminta input dari user jika user input lebih dari 1 tower
if amount_tower > 1:
    while valid == False:
        distance_between_towers = screen.numinput("Distance between Towers", "Enter the distance between towers in bricks (integer)", minval=2, maxval=5)
        if distance_between_towers != int(distance_between_towers):
            tk.showerror("Error", "Distance between towers must be an integer")
        else:
            valid = True
    valid = False
    while valid ==False:
        tower_layer_differences = screen.numinput("Tower Layer Differences", "Enter the number of layer differences between each tower (integer)", minval=2, maxval=5)
        if tower_layer_differences != int(tower_layer_differences):
            tk.showerror("Error", "Tower layer differences must be an integer")
        else:
            valid = True
    valid = False

# Meminta input spekifikasi tower dari user
while valid == False:
    brick_length = screen.numinput("Brick Length", "Enter the length of the brick (integer)", minval=1, maxval=35)
    if brick_length != int(brick_length):
        tk.showerror("Error", "Brick length must be an integer")
    else:
        valid = True
valid = False
while valid == False:
    brick_height = screen.numinput("Brick Height", "Enter how tall the bricks are (integer)", minval=1, maxval=25)
    if brick_height != int(brick_height):
        tk.showerror("Error", "Brick height must be an integer")
    else:
        valid = True
valid = False
while valid == False:
    layer_height = screen.numinput("First Tower Layer Amount", "Enter how tall the tower is in bricks (integer)", minval=1, maxval=25)
    if layer_height != int(layer_height):
        tk.showerror("Error", "Tower height must be an integer")
    else:
        valid = True
valid = False
while valid == False:
    layer_length = screen.numinput("Layer Length", "Enter the length of the layer in bricks (integer)", minval=1, maxval=25)
    if layer_length != int(layer_length):
        tk.showerror("Error", "Layer length must be an integer")
    else:
        valid = True

# Menghitung panjang dan tinggi tower
tower_length = brick_length*layer_length
tower_height = brick_height*layer_height
bricks_distance_between_towers = brick_length*distance_between_towers

# Menghitung total brick yang digunakan nanti
total_brick=0

# Memposisikan turtle untuk membuat tower agar tower-tower center
speed(10)
hideturtle()
penup()
setposition(-1*(((tower_length+bricks_distance_between_towers)*amount_tower)-bricks_distance_between_towers)/2, -1*(brick_height*(layer_height+1)+(tower_layer_differences*amount_tower))/2)

# Membuat tower-tower (MAIN LOOPING PROGRAM)
for i in range(0, int(amount_tower)):
    
    # Membuat keliling tower
    showturtle()
    pendown()
    fillcolor('#CA7F65')
    begin_fill()
    for j in range(0, 2):
        forward(tower_length)
        left(90)
        forward(tower_height)
        left(90)
    end_fill()
        
    # Membuat lapisan tower horizontal
    for k in range(0, int(layer_height)):
        if k%2 == 0:
            forward(tower_length)
            left(90)
            forward(brick_height)
            left(90)
        else:
            forward(tower_length)
            right(90)
            forward(brick_height)
            right(90) 
            
    # Membuat lapisan tower vertikal
    if layer_height%2 == 0:
        for l in range(0, int(layer_length)):
            if l%2 == 0:
                forward(brick_length)
                right(90)
                forward(tower_height)
                left(90)
            else:
                forward(brick_length)
                left(90)
                forward(tower_height)
                right(90)
    else:
        for l in range(0, int(layer_length)):
            if l%2 == 0:
                forward(brick_length)
                left(90)
                forward(tower_height)
                right(90)
            else:
                forward(brick_length)
                right(90)
                forward(tower_height)
                left(90)
    
    # Memposisikan turtle untuk membuat atap tower
    penup()
    if layer_height%2 == 1:
        right(90)
        if layer_length%2 == 1:
            forward(tower_height)
        right(90)
        forward(tower_length)
    else:
        if layer_length%2 == 1:
            left(90)
            forward(tower_height)
            right(90)
    
    # Membuat atap tower
    pendown()
    fillcolor('#693424')
    begin_fill()
    forward(brick_length/2)
    left(90)
    forward(brick_height)
    left(90)
    forward(tower_length + brick_length)
    left(90)
    forward(brick_height)
    left(90)
    end_fill()
    for m in range(0, int(layer_length)+1):
        if m%2 == 0:
            forward(brick_length)
            left(90)
            forward(brick_height)
            right(90)
        else:
            forward(brick_length)
            right(90)
            forward(brick_height)
            left(90)
    
    # Membuat jamur
    if m%2 == 1:
        left(90)
        forward(brick_height)
        right(90)
    backward(((tower_length+brick_length)/2)-(brick_length/2))
    left(90)
    penup()
    forward(brick_length)
    pendown()
    fillcolor('#fa0f36')
    begin_fill()
    circle(brick_length/2, 180)
    left(90)
    forward(brick_length)
    end_fill()
    backward((brick_length/2)-(brick_height/2))
    right(90)
    fillcolor("#fabf84")
    begin_fill()
    forward(brick_length)
    right(90)
    forward(brick_height)
    right(90)
    forward(brick_length)
    end_fill()

    # Memposisikan turtle ke tempat terakhir sebelum pembuatan jamur
    penup()
    right(180)
    forward(brick_length)
    left(90)
    forward((tower_length+brick_length)/2+(brick_height/2))
    right(90)
    forward(brick_height)

    # Menghentikan program jika user input 1 tower
    if amount_tower == 1:
        penup()
        break  
    
    # Memposisikan turtle untuk membuat tower selanjutnya
    penup()
    forward(tower_height)
    left(90)
    forward(bricks_distance_between_towers-(brick_length/2))

    # Menghitung total brick
    total_brick=total_brick+(layer_length*(layer_height+1))+1

    # Menghitung panjang dan tinggi tower selanjutnya yang akan ditambahkan tergantung input user
    layer_height = layer_height + tower_layer_differences
    tower_height = brick_height*layer_height

tower_length = brick_length*layer_length
bricks_distance_between_towers = brick_length*distance_between_towers


backward(bricks_distance_between_towers)
fillcolor('green')
begin_fill()
left(180)
forward(((tower_length+bricks_distance_between_towers)*amount_tower)-bricks_distance_between_towers)
right(90)
forward(brick_height)
right(90)
forward(((tower_length+bricks_distance_between_towers)*amount_tower)-bricks_distance_between_towers)
right(90)
forward(brick_height)
right(90) 
end_fill()

pencolor("black")
for a in range(int(((layer_length+distance_between_towers)*amount_tower)-distance_between_towers)):
    if a%2 == 0:
        forward(brick_length)
        right(90)
        forward(brick_height)
        left(90)
    else:
        forward(brick_length)
        left(90)
        forward(brick_height)
        right(90)

# Menulis total brick yang digunakan
hideturtle()
setposition(0, -1*(brick_height*(layer_height+1)+(tower_layer_differences*amount_tower))/2.5)
write(f"{int(amount_tower)} Super Mario Towers have been built with a total of {int(total_brick)} bricks" , align="center", font=("Arial", 20, "normal"))

mainloop()