from geometry.point import Point

class Sqaure:
  def __init__(self, start_point:Point, side:float):
    self.start_point = start_point
    self.side = side

  def draw_sqaure(self, pen):
   x = self.start_point.x
   y = self.start_point.y

   pen.moveto(x,y)
   pen.lineto(x+self.side, y)
   pen.lineto(x+self.side, y+self.side)
   pen.lineto(x,y+self.side)
   pen.lineto(x,y)

  
