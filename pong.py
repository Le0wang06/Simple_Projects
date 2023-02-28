import turtle

win = turtle.Screen()
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)


#paddle one
paddle_1 = turtle.Turtle()
paddle_1.tracer(0)
paddle_1.shape("square")
paddle_1.color("white")

#paddle two

#the ball

while True:
  win.update