from geometry.point import Point
from geometry.line import Line
from drawing.pen1 import Pen
from drawing.tkpanel import Tkpanel
import tkinter as tk
class App:
  def __init__(self):

    self.root = tk.Tk()
    self.root.title("Anus canvas")
    self.canvas = Tkpanel(self.root)
    self.canvas.pack()



  def run(self):
    p1 = Point(0,0)
    p2 = Point(2,2)
    add = p1.add(p2)
    print("Addition: ", add)

    sub = p1.subtract(p2)
    print("subtraction: ", sub)
    
    pen = Pen(self.canvas)
    print(pen.get_position())
   
    pen.move_to(100,200)
    print(pen.get_position())

    pen.line_to(150,50)
    pen.line_to(100,200)
    pen.line_to(200,200)
    pen.line_to(150,50)

    
  




    print("\n Program run successfully")

    self.root.mainloop()









# import tkinter as tk

# r = tk.Tk()
# r.title("Line generator")
# r.mainloop()
