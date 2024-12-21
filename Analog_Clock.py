import tkinter as tk
import time
import math

window = tk.Tk()
window.title("Analog Clock")
window.geometry("400x400")
window.resizable(False, False)

canvas = tk.Canvas(window, width=400, height=400, bg="white")
canvas.pack()

center_x, center_y = 200, 200
clock_radius = 180

canvas.create_oval(center_x - clock_radius, center_y - clock_radius, 
                   center_x + clock_radius, center_y + clock_radius, fill="lightblue")

for i in range(1, 13):
    angle = math.radians((360 / 12) * i - 90)
    x = center_x + (clock_radius - 30) * math.cos(angle)
    y = center_y + (clock_radius - 30) * math.sin(angle)
    canvas.create_text(x, y, text=str(i), font=("Arial", 14, "bold"))

def get_hand_coords(length, angle):
    angle = math.radians(angle - 90) 
    x = center_x + length * math.cos(angle)
    y = center_y + length * math.sin(angle)
    return x, y

hour_hand = canvas.create_line(center_x, center_y, center_x, center_y - 50, width=6, fill="black")
minute_hand = canvas.create_line(center_x, center_y, center_x, center_y - 70, width=4, fill="blue")
second_hand = canvas.create_line(center_x, center_y, center_x, center_y - 90, width=2, fill="red")

def update_clock():
    now = time.localtime()
    hours = now.tm_hour % 12
    minutes = now.tm_min
    seconds = now.tm_sec
    hour_angle = (360 / 12) * hours + (360 / 12) * (minutes / 60)
    minute_angle = (360 / 60) * minutes + (360 / 60) * (seconds / 60)
    second_angle = (360 / 60) * seconds
    canvas.coords(hour_hand, center_x, center_y, *get_hand_coords(60, hour_angle))
    canvas.coords(minute_hand, center_x, center_y, *get_hand_coords(90, minute_angle))
    canvas.coords(second_hand, center_x, center_y, *get_hand_coords(120, second_angle))
    window.after(1000, update_clock)

update_clock()

window.mainloop()