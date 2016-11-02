import turtle

def draw_art():

    window = turtle.Screen()


    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color("red")
    angie.speed(10)
    for i in range(1,37):
        angie.right(10)
        angie.circle(100)
#window.exitonclick()
draw_art()
