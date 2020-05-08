import turtle

def drawCurve(turtle, l, n):
    if n ==0 :
        turtle.forward(l)
        return
    else:
        drawCurve(turtle, l/3, n-1)
        turtle.left(60)
        drawCurve(turtle, l/3, n-1)
        turtle.left(-120)
        drawCurve(turtle, l/3, n-1)
        turtle.left(60)
        drawCurve(turtle, l/3, n-1)
def kochSnowFlake(turtle,l,n):
    for i in range(0,3):
        drawCurve(turtle, l,n)
        turtle.right(120)



if __name__ == "__main__":
    turtle.setup(800, 400)
    drawCurve(turtle, 300,2)
    turtle.exitonclick()