import turtle

# Настройки экрана
screen = turtle.Screen()
screen.setup(width=1000, height=400)
screen.bgcolor("#1a1a1a")

t = turtle.Turtle()
t.speed(0) # Максимальная скорость для проверки
t.pensize(5)
t.color("cyan")

def reset_pos(x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(90) # Всегда смотрим вверх перед буквой
    t.pendown()

def draw_N():
    t.forward(100)
    t.goto(t.xcor() + 60, t.ycor() - 100)
    t.forward(100)

def draw_U():
    t.penup()
    t.forward(100)
    t.pendown()
    t.setheading(-90)
    t.forward(70)
    t.circle(30, 180)
    t.forward(70)

def draw_R():
    t.forward(100)
    t.right(90)
    t.circle(-25, 180)
    t.left(135)
    t.forward(70)

def draw_M():
    t.forward(100)
    t.goto(t.xcor() + 30, t.ycor() - 40)
    t.goto(t.xcor() + 30, t.ycor() + 40)
    t.setheading(-90)
    t.forward(100)

def draw_A():
    t.goto(t.xcor() + 30, t.ycor() + 100)
    t.goto(t.xcor() + 30, t.ycor() - 100)
    # Перекладина
    t.penup()
    t.goto(t.xcor() - 45, t.ycor() + 40)
    t.setheading(0)
    t.pendown()
    t.forward(30)

def draw_T():
    t.penup()
    t.forward(100)
    t.pendown()
    t.setheading(0)
    t.forward(80)
    t.penup()
    t.backward(40)
    t.setheading(-90)
    t.pendown()
    t.forward(100)

# Основная логика отрисовки
letters = [draw_N, draw_U, draw_R, draw_M, draw_U, draw_R, draw_A, draw_T]
current_x = -400

for func in letters:
    reset_pos(current_x, -50)
    func()
    current_x += 100 # Шаг между буквами

t.hideturtle()
screen.mainloop()