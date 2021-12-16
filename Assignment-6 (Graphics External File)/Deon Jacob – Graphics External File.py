
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



#CUSTOUMIZED DRAWING-------------------------------------------------------


print()
#INPUT FOR CUSTOUM DRAWING
bc = input("Background colour: ")
pc = input("Pen colour: ")
t = input("Art name: ")
fn = t + '.txt'



#opens new file for customized drawing
cfile = open(fn, "w")
#re-opens external txt
mfile = open("external_turtle_file_windows.txt", "r", encoding= "utf16")

#inputs all the new data and position settings into coustum drawing file
cfile.write (bc +'\t'+ pc +'\t'+ t +'\n')
for x in range(x):
    el = mfile.readline()
    cfile.write(el)

# Setup to write the title of the drawing
cfile.write("UP" +'\n')
cfile.write("200" +'\t'+ "-300" +'\n')
cfile.write ("text" +'\t'+ t +'\n')

mfile.close()
cfile.close()



# Re-opens coustom drawing file as a read file to draw
cfile = open(fn, "r")

# Coustum MAIN
def main2(f,t):
    #counts lines
    for aline in f:
        #splits the values on each line
        value = aline.split()
        #analizing/exicuteing directions
        if value[0] == "UP":
            t.penup()
        elif value[0] == "DOWN":
            t.pendown()
        elif value[0] == "text":
            del value[0]
            r = " "
            new = r.join(value)
            t2.write(new, move=False, font=("Calibri", 20, "underline"))
        elif len(value) == 2:
            t.goto(int(value[0]), int(value[1]))
        elif len(value) == 3:
            print()
    t.hideturtle()

#reads & inputs the coustum settings for bg & pen
aline = cfile.readline() 
value = aline.split()

#impots turtle
import turtle
wn = turtle.Screen()
wn.bgcolor(value[0])

t2 = turtle.Turtle() 
t2.color(value[1])
t2.pensize(4)
t2.speed(0)

# Calls main2
main2(cfile,t2)

#Closing all programs
print()
cfile.close()
wn.exitonclick()