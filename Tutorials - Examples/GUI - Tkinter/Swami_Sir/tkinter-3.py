from tkinter import *
master = Tk()
w = Canvas(master, width=500, height=500)
w.pack()
canvas_height=500
canvas_width=500
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y )
mainloop()
