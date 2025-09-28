from geometry.point import Point

class Line:
  def __init__(self, start:Point, end:Point):  #creating attributes of point type
    self._start = start
    self._end = end

  def length(self):
    return self._start.distance(self._end)
    
  def __str__(self):  # use of magic functions
    return f"Line({self._start} → {self._end})"
  


