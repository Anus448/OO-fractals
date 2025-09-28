import tkinter as tk
from geometry.point import Point
from geometry.line import Line

class Tkpanel(tk.Canvas):
  def __init__(self, master=None, width = 800, height = 600):
    super().__init__(master, width=width , height= height, bg = 'white')
    self.lines = []


  def add_line(self, p1:Point, p2:Point):
    l1 = Line(p1,p2)
    self.lines.append(l1)
    self.draw()

  def draw(self):
    self.delete('all')
    for line in self.lines:
      x1, y1 = line._start.x, line._start.y
      x2, y2 = line._end.x, line._end.y
      self.create_line(x1,y1, x2, y2, fill = "black", width = 2)


