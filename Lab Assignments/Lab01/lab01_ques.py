# Input Length, Width and compute the area of a rectangle


##length = int(input("Enter the length:"))
##width = int(input("Enter the width:"))
##area = length * width
##print (area)

#  From an integer number, display its unit's place


##num = int (input("Enter the number: "))
##unit_place = num%10
##print (unit_place)

# Remove the unit's place from an integer ( 2356 should become 235 )


##num = input("Enter the number: ")
##new_num = num[:-1]
##print (new_num)
##
### OR
##
##num = int (input("Enter the number: "))
##new_num = int (num/10)
##print (new_num)

# Input n and display if it is an odd or even

##n = int(input("Enter the number: "))
##if n%2 == 0:
##    print("The number is even")
##else :
##    print ("The number is odd")


# Based on input n, display n number of lines with stars equal to line number:


##n = int(input("Enter the number: "))
##m="*"
##for i in range(n+1):
##    print(i*m)

# Input n and display if it is a prime number or not


##n = int(input("Enter the number: "))
##count = int (0)
##for i in range(1,int(n/2)):
##    if n%i==0:
##        count+=1
##if count >= 2:
##    print("The number is not prime.")
##else:
##    print("It is a prime number.")


# Count the number of digits in an integer


##n = input ("Enter the number: ")
##no_of_digits = len(n)
##print (no_of_digits)



# Display the first digit of any integer ( most significant ) #swami_sir

n = int(input("Enter an integer: "))
for i in range(n):
    x=divmod(n,10)
    if divmod(n,10)[0] > 1:
        continue
    else:
        print (x)

