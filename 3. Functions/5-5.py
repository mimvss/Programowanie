import turtle
import figures  # Importujemy nasz plik z figurami

# Ustawienia ekranu
window = turtle.Screen()
window.bgcolor("lightgreen")

# --- WAŻNA ZMIANA ---
# Aby funkcje z figures.py (które używają domyślnego 'turtle') 
# rysowały w tym samym miejscu, w którym jest nasz 'pen', 
# 'pen' musi odnosić się do tego samego obiektu.
pen = turtle 
pen.speed(5)

# --- 1. Rysujemy KWADRATY (Squares) ---
# Pierwszy kwadrat
figures.draw_square(50)

# Przesunięcie
pen.penup() #unosi się nad kratką nie zostawia śladu
pen.goto(-150, 0) #idz do punktu x i y
pen.pendown() #opuść pisak

# Drugi kwadrat
figures.draw_square(50)


# --- 2. Rysujemy TRÓJKĄTY (Triangles) ---
# Przesunięcie na nową pozycję
pen.penup()
pen.goto(100, 100)
pen.pendown()

# Pierwszy trójkąt
figures.draw_triangle(60)

# Przesunięcie
pen.penup()
pen.goto(200, 100)
pen.pendown()

# Drugi trójkąt
figures.draw_triangle(60)


# --- 3. Rysujemy PROSTOKĄTY (Rectangles) ---
# Przesunięcie na nową pozycję
pen.penup()
pen.goto(-150, -150)
pen.pendown()

# Pierwszy prostokąt (boki 80 i 40)
figures.draw_rectangle(80, 40)

# Przesunięcie
pen.penup()
pen.goto(0, -150)
pen.pendown()

# Drugi prostokąt
figures.draw_rectangle(80, 40)


# Koniec programu
pen.hideturtle()
window.mainloop()