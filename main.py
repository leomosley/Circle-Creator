# modules required
import math
from os import system, name
from time import sleep

# main class
class circleCreator:

    # initializes class
    def __init__(self):
        self.clear()
        print("\t\t\tWelcome to the circle creator\n")
        ans = input("Would you like to:\nA: Create a new circle\nB: Open a previous circle\n-> ")
        
        # user makes choice and corresponding function is called
        if ans.upper() == "A":
            self.getValue()
            sleep(1)
            self.continueProgram()

        elif ans.upper() == "B":
            self.prevCircles()
            sleep(1)
            self.continueProgram()

        else:   # if invalid input is made
            print("Error: Invalid input\n\nRESTART")
            sleep(1)
            self.clear()
            sleep(1)
            circleCreator()
    
    # clears terminal
    def clear(self):
        if name == 'nt':
            _ = system('cls')
    
    # takes users input
    def getValue(self):
        r = int(input("\nEnter the radius of your derired circle: "))
        self.createCircle(r)

    # creating a the circle
    def createCircle(self, r):
        
        width = height = (2*r) + 1
        a = b = r

        # writes radius value to previous circles text file
        with open("prev.txt", "a+") as f:
            
            # calls function to check if radius value is alreday in prev.txt
            answer = self.inPrev(r)
            if answer == False: # if not in prev.txt
                f.write(f"{str(r)}\n") # write r to prev.txt
            
            f.close()

        # code below by Peter Gibson [https://stackoverflow.com/questions/22777049/how-can-i-draw-a-circle-in-a-data-array-map-in-python]
        # creates arr without plotted points
        map_ = [['.' for x in range(width)] for y in range(height)]

        # creates and maps points on the array
        for angle in range(0, 360, 5):
            x = r * math.sin(math.radians(angle)) + a
            y = r * math.cos(math.radians(angle)) + b
            map_[int(round(y))][int(round(x))] = '#'

        # prints the array neatly
        for line in map_:
            print(' '.join(line))

    # checks if radius value is not already in prev.txt
    def inPrev(self, val):

        with open("prev.txt", "r") as f:
            for i in f:
                if val == int(i):
                    return True # if in prev.txt
            return False # if not in prev.txt
            f.close()
    
    # previous circles
    def prevCircles(self):
        
        # prints every circle in prev.txt along with a corresponding number
        with open("prev.txt", "r") as f:
            for n,i in enumerate(f):
                print(f"Circle {n+1}:")
                self.createCircle(int(i))
                print("")
            f.close()

        # user chooses what circle they want to use
        circleNum = int(input("What circle would you like to use? ")) - 1

        # printts the users choice
        with open("prev.txt") as f:
            for n, i in enumerate(f):
                
                if n == circleNum:
                    self.createCircle(int(i))

            f.close()     

    # checks if user wants to continue using the progam
    def continueProgram(self):

        ans = input("\nWould you like to create another circle or use a previous one? (y/n): ")
        
        if ans.lower() == "y":
            circleCreator() # recall main class
        elif ans.lower() == "n":
            ans = input("\nWould you like to:\nA: Close this program\nB: Leave it running\n-> ")
            if ans.upper() == "A":
                self.clear() # clear terminal
            elif ans.upper() == "B":
                print("Ok... Enjoy") # leaves program as it is
            else:
                print("ERROR: Invalid Input\nRESTART") # invalid input resarts the program
                sleep(1)
                self.clear()
                sleep(1)
                circleCreator()   

#main program
circleCreator()
