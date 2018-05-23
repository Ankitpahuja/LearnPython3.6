import tkinter as tk

window = tk.Tk()

window.title("Tkinter's Tutorial")

window.geometry("550x400")

# Label
title = tk.Label(text="Hello World. Welcome to tkinter's tutorial!", font=("Times New Roman",20))
title.grid(column=0,row=0)

#Button1
button1 = tk.Button(text="Click Me!", bg="red")
button1.grid(column=0,row=1)

#Entry Field
entry_field1 = tk.Entry()
entry_field1.grid(column=0, row=2)

#Text Field
text_field = tk.Text(master=window, height=10, width=30)
text_field.grid()
# mainloop() fundtion called with windows; it runs everything inside that window. Make sure this function is at the last.
window.mainloop() 


'''
Following are the steps you need to follow in ordert to build an app using tkinter:
0. Plan out layout of app
1. Create a window for the app (Add title and geometry)
2. Declare Size, Place labels, buttons, entry fields etc. on the window (Use grids to place them!)
3. Place Labels, buttons, entry fields, onto the window!
4. Connect buttons/entries to one another through functions
5. Use .mainloop() to run the window!

'''

''' More resources can be found at: http://effbot.org/tkinterbook/ '''
