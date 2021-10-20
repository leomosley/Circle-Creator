# Circle Creator

This purpose of this program is to create a circle in an array, the user will decied on the radius of the circle and the rest of the dimensions of the circle and the array wil be decided based off of the radius. The user will also be able to choose from all the previously created circles that are stored in the "prev.txt" file

## Required Modules

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install these modules if you do not already have them.

```python
import math
from os import system, name
from time import sleep
```

## Creating and Plotting the Circle

The code I have used for this can be found [here,](https://stackoverflow.com/questions/22777049/how-can-i-draw-a-circle-in-a-data-array-map-in-python) along with a more detailed explanation.

```python
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
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

