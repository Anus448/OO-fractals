from geometry.point import Point
from drawing.tkpanel import TKpanel 

class pen:
  def __init__(self, master =None):
    self._canvas = TKpanel(master)
    self._cp = Point(0,0)

  def moveto(self, x, y): 
    # moves the pen to a new position without drawing
    self._cp = Point(x,y)

  def lineto(self, x, y):
    # draws the line between cp and new_point
    #Then updates the cp

    new_point = Point(x,y)
    self._canvas.add_line(self._cp,new_point)

    self._cp = new_point  #updation of current position 

  def get_position(self):
    return self._cp      #returns the latest position of pen
  



  

  