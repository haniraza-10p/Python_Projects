class Rectangle:

  width = None
  height = None

  def __init__(self,width,height): 
      self.width = width
      self.height = height  

  def set_width(self,width):
    self.width = width

  def set_height(self,height):
    self.height = height
    
  def get_area(self):
      return self.width * self.height
  
  def get_perimeter(self):
      per = 2 * self.width + 2 * self.height
      return per
  
  def get_diagonal(self):
    diag = (self.width ** 2 + self.height ** 2) ** 0.5
    return diag

  def get_picture(self): 
    
    if self.width>50 or self.height>50:
        return "Too big for picture."
    
    p1 = "*"*self.width + "\n"
    p2 = p1 * self.height
    return p2

  def get_amount_inside(self,shape): 
    
    area1 = self.get_area()
    area2 = shape.get_area()
    answer = area1/area2
    
    return int(answer)

  def __str__(self):
     return "Rectangle(width=%s, height=%s)" % (self.width, self.height)

class Square(Rectangle):
    
    side = None
           
    def set_side(self,side):
        self.width = side
        self.height = side
        self.side = side
    
    def __init__(self,side): 
        self.width = side
        self.height = side
        self.side = side
        
    def __str__(self):
        return "Square(side=%s)" % (self.side)
        
    
      
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

