# draw square in Python Turtle
import turtle

t = turtle.Turtle()

s = int(input("Enter the length of the side of the Squre: "))

# drawing first side
t.forward(s) # Forward turtle by s units
t.left(90) # Turn turtle by 90 degree

# drawing second side
t.forward(s) # Forward turtle by s units
t.left(90) # Turn turtle by 90 degree

# drawing third side
t.forward(s) # Forward turtle by s units
t.left(90) # Turn turtle by 90 degree

# drawing fourth side
t.forward(s) # Forward turtle by s units
t.left(90) # Turn turtle by 90 degree
# draw Squre in Python Turtle
import turtle

t = turtle.Turtle()

s = int(input("Enter the length of the side of squre: "))

for _ in range(4):
  t.forward(s) # Forward turtle by s units
  t.left(90) # Turn turtle by 90 degree
