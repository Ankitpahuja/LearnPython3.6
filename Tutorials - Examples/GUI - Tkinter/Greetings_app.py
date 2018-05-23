'''
You are supposed to build a greetings app; where on input you output Hello <Your input>!
'''
import random
import tkinter as tk

window = tk.Tk()
window.title("Greetings_____")
window.geometry("400x400")


# Functions
def phrase_generator():
    phrases = ["Hello","What's Up!","Aloha"]
    name = str(entry1.get())
    return phrases[random.randint(0,2)] + " "+name

def phrase_display():
    greeting = phrase_generator()

    # This creates the text field
    greeting_display = tk.Text(master=window,height=10,width=30)
    greeting_display.grid(column=0, row=3)

    greeting_display.insert(0.0,greeting) #Paramter1 : index, Param2 : Value

# Label
label1= tk.Label(text="Welcome to my greetings App!")
label1.grid(column=0, row=0)

label2 = tk.Label(text="What's your name?")
label2.grid(column=0,row=1)

# Entry Field
entry1 = tk.Entry()
entry1.grid(column=1, row=1)

# Button
button1 = tk.Button(text="Click Me", command = phrase_display)
button1.grid(column=0, row=2)

window.mainloop()
