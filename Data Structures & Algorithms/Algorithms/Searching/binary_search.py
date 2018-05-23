def binary_search(arr,element,start=0,end=None):
    if end is None:
        end = len(arr)-1
    if start>end:
        return False

    mid = (start+end)//2
    if element==arr[mid]:
        return mid
    if element<arr[mid]:
        return binary_search(arr,element,start,mid-1)
    if element > arr[mid]:
        return binary_search(arr,element,mid+1,end)        


# Main program proceeds

my_list = list(range(0,11))
inp = int(input("What element do you want to search for?\n"))
found = binary_search(my_list,inp)
if found:
    print("Element found:",found)
else:
    print("Element not found")
