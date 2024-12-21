import tkinter as tk
from time import strftime

window = tk.Tk()
window.title("Digital Clock")

clock_label = tk.Label(window, font=('calibri', 40, 'bold'), background='black', foreground='white')
clock_label.pack(anchor='center')

def update_time():
    current_time = strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time) 

update_time()

window.mainloop()