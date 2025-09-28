from geometry.point import Point

class Triangle:
  def __init__(self, start_point:Point,base:float ,height:float):
    self.start_point = start_point
    self.base = base 
    self.height = height


  def draw_triangle(self, pen):
    x = self.start_point.x
    y = self.start_point.y

    pen.moveto(x,y)
    pen.lineto(x+self.base, y)
    pen.lineto(x+self.base/2, y-self.height)
    pen.lineto(x,y)





  
  
