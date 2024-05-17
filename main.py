import tkinter as tk
import random
from rectangle import min_area_rectangle

points = []

window = tk.Tk()
width = window.winfo_screenwidth() 
height = window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
window.title("Minimum Area Rectangle Problem")

canvas = tk.Canvas(window, width=width, height=height)

def add_point():
    for i in range(int(points_entry.get())):
        x = random.randint(width*0.25, width*0.75)
        y = random.randint(height*0.25, height*0.75)
        canvas.create_oval(x-5, y-5, x+5, y+5, fill='red')
        points.append((x, y))

def clear_canvas():
    points.clear()
    canvas.delete('all')

def draw_rectangle():
    if len(points) != 0:
        rectangle = min_area_rectangle(points)
        if rectangle:
            canvas.create_polygon(rectangle, outline='blue', width=5, fill='')

points_label = tk.Label(window, text="Number of points:")
points_label.pack(anchor='w')

points_entry = tk.Entry(window)
points_entry.pack(anchor='w')

add_button = tk.Button(window, text="Add Point", command=add_point)
add_button.pack(anchor='w')

clear_button = tk.Button(window, text="Clear Canvas", command=clear_canvas)
clear_button.pack(anchor='w')

rectangle_button = tk.Button(window, text="Draw Rectangle", command=draw_rectangle)
rectangle_button.pack(anchor='w')

canvas.pack()

window.mainloop()
