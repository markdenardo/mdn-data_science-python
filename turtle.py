import turtle
t=turtle.Turtle()


def shape():
  t.forward(30)
  t.right(125)
  t.forward(30)
  t.right(96)
  t.forward(20)

def rec(i):
  while i < 100:
    shape()
    t.right(45)
    i+=1

rec(1)
