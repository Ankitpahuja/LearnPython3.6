# This file holds all the implementation to the function made for DS & Algo Implementation

from Modules import *

# Implementing Linear Search by passing the list and an item | Returns position of the element found!
sample = [1,2,3,4,5,6,7,8,99,100]
item = int(input("Enter the number you want to search from range 1-100:"))
position = LinearSearch (sample,item)
if position:
    print("Element found at: ",position,"\nNote: Elements in CS Starts at index 0. ")
else:
    print(" Element Not Found!")
