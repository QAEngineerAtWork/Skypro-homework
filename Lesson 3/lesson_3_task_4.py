# импортируем модуль turtle
import turtle as t

# создаем и называем окно
window = t.Screen()
window.title("My little house")

# настраиваем форму, скорость, ширину и изначальное местоположение курсора
t.shape("arrow")
t.speed(1)
t.width(5)
t.penup()
t.backward(150)
t.left(90)
t.forward(50)
t.right(90)
t.pendown()

#рисуем и закрашиваем стену
t.fillcolor('gray')
t.begin_fill()

for _ in range(4):
    t.forward(300)
    t.right(90)

t.end_fill()

# рисуем и закрашиваем крышу
t.fillcolor('teal')
t.begin_fill()

t.left(45)
t.forward(212)
t.right(90)
t.forward(212)

t.end_fill()

# перемещаем курсор для отрисовки окна
t.left(225)
t.penup()
t.forward(150)
t.left(90)
t.forward(50)
t.right(90)
t.forward(50)
t.pendown()

# рисуем и закрашиваем окно
t.fillcolor('white')
t.begin_fill()

for x in range(4):
    t.left(90)
    t.forward(100)

t.end_fill()

# рисуем перегородки
t.left(90)
t.forward(35)
t.left(90)
t.forward(100)
t.backward(50)
t.right(90)
t.forward(65)

# прячем курсор
t.ht()

# закрываем окно по клику
window.exitonclick()
