import turtle

# 创建画布
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("#fff5f5")
screen.title("玫瑰花")

# 创建画笔
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)

# 绘制玫瑰花瓣
pen.color("#d62828", "#f94144")
pen.begin_fill()

for angle in range(0, 360, 10):
    pen.setheading(angle)
    pen.circle(120, 60)
    pen.left(120)
    pen.circle(120, 60)

pen.end_fill()

# 绘制花蕊
pen.penup()
pen.goto(0, -20)
pen.setheading(0)
pen.color("#ffb703", "#ffb703")
pen.begin_fill()
pen.circle(20)
pen.end_fill()

# 绘制花茎
pen.goto(0, -20)
pen.setheading(-90)
pen.color("#2d6a4f")
pen.pensize(8)
pen.pendown()
pen.forward(300)

# 绘制叶子
pen.pensize(2)
pen.color("#2d6a4f", "#52b788")

for heading in (-150, -30):
    pen.penup()
    pen.goto(0, -180)
    pen.setheading(heading)
    pen.pendown()
    pen.begin_fill()
    pen.circle(80, 60)
    pen.left(120)
    pen.circle(80, 60)
    pen.end_fill()

# 隐藏画笔并保持窗口
pen.hideturtle()
turtle.done()