from math import floor

class Rectangle:
    def __init__(self, width, height):
        self.width=width
        self.height=height
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def set_width(self, w):
        self.width=w
    def set_height(self, h):
        self.height=h
    
    def get_area(self):
        return self.width*self.height
    def get_perimeter(self):
        return 2*(self.width+self.height)
    def get_diagonal(self):
        return (self.width**2+self.height**2)**0.5
    def get_picture(self):
        self.img=""
        if self.width>50 or self.height>50:
            return "Too big for picture."
        for i in range(self.height):
            for i in range(self.width):
                self.img+="*"
            self.img+="\n"
        return self.img
    def get_amount_inside(self, shape):
        if self.width<shape.width or self.height<shape.height:
            return 0
        else:
            if self.width>=shape.width and self.height>=shape.height:
                return floor(self.width/shape.width)*floor(self.height/shape.height)
                

class Square(Rectangle):
    def __init__(self, wh):
        self.side=wh
        self.width=wh
        self.height=wh

    def __str__(self):
        return f"Square(side={self.side})"
    
    def set_side(self, s):
        self.side=s
        self.width=s
        self.height=s
    def set_width(self, s):
        self.side=s
        self.width=s
        self.height=s
    def set_height(self, s):
        self.side=s
        self.width=s
        self.height=s

rect=Rectangle(5, 10)
print(rect.get_area())
#rect.set_width(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq=Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

print(rect.get_amount_inside(sq))
