import turtle
import math

# Configurar la ventana de dibujo
window = turtle.Screen()
window.bgcolor("sky blue")
window.setup(width=1000, height=800)

# Crear un objeto Turtle para dibujar
girasol = turtle.Turtle()
girasol.shape("circle")
girasol.color("yellow")
girasol.speed(0)  # Velocidad máxima

# Función para dibujar un pétalo
def dibujar_petalo():
    for _ in range(2):
        girasol.circle(50, 60)
        girasol.left(120)

# Función para dibujar el girasol completo
def dibujar_girasol(x, y, size=1.0):
    girasol.penup()
    girasol.goto(x, y)
    girasol.pendown()
    
    # Dibujar tallo
    girasol.color("green")
    girasol.pensize(3)
    girasol.setheading(90)
    girasol.forward(120 * size)
    
    # Dibujar centro del girasol (café)
    girasol.penup()
    girasol.goto(x, y + 120 * size)
    girasol.pendown()
    girasol.color("brown")
    girasol.begin_fill()
    girasol.circle(20 * size)
    girasol.end_fill()
    
    # Dibujar pétalos
    girasol.color("yellow")
    girasol.penup()
    girasol.goto(x, y + 120 * size)
    girasol.pendown()
    
    for _ in range(12):
        girasol.penup()
        girasol.goto(x, y + 120 * size)
        girasol.pendown()
        girasol.setheading(_ * 30)
        girasol.forward(40 * size)
        girasol.left(30)
        girasol.forward(20 * size)
        girasol.left(120)
        girasol.forward(20 * size)
        girasol.left(30)
        girasol.forward(40 * size)

# Dibujar muchos girasoles
for i in range(15):
    x = (i % 5) * 200 - 400
    y = (i // 5) * 200 - 300
    size = 0.8 + (i % 3) * 0.2
    dibujar_girasol(x, y, size)

# Escribir el mensaje
girasol.penup()
girasol.goto(0, -350)
girasol.color("red")
girasol.write("TE QUIERO MUCHO MI HORMIGUITA", 
              align="center", 
              font=("Arial", 20, "bold"))

# Ocultar el objeto Turtle
girasol.hideturtle()

# Cerrar la ventana al hacer clic en ella
window.exitonclick()