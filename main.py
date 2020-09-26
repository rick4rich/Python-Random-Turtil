import turtle, random
name = "enga";
name2 = random.randrange(0,100)
name3 = random.randrange(0,50)
name4 = random.randrange(0,60)
while (name == "enga"):
    turtle.forward(name2)
    turtle.right(name4)
    turtle.back(name3)
    turtle.left(90)
    turtle.right(90)
    turtle.forward(name2)
    turtle.back(45)
    turtle.left(90)
    turtle.right(90)
