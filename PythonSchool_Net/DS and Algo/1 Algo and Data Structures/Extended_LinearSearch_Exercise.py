
def LinearSearch(list,item):
    position = 0
    found = False
    while position<len(list) and not found:
        if list[position] == item:
            found = True
            return position
        position+=1

# Main Program Proceeds
sample = [1,2,3,4,5,6,7,8,99,100]
item = int(input("Enter the number you want to search from range 1-100:"))
position = LinearSearch (sample,item)
if position:
    print("Element found at: ",position,"\nNote: Elements in CS Starts at index 0. ")
else:
    print("Element Not Found!")
    query = input("Do you want to add a number to the list: (Reply with a Y if yes!)")
    if query == 'Y':
        sample.append(item)
        print(sample)
        print("Item added Successfully!")
    else:
        print("Item not added and thanks for your time!")
