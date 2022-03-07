#Maria Eden Peralta
#March 6, 2022


#Problem 1:
#Write a function areaOfCircle(r) which returns the area of a circle of radius r.
#Make sure you use the math module in your solution.

import math

def areaOfCircle(r):
    return math.pi*r*r

print(areaOfCircle(10))
print(areaOfCircle(20))


#Problem 2:
#Write a Python function to check whether a number is in a given range.
#Use range(1,10). Print whether the number is in or not in the range.

# prompt the user to enter a number
number = int(input('Enter a number to check in range(1, 10) : '))

# check if 'number' lies between 1 and 10
if number >= 1 and number <= 10:
    # if it is in range, print apt message
    print('The number is in range(1,10)')

else:
    # if it is NOT in range, print apt message
    print('The number is NOT in range(1,10)') 


#Problem 3: Write a Python function to multiply all the numbers in a list.
#Use list [5, 2, 7, -1].

#create a list
myList = [5,2,7,-1]

#find the sum of myList
listSum = sum(myList)

#print the sum
print('\nSum of the list is', listSum)


#Problem 4:
#Write a Python function that takes a list of numbers and
#returns a new list with unique elements of the first list.
#Use list [1, 3, 3, 3, 6, 2, 3, 5].
#Use the append function.

def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1, 3, 3, 3, 6, 2, 3, 5]))

#Problem 5: Use the following chunk of code as a base to produce the image shown below.

import turtle

def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")

side = 20
width = 10
for squares in range(5):

    drawSquare(alex,side)
    alex.penup()
    alex.back(width)
    alex.right(90)
    alex.forward(width)
    alex.left(90)
    alex.pendown()
    side+=2*width

wn.exitonclick()

#Problem 6: Use the polygon program from the last module and convert it to a function.
#Call the function in a way to create a pattern similar to below.

import turtle

# creating screen
wn = turtle.Screen()


# creating turtle
turt = turtle.Turtle()


# function to create polygons
def Polygon(sides):

    # calculating angle
    angle = 360 / sides

    # creating the polygon
    for count in range(sides):
      turt.forward(100)
      turt.left(angle)
      turt.color("hotpink")


# calling function using for loop to create regular polygons with same initial side
for sides in range(3, 9):
    Polygon(sides)



