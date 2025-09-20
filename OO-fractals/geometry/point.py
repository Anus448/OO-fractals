import math

class Point:
  def __init__(self, x=0, y=0):
    self._x = x
    self._y = y

  @property
  def x(self):
    print("Value of x is: ")
    return self._x

  @x.setter
  def x(self, value):
    self._x = value
    print("The new x value is: ", self._x)


  @property
  def y(self):
   print("Value of y is: ")
   return self._y

  @y.setter
  def y(self, value):
   self._y = value
   print("The new y value is: ", self._y)
   
   
  def add(self, otherpoint):
    return Point(self._x + otherpoint._x , self._y + otherpoint._y)

  def subtract(self, otherpoint):
    return Point(self._x - otherpoint._x, self._y - otherpoint._y )

  def distance(self, p):
    return math.sqrt((self._x - p._x)**2 + (self._y - p._y)**2)

  def __str__(self):
    return(f"({self._x}, {self._y})")
  
  def __repr__(self):
    return(f"({self._x}, {self._y})")
  

    