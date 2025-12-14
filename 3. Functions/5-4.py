import turtle #bibioteka z funkcjami rysującymi
import figures  # Importujemy nasz własny plik figures.py

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Ustawiamy prędkość domyślnego żółwia (opcjonalnie)
turtle.speed(5)

# Side length
side_length = 100 #przekazuje wartość 100

# Draw a square using the function from our module
# Wywołujemy funkcję z modułu 'figures', podając tylko długość
figures.draw_square(side_length)

# Hide the turtle and finish
turtle.hideturtle() #ukrycie zółwia
window.mainloop() #zapewnia że użytkownik zobaczy efeky końcowy, zanim zakończy działanie