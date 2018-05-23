from tkinter import *
def addRecord():
    f=open("data.csv","a")
    f.write(name.get()+","+maths.get()+","+english.get()+"\n")
    name.delete(0,END)
    maths.delete(0,END)
    english.delete(0,END)
    f.close()

 
master = Tk()
Label(master, text='Name').grid(row=0)
Label(master, text='Maths').grid(row=1)
Label(master, text='English').grid(row=2)

name = Entry(master)
maths = Entry(master)
english=Entry(master)

name.grid(row=0, column=1)
maths.grid(row=1, column=1)
english.grid(row=2, column=1)

b = Button(master, text="SAVE", width=10, command=addRecord)
b.grid(row=3,column=1)

mainloop()





