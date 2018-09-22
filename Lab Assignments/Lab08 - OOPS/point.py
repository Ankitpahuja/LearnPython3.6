# With this example you will completely get the feel of using a class, instantiating an object and then making methods and calling them. 

class point:
    def __init__(self,a=0,b=0):
        self.x = a;
        self.y = b;

    def display(self):
        print(self.x,self.y)

    def movVertical (self,offset):
        self.y += offset
    
    def movHorizontal (self,offset):
        self.x += offset


#Main Program Proceeds

p = point(10,20)
p.movHorizontal(5)
p.movVertical(-5)
p.display()

