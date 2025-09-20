class point:
  def __init__(self,x,y):
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
   


p = point(5,5)

print(p.x)
print(p.y)


p.x = 10
p.y = 10

