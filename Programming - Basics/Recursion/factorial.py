'''
Write a recursive program to calculate factorial of a number.
'''

def Fact(num):
    if (num==0):
        return 1
    elif (num==1):
        return 1
    else:
        return num*Fact(num-1)


# Main Program Starts
n = int(input("Enter the number, you want to find factorial of:"))
ans = Fact(n)
print("The factorial of {} is {}" .format(n,ans))
