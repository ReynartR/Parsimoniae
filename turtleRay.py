
import turtle


ray = turtle.Turtle()
key = input("Enter the number of employees")



def turtleThings(key):
    ray = turtle.Turtle()
    key = str(input("Enter the number of employees"))
    
    alist = []
    year = 2017-len(key)
    alist2= []

    
    ray.color("blue")
    ray.pensize(5)
    ray.penup()
    ray.goto(150,0)
    ray.write("Year")
    ray.pendown()
    ray.goto(-150,0)
    ray.goto(-150,250)
    ray.write("Employees")
    ray.goto(-150,0)
    ray.forward(20)

    for i in key:
        if i.isdigit():
            return print("Failure")
        else:

            value = ord(i)

            ray.left(90)
            ray.forward(value)
            ray.right(90)
            ray.write(value)
            ray.forward(20)
            ray.right(90)
            ray.forward(value)
            ray.penup()
            ray.forward(20)
            ray.right(90)
            ray.forward(10)
            ray.write(year)
            ray.backward(10)
            ray.left(90)
            ray.backward(20)
            ray.pendown()
            ray.left(90)
            ray.forward(20)
            alist.append(value)
            year += 1

        
    for i in alist:
        val = i % 26
        alist2.append(val)
    return print(alist2)  

turtleThings(key)
