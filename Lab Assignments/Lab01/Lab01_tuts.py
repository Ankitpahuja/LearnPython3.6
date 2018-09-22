# know what happens on doing this?
a=b=c=10,4,3
print (b)

test = abs(-5.99)
print (test)

one = round(4.4,0)
second = round (4.5,0)
third = round (4.6,0)
forth = round (4.9,0)
fifth = round (4.665,2)
print (one)
print (second)
print (third)
print (forth)
print (fifth)


# Know why it happens further - #Swami_Sir
sixth = round (1.5,0)
seventh = round (2.5,0)
print (sixth)
print (seventh)

# What does it give you -  String or a number?
a = int ("10")
print (a)

b = str(12)
print (b)

c = str(4.5)
print (c)

#print (abs(c))   Know what happens here!

# This is how conversion to float happens:
d= float (50)
e= float ("12")

print (d,e)

# Working with sequences:

f = (20,12,15,161,78)
print (max(f))
print (min(f))
print (len(f))

g = "Hello World!"
print (max(g))
print (min(g))
print (len(g))

# Character to ASCII conversions:

print (chr(65))
print (ord('A'))
print (chr(351)) #Swami_Sir

# divmod function : returns quotient and remainder

print (divmod(10,3))

# Hex Conversions
print (hex (65))

# Power Function
h=pow(5,2)
i = pow (5,2,3) # It means (5**2)%3
print (i)

j = "hello world"
print(j.startswith ("he"))

# Using in and not in with sequences
print ("a" in "hello world")
print ("a" not in "hello world")
print (10 in ( 5,6,9,10,15))
