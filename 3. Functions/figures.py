import turtle

def draw_square(length): #funkcja do rysowania kwadratu
    for i in range(4): #pętla wykonuje się 4 razy
        turtle.forward(length) #za każdym razem idzie do przodu 100(lenght)
        turtle.right(90) #skręca w prawo o 90 stopni

def draw_triangle(length):
    # Trójkąt równoboczny (jest też równoramienny)
    for i in range(3):
        turtle.forward(length)
        turtle.right(120)

def draw_rectangle(length_a, length_b):
    for i in range(2):
        turtle.forward(length_a)
        turtle.right(90)
        turtle.forward(length_b)
        turtle.right(90)