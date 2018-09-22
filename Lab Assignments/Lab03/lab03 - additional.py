# Print all prime divisors of a number

num = int(input("Enter a number please: "))
count = int(0)
print("These are the numbers:")
for i in range(1,num+1):
    if(num%i==0):
        print(i)
        
        
# Input an integer and display it in 1000 100 10 and units

num = input("Enter a number please: ")
num_l = list(num)
length_l = len(num_l)

for i in range(0,length_l):
    print (num_l[i],10**(length_l-1))
    length_l-=1
# how to do the above question using string operation?

# Input a string and verify if it is a Palindrome

string = input("Enter a string please: ")
length_s = len(string)
for i in range(0,length_s):
    if(string[i] == (length_s-1)):
        continue
    elif (string[i]==string[i+1]):
        print ("It is an even pallindrome!")
    else:
        print("It is an odd pallindrome!")
    
