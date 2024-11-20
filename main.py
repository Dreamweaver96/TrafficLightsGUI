import tkinter

root = tkinter.Tk()
root.geometry('900x700')

'''Lights being on or off are determined by fill parameters of each index number of tuples containing colours. 
0 - light is off
1 - light is on
Each colour has its own two-element tuple declared below.
'''
green = ('#175700','#3DE500')
yellow = ('#957700','#F9C700')
red = ('#7D0000','#F90000')

#1.In normal operation mode, all lights are turned off.
TrafficSemaphor = tkinter.Canvas(height=450, width=200, bg='black')
TrafficSemaphor.place(x=100, y=100)

red_traffic = TrafficSemaphor.create_oval(50, 25, 150, 125, fill=red[0])
yellow_traffic = TrafficSemaphor.create_oval(50, 175, 150, 275, fill=yellow[0])
green_traffic = TrafficSemaphor.create_oval(50, 325, 150, 425, fill=green[0])

PedestrianSemaphor = tkinter.Canvas(height=300, width=200, bg='black')
PedestrianSemaphor.place(x=350, y=175)
red_pedestrian = PedestrianSemaphor.create_oval(50, 25, 150, 125, fill=red[0])
green_pedestrian = PedestrianSemaphor.create_oval(50, 175, 150, 275, fill=green[0])


def switch_mode():
    global b_switch_state, sequence_flag
    if b_switch_state == 'day':
        b_switch.config(text="LIGHTS MODE:\n NIGHT\n\n PRESS TO SWITCH\nTO DAY MODE", background="blue",fg="yellow")
        b_switch_state = 'night'
        b_pedestrian.config(state="disabled")
    else:
        b_switch.config(text="LIGHTS MODE:\n DAY\n\n PRESS TO SWITCH\nTO NIGHT MODE", background="green", fg="white")
        b_switch_state = 'day'
        if sequence_flag == False:
            b_pedestrian.config(state="normal")


#2. After the pedestrian presses the button:
#2.1. The green light for cars turns on, and the red light for pedestrians turns on (for 2 seconds).

def step_one():
    global sequence_flag
    sequence_flag = True
    # setting b_pedestrian state to disabled to avoid multiple clicks and thus function calls
    b_pedestrian.config(state="disabled")
    TrafficSemaphor.itemconfig(green_traffic, fill=green[1])
    PedestrianSemaphor.itemconfig(red_pedestrian, fill=red[1])
    root.after(2000, step_two)

#2.2. The orange light for cars turns on (for 2 seconds)
def step_two():
    TrafficSemaphor.itemconfig(green_traffic, fill=green[0])
    TrafficSemaphor.itemconfig(yellow_traffic, fill=yellow[1])
    root.after(2000, step_three)

#2.3. The red light for cars turns on (for 2 seconds).
def step_three():
    TrafficSemaphor.itemconfig(yellow_traffic, fill=yellow[0])
    TrafficSemaphor.itemconfig(red_traffic, fill=red[1])
    root.after(2000, step_four)

#2.4. The green light for pedestrians turns on (for 10 seconds) simultaneously with the red light for cars.
def step_four():
    PedestrianSemaphor.itemconfig(red_pedestrian, fill=red[0])
    PedestrianSemaphor.itemconfig(green_pedestrian, fill=green[1])
    root.after(10000, step_five)

#2.5. The red light for pedestrians turns on (for 2 seconds).
def step_five():
    PedestrianSemaphor.itemconfig(green_pedestrian, fill=green[0])
    PedestrianSemaphor.itemconfig(red_pedestrian, fill=red[1])
    root.after(2000,step_six)

#2.6. The red and orange lights for cars turn on (for 2 seconds).
def step_six():
    TrafficSemaphor.itemconfig(yellow_traffic, fill=yellow[1])
    root.after(2000, step_seven)

#2.7. The green light for cars turns on (for 10 seconds).
def step_seven():
    TrafficSemaphor.itemconfig(yellow_traffic, fill=yellow[0])
    TrafficSemaphor.itemconfig(red_traffic, fill=red[0])
    TrafficSemaphor.itemconfig(green_traffic, fill=green[1])
    root.after(10000, step_eight)

def step_eight():
#2.8. Both the green light for cars and the red light for pedestrians turn off.
    TrafficSemaphor.itemconfig(green_traffic, fill=green[0])
    PedestrianSemaphor.itemconfig(red_pedestrian, fill=red[0])
    global sequence_flag
    sequence_flag = False
    global b_switch_state
    # setting b_pedestrian state to clickable again as the sequence ends. If block is necessary to block enabling in night mode.
    if b_switch_state == "day":
        b_pedestrian.config(state="normal")


b_switch = tkinter.Button(text="LIGHTS MODE:\n DAY\n\n PRESS TO SWITCH\nTO NIGHT MODE", font=30, fg='white', background='green', height=10, width=20, command=switch_mode)
b_switch.place(x=600, y=50)
#default state of the b_switch button
b_switch_state = 'day'


b_pedestrian = tkinter.Button(text="PRESS\nTHE\nBUTTON", font=30, background='yellow', height=10, width=20, command=step_one)
b_pedestrian.place(x=600, y=250)

#sequence flag checks if the daylight sequence is being executed
sequence_flag = False
def night_lights():
    global b_switch_state, sequence_flag
    if b_switch_state == 'night':
        if sequence_flag == False:
            TrafficSemaphor.itemconfig(yellow_traffic, fill=yellow[1])
            root.after(500, lambda: TrafficSemaphor.itemconfig(yellow_traffic, fill=yellow[0]))
    root.after(1000,night_lights)
night_lights()

root.mainloop()