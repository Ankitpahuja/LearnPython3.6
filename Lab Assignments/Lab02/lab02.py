#  Q1: From a string containing a sequence “ATTTCTATTATGTTATCTATGTTTATGGTA”
#  Find out all positions where a “ATG” exists.

string = "ATGTTCTATTATGTTATCTATGTTTATGGTA"
for i in range(len(string)-2):
    if string[i]=='A' and string[i+1]=='T' and string[i+2]=='G':
        print (i)
        i+=2
    else:
        continue

# Q2: error - on how to get this output in the same line and not on a new one?

string = "ATGTTCTATTATGTTATCTATGTTTATGGTA"
for i in range(len(string)-2):
    if string[i]=='A' and string[i+1]=='T' and string[i+2]=='G':
        print (i)
        i+=2
    else:
        print (".")

        
# From a URL which may start with http:// or https:// or simply www, display the domain and the remaining part of the URL separately.

#  Display the string that is the last component of a URL ( i.e. the text after the last / symbol ). The URL should be entered from the keyboard, and may contain many / symbols.

#  From a string cut the first character and append it at the end and display the resulting string. This process should be repeated n times, where n is input from the keyboard as a number.
    

user_string = input("Enter a string")
times = int(input("Enter the number of times you want to keep 1st string to last and so on... : "))


for i in range(times):
    user_string+=user_string[0]
    user_string = user_string[1:]
print (user_string)


# From a string, extract the first number that exists in it. Note that the number may be more than one digit also. "A GROUP OF 25 CATS RAN"  should give you 25
