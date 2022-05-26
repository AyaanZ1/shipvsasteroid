import random
import numpy as np
runs = 0
#program is still in work, so some stuff is still being worked on
while runs < 100:
    seats = np.zeros((4,6),dtype=int)
    rows = len(seats)
    columns = len(seats[0])
    iteration = 0
    iteration2 = 0
#this assigns the 4 "students" their seats. Changing how long the iteration goes for changes the amount of people.
#each student is a 1. You can see all the combos of you and your friends!
    while iteration < 4:
        vertical = random.randint(0,columns-1)
        horizontal = random.randint(0,rows-1)
        seats[horizontal][vertical] = 1
        iteration += 1
#this next loop will print each seperate row on a seperate line
    while iteration2 < rows:
        print(seats[iteration2])
        iteration2 += 1
    print(" " * 2)
    runs += 1

#code isn't most efficient