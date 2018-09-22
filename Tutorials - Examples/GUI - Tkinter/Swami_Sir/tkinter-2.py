import tkinter as tk
window = tk.Tk()
window.title('Testing button')
button = tk.Button(window, text='Stop', width=15, command=window.destroy)
button.pack()
window.mainloop()
