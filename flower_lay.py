import turtle
import random
print("Hi!")
print("It's flower lay drawer")
spd = int(input("Write speed: "))
indent = int(input("Write flower indent: "))
pensize = int(input("Write pensize: "))
masechka = turtle.Turtle()
colours = ["red", "dark orchid", "aquamarine", "hot pink"]
masechka.speed(spd)
def flowerone():
    masechka.penup()
    masechka.forward(10)
    masechka.pendown()
    masechka.pensize(2)
    masechka.color(random.choice(colours))
    masechka.pensize(pensize)
    for i in range(0, 8):
        masechka.circle(6)
        masechka.right(45)
        masechka.penup()
        masechka.forward(5)
        masechka.pendown()
    masechka.right(135)
    masechka.penup()
    masechka.forward(7)
    masechka.pendown()
    masechka.color("goldenrod")
    masechka.pensize(10)
    masechka.circle(2)
while True:
    flowerone()
    masechka.penup()
    masechka.right(random.randint(20, 100))
    masechka.forward(indent)
    masechka.pendown()