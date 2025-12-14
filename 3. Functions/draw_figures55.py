# --- Plik: draw_figures.py ---
import turtle

def draw_square(pen, length):
    # Rysuje kwadrat
    for i in range(4):
        pen.forward(length)
        pen.right(90)

def draw_triangle(pen, length):
    # Rysuje trójkąt (używamy kąta 120 stopni dla trójkąta równobocznego)
    for i in range(3):
        pen.forward(length)
        pen.right(120)

def draw_rectangle(pen, length_a, length_b):
    # Rysuje prostokąt
    for i in range(2):
        pen.forward(length_a)
        pen.right(90)
        pen.forward(length_b)
        pen.right(90)  # Importujemy nasz plik z figurami

# 1. Ustawienia ekranu
window = turtle.Screen()
window.bgcolor("lightgreen")

# 2. Tworzymy żółwia (pisak)
pen = turtle.Turtle()
pen.speed(5)  # Szybkość rysowania

# --- RYSOWANIE KWADRATÓW ---
# Kwadrat 1
draw_square(pen, 50) 

# Przenoszenie (bez rysowania linii)
pen.penup()         # Podnieś pisak
pen.goto(100, 0)    # Idź w prawo
pen.pendown()       # Opuść pisak

# Kwadrat 2
draw_square(pen, 50)


# --- RYSOWANIE TRÓJKĄTÓW ---
# Przenoszenie w nowe miejsce
pen.penup()
pen.goto(-150, -100) # Idź w dół i w lewo
pen.pendown()

# Trójkąt 1
draw_triangle(pen, 60)

# Przenoszenie kawałek dalej
pen.penup()
pen.goto(-50, -100)
pen.pendown()

# Trójkąt 2
draw_triangle(pen, 60)


# --- RYSOWANIE PROSTOKĄTÓW ---
# Przenoszenie
pen.penup()
pen.goto(100, -100)
pen.pendown()

# Prostokąt 1 (boki 80 i 40)
draw_rectangle(pen, 80, 40)

# Przenoszenie
pen.penup()
pen.goto(200, -100)
pen.pendown()

# Prostokąt 2
draw_rectangle(pen, 80, 40)


# Koniec - ukrywamy żółwia i czekamy
pen.hideturtle()
window.mainloop()