import tkinter
from _datetime import datetime
import threading
import tkinter as tk
from tkinter import messagebox

root = tkinter.Tk()
root.geometry('900x700')
root.minsize(900, 700)
root.maxsize(900, 700)

'''Lights being on or off are determined by fill parameters of each index number of tuples containing colours. 
0 - light is off
1 - light is on
Each colour has its own two-element tuple declared below.
'''
green = ('#175700','#3DE500')
yellow = ('#957700','#F9C700')
red = ('#7D0000','#F90000')
step_day = 0
step_night = 0

lights_state_day = ('green', 'yellow', 'red', 'red yellow', 'off')
lights_state_night = ('yellow', 'off')
lights_interval_day = (2000, 2000, 2000, 10000, 2000, 2000)
lights_interval_night = (500, 500)
work_mode = ('day','night')

TrafficSemaphor = tkinter.Canvas(height=450, width=200, bg='black')
TrafficSemaphor.place(x=100, y=100)

red_traffic = TrafficSemaphor.create_oval(50, 25, 150, 125, fill=red[0])
yellow_traffic = TrafficSemaphor.create_oval(50, 175, 150, 275, fill=yellow[0])
green_traffic = TrafficSemaphor.create_oval(50, 325, 150, 425, fill=green[1])

PedestrianSemaphor = tkinter.Canvas(height=300, width=200, bg='black')
PedestrianSemaphor.place(x=350, y=175)
red_pedestrian = PedestrianSemaphor.create_oval(50, 25, 150, 125, fill=red[1])
green_pedestrian = PedestrianSemaphor.create_oval(50, 175, 150, 275, fill=green[0])

def config_semaphors_traffic(state):
    match state:
        case 'green':
            TrafficSemaphor.itemconfig(red_traffic, fill=red[0])
            TrafficSemaphor.itemconfig(yellow_traffic, fill=yellow[0])
            TrafficSemaphor.itemconfig(green_traffic, fill=green[1])

        case 'yellow':
            TrafficSemaphor.itemconfig(red_traffic, fill=red[0])
            TrafficSemaphor.itemconfig(yellow_traffic, fill=yellow[1])
            TrafficSemaphor.itemconfig(green_traffic, fill=green[0])

        case 'red':
            TrafficSemaphor.itemconfig(red_traffic, fill=red[1])
            TrafficSemaphor.itemconfig(yellow_traffic, fill=yellow[0])
            TrafficSemaphor.itemconfig(green_traffic, fill=green[0])

        case 'red yellow':
            TrafficSemaphor.itemconfig(red_traffic, fill=red[1])
            TrafficSemaphor.itemconfig(yellow_traffic, fill=yellow[1])
            TrafficSemaphor.itemconfig(green_traffic, fill=green[0])

        case 'off':
            TrafficSemaphor.itemconfig(red_traffic, fill=red[0])
            TrafficSemaphor.itemconfig(yellow_traffic, fill=yellow[0])
            TrafficSemaphor.itemconfig(green_traffic, fill=green[0])

        case _:
            TrafficSemaphor.itemconfig(red_traffic, fill=red[0])
            TrafficSemaphor.itemconfig(yellow_traffic, fill=yellow[0])
            TrafficSemaphor.itemconfig(green_traffic, fill=green[0])

def config_semaphors_pedestrian(state):
    match state:
        case 'red':
            PedestrianSemaphor.itemconfig(red_pedestrian, fill=red[1])
            PedestrianSemaphor.itemconfig(green_pedestrian, fill=green[0])

        case 'green':
            PedestrianSemaphor.itemconfig(red_pedestrian, fill=red[0])
            PedestrianSemaphor.itemconfig(green_pedestrian, fill=green[1])

        case 'off':
            PedestrianSemaphor.itemconfig(red_pedestrian, fill=red[0])
            PedestrianSemaphor.itemconfig(green_pedestrian, fill=green[0])

        case _:
            PedestrianSemaphor.itemconfig(red_pedestrian, fill=red[0])
            PedestrianSemaphor.itemconfig(green_pedestrian, fill=green[0])

def check_work_mode():
    current_time = datetime.now().time()
    current_time = datetime(2024,11,25,5,23,21)
    if current_time.hour >= 22 or current_time.hour <= 6:
        return work_mode[0]
    else:
        return work_mode[1]

def night_lights_cycle():
    global step_night
    global step_day
    global work_mode
    if work_mode != 'night':
        b_pedestrian.config(state="active")
        step_night = 0
        step_day = 7
        work_mode = 'night'
        night_lights()

b_switch = tkinter.Button(text="LIGHTS MODE:\n DAY\n\n PRESS TO SWITCH\nTO NIGHT MODE", font=30, fg='white', background='green', height=10, width=20, command=night_lights_cycle)
b_switch.place(x=600, y=50)

def day_lights_cycle():
    global step_day
    global step_night
    global work_mode
    if work_mode != 'day' or step_day == 0:
        step_day = 0
        step_night = 2
        work_mode = 'day'
        day_lights()

def day_lights():
    global step_day
    print(f"Timer tick,step_day = {step_day}")
    match step_day:
        case 0:
            config_semaphors_traffic('green')
            config_semaphors_pedestrian('red')
        case 1:
            config_semaphors_traffic('yellow')
            config_semaphors_pedestrian('red')
        case 2:
            config_semaphors_traffic('red')
            config_semaphors_pedestrian('red')
        case 3:
            config_semaphors_traffic('red')
            config_semaphors_pedestrian('green')
        case 4:
            config_semaphors_traffic('red')
            config_semaphors_pedestrian('red')
        case 5:
            config_semaphors_traffic('red yellow')
            config_semaphors_pedestrian('red')
        case 6:
            config_semaphors_traffic('green')
            config_semaphors_pedestrian('red')

    if step_day > 5:
        b_pedestrian.config(state="active")
        step_day = 0
    else:
        root.after(lights_interval_day[step_day], day_lights)
        step_day = step_day + 1

b_pedestrian = tkinter.Button(text="PRESS\nTHE\nBUTTON", font=30, background='yellow', height=10, width=20, command = day_lights_cycle)
b_pedestrian.place(x=600, y=250)

#sequence flag checks if the daylight sequence is being executed
sequence_flag = False
def night_lights():
    global step_night
    print(f"Timer tick,step_night = {step_night}")
    match step_night:
        case 0:
            config_semaphors_traffic('yellow')
            config_semaphors_pedestrian('off')
            root.after(lights_interval_night[step_night], night_lights)
            step_night = 1
        case 1:
            config_semaphors_traffic('off')
            config_semaphors_pedestrian('off')
            root.after(lights_interval_night[step_night], night_lights)
            step_night = 0

def on_closing():
    """Handle the window close event."""
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        stop_thread = True
        root.destroy()  # Close the window

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()