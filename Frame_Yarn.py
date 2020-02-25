from turtle import *

speed(0)
shape("turtle")

def frame(h, w):
    """Adjustable frame with width of 30 and outline of
        of width 15"""
    up()
    setpos(-w/2,h/2)
    width(30)
    pencolor("saddlebrown")
    down()
    setheading(-90)
    forward(h)
    setheading(0)
    forward(w)
    setheading(90)
    forward(h)
    setheading(180)
    forward(w)
    up()
    setpos((-w/2 - 20),(h/2 + 20))
    width(10)
    pencolor("black")
    down()
    setheading(-90)
    forward(h + 40)
    setheading(0)
    forward(w + 40)
    setheading(90)
    forward(h + 40)
    setheading(180)
    forward(w + 40)
    up()


def setup(h, w):
    """Places the nail holes with the corresponding height and width
        and then places string across to weave through -- 19"""
    setpos(-w/2, (h/2 - 10))
    setheading(-90)
    pencolor("bisque")
    for x in range(19):
        down()
        dot(5, "grey")
        up()
        forward(h/19)     
    for x in range(19):
        up()
        width(1)
        setpos(-w/2, (h/2 - 10) - (x * (h/19)))
        setheading(0)
        down()
        forward(w)
        dot(5, "grey")
        up()


def vert_solid(h, skip, reps, color):
    """creaates solid color lines seperated by a gap, skips is to place where
        you want to skip into the width (0.5 would start halfway), reps is how many
        lines it will create (50 would give 100w), pick your color"""
    for x in range(reps):
       setpos(((-w/2 + 10) + (w * skip)) + (x * 2), (h/2 - 10))
       down()
       setheading(-90)
       pencolor(color)
       forward(h - 20)
       up()


def vert_sep(h, skip, reps, color_1, color_2, sep):
    """creaates multi color lines seperated by a gap, skips is to place where
        you want to skip into the width (0.5 would start halfway), reps is how many
        lines it will create (50 would give 100w), color)_1 starts, color_2 is next,
        sep is how you want is seperated (ex. 1 = 2 diff colors, 2 = 4 diff colors)"""
    for x in range(reps):
        up()
        setpos(((-w/2 + 10) + (w * skip)) + (x * 2), h/2)
        setheading(-90)
        for y in range(sep):
           down()
           pencolor(color_1)
           forward(h/(sep*2))
           pencolor(color_2)
           forward(h/(sep*2))
           up()

def vert_pos(h, skip, reps, color_1, color_2, dep, long):
    """made similarly to ver_sep"""
    for x in range(reps):
        up()
        setpos(((-w/2 + 10) + (w * skip)) + (x * 2), h/2)
        setheading(-90)
        down()
        pencolor(color_1)
        forward(dep)
        pencolor(color_2)
        forward(long)
        pencolor(color_1)
        forward(h - (dep+long))
        up()
        


def vert_mid(h, skip, reps, color, dep, long):
    """made similarly to ver_sep"""
    up()
    pencolor(color)
    for x in range(reps):
        setpos(((-w/2 + 10) + (w * skip)) + (x * 2), h/2)
        setheading(-90)
        forward((dep * h/19) - 10)
        down()
        forward(long)
        up()


#olive
#chocolate

#NEED TO MAKE IT SO IT ONLY WORKS OFF THE WIRES
               
h = 400
w = 350
frame(h, w)
setup(h, w)
vert_solid(h, 0, int(w/2) - 10, "olive")
vert_mid(h, 2.5/20, 122, "purple", 7, 5 * (h/19))
vert_mid(h, 7/20, 45, "purple", 3, 14 * (h/19))
vert_mid(h, 4/20, 96, "chocolate", 8, 3 * (h/19))
vert_mid(h, 8/20, 25, "chocolate", 4, 12 * (h/19))

#GOOD IDEAS BUT DO NOT FOLLOW NECESSAERY WIRES
#for x in range(20):
   # vert_mid(h, x * (10/350) , 5, "chocolate", (x * 2), 20)
   # vert_mid(h, x * (10/350) , 5, "orange", 20 + (x * 2), 20)
   # vert_mid(h, 0.25 + (x * (1/35)), 5, "orange", 50 + (x * 2), 100) 
    
