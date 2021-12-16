
#MAIN
def main1(f, t):
    #counts lines
    for aline in f:
        #splits the values on each line
        value = aline.split()
        #analizing/exicuteing directions
        if value[0] == "UP":
            t.penup()
        elif value[0] == "DOWN":
            t.pendown()
        elif len(value) == 2:
            t.goto(int(value[0]), int(value[1]))
    t.hideturtle()

#IMPORTS TURTULE
import turtle
wn = turtle.Screen()
wn.bgcolor("black")

t1 = turtle.Turtle() 
t1.color("silver")
t1.pensize(4)
t1.speed(0)

#IMPORTS original FILE
mfile = open("external_turtle_file_windows.txt", "r", encoding= "utf16")

#Calls main
main1(mfile, t1)

#clear window
print()
input("Click enter to clear the draft drawing")
wn.clear()
print()

#Closes file
mfile.close()



# To find the number of lines in original file + records it for use
mfile = open("external_turtle_file_windows.txt", "r", encoding= "utf16")
ls = mfile.readlines()
x = len(ls)
mfile.close()
