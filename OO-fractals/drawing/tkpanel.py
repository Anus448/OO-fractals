import tkinter as tk
from geometry.point import Point
from geometry.line import Line

class Tkpanel(tk.Canvas):
  def __init__(self, master=None, width = 500, height = 500):
    super().__init__(master, width=width , height= height, bg = 'white')
    self.lines = []


  def add_line(self, p1:Point, p2:Point):
    l1 = Line(p1,p2)
    self.lines.append(l1)
    self.draw()

  def draw(self):
    self.delete('all')
    for line in self.lines:
      self.create_line(line._start.x, line._start.y,
                       line._end.x, line._end.y,
                       fill= 'black', width= 2
                       )
