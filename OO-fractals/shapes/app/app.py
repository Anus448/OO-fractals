from geometry.point import Point
from geometry.line import Line
from drawing.pen import pen
from drawing.tkpanel import Tkpanel
from triangle.triangle import Triangle
from square.square import Sqaure
import tkinter as tk

class App:
  def __init__(self):

    self.root = tk.Tk()
    self.root.title("Trianlge Drawing")
    self.canvas = Tkpanel(self.root)
    self.canvas.pack()

    self.pen=pen(self.canvas)
    
  def run(self):
    
    traingle = Triangle(Point(400,300), base = 150, height= 200)
    traingle.draw_triangle(self.pen)

    square = Sqaure(Point(80, 150), side = 150.58)
    square.draw_sqaure(self.pen)
    
    self.root.mainloop() 

