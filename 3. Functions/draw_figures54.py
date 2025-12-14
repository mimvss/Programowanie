import turtle

def draw_square(length):
    # Tworzymy żółwia (pisaka) wewnątrz funkcji
    pen = turtle.Turtle()
    pen.speed(5)
    
    # Rysujemy kwadrat
    for i in range(4):
        pen.forward(length)
        pen.right(90)
    
    # Ukrywamy żółwia na koniec (opcjonalne, ale ładne)
    pen.hideturtle()  # Importujemy Twój plik figures.py

# 1. Ustawiamy ekran (tak jak w oryginalnym kodzie)
window = turtle.Screen()
window.bgcolor("lightgreen")

# 2. Rysujemy kwadrat korzystając z funkcji z importowanego modułu
# Podajemy tylko długość boku (np. 100)
draw_square(100)

# 3. Zatrzymujemy okno, żeby nie zniknęło od razu
window.mainloop()