class point:
    # Constructor : Is itself called on object instantiation
    def __init__(self,a=0,b=0):
        self.x = a
        self.y = b
    def display(self):
        print(self.x,self.y)
    def move_vertical(self,a):
        self.y+=a        
    def move_horizontal(self,a):
        self.x+=a
    def seek_quad(self):
        if self.x>0 and self.y>0:
            print("1st Quadrant")
        
        if self.x<0 and self.y>0:
            print("2nd Quadrant")
        
        if self.x<0 and self.y<0:
            print("3rd Quadrant")
            
        if self.x>0 and self.y<0:
            print("4th Quadrant Quadrant")

# Main Program Proceeds
p = point(10,20)
q = point(30,40)
p.display()
p.move_vertical(5)
p.move_horizontal(5)
p.display()
p.seek_quad()
