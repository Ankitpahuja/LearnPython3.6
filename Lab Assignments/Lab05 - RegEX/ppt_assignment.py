'''
Write a function that would validate an enrolment number.

valid=validateEnrolment(eno )

Example enrolment number U101113FCS498
U-1011-13-F-CS-498
13 – is the year of registration, can be between 00 to 99
CS, EC or BT
Last 3 are digits
'''
import re
pattern = re.compile("U1011[0-9][0-9]F(CS|BT)\d\d\d")
def enroll(eno):
    found = pattern.search(eno)
    if found:
        return True
    else:
        return False


# Main Program Proceeds
eno = input("Enter Enrollment number: (I will tell if it exists or not!)\n")
n = enroll(eno)
if n:
    print("Yes, It's a valid E NO. and it exists!")
else:
    print("No. Isn't a valid E No.")
