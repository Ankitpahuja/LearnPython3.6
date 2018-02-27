# Create a text file containing lot of numbers in float form. The numbers may be on separate lines and there may be several numbers on same line as well. We have to read this file, and generate a list by comprehension that contains all the float values as elements. After the data has been loaded, display the total number of values and the maximum/minimum and average values.

#Next is a multi-line comment.
#Step1: Write your logic
"""fp = open("float.txt","r")
for line in fp:
    print(line)"""

#Step2: Reducing the lines (removing objects and calling them directly as;)
""" for line in open("float.txt"):
    print(line) """

#Step3: Writing the comprehension!    
L = [float(line) for line in open("float.txt","r")]
print(len(L))
print("Maximum value is: ",max(L))
print("Minimum value is: ",min(L))
print("Average is: ",sum(L)/len(L))

# End of the Program!
