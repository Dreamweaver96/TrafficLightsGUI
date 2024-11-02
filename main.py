import tkinter

root = tkinter.Tk()
root.geometry('900x700')


'''Lights being on or off are determined by fill parameters of each ndex number of tuples containing colours. 
0 - light is off
1 - light is on
Each colour has it's own two-element tuple declared below.
'''

green = ('#175700','#3DE500')
yellow = ('#957700','#F9C700')
red = ('#7D0000','#F90000')

TrafficSemaphor = tkinter.Canvas(height=450, width=200, bg='black')
TrafficSemaphor.place(x=100, y=100)
#1a.W normalnym trybie pracy światła dla samochodu są wyłączone, co oznacza to samo, co światło zielone
green_traffic = TrafficSemaphor.create_oval(50, 25, 150, 125, fill=green[1])
yellow_traffic = TrafficSemaphor.create_oval(50, 175, 150, 275, fill=yellow[0])
red_traffic = TrafficSemaphor.create_oval(50, 325, 150, 425, fill=red[0])

PedestrianSemaphor = tkinter.Canvas(height=300, width=200, bg='black')
PedestrianSemaphor.place(x=350, y=175)
#1b.W normalnym trybie pracy dla pieszego świeci się światło czerwone
green_pedestrian = PedestrianSemaphor.create_oval(50, 25, 150, 125, fill=green[0])
red_pedestrian = PedestrianSemaphor.create_oval(50, 175, 150, 275, fill=red[1])

#2.Po naciśnięciu przez pieszego przycisku
# 2.1.Dla samochodu załącza się światło zielone (na 2 Sekundy)
def step_one():
    #setting b1 state to disabled to avoid multiple clicks and thus function calls
    b1.config(state="disabled")
    root.after(2000, step_two)

#2.2.Dla samochodu załącza się światło pomarańczowe (na 2 Sekundy)
def step_two():
    TrafficSemaphor.itemconfig(green_traffic, fill=green[0])
    TrafficSemaphor.itemconfig(yellow_traffic, fill=yellow[1])
    root.after(2000, step_three)

#2.3.Dla samochodu załącza się światło czerwone (świeci przez 2 Sekundy)
def step_three():
    TrafficSemaphor.itemconfig(yellow_traffic, fill=yellow[0])
    TrafficSemaphor.itemconfig(red_traffic, fill=red[1])
    root.after(2000, step_four)

#2.4.Dla pieszego załącza się światło zielone (na 10 Sekund), równolegle ze światłem czerwonym dla samochodu
def step_four():
    PedestrianSemaphor.itemconfig(red_pedestrian, fill=red[0])
    PedestrianSemaphor.itemconfig(green_pedestrian, fill=green[1])
    root.after(10000, step_five)

#2.5.Dla pieszego załącza się światło czerwone (na 2 Sekundy)
def step_five():
    PedestrianSemaphor.itemconfig(green_pedestrian, fill=green[0])
    PedestrianSemaphor.itemconfig(red_pedestrian, fill=red[1])
    root.after(2000,step_six)

#2.6.Dla samochodu załączają się światła czerwone i pomarańczowe (na 2 Sekundy)
def step_six():
    TrafficSemaphor.itemconfig(yellow_traffic, fill=yellow[1])
    root.after(2000, step_seven)

    #2.7.Dla samochodu załącza się światło zielone (na 10 Sekund)
def step_seven():
    TrafficSemaphor.itemconfig(yellow_traffic, fill=yellow[0])
    TrafficSemaphor.itemconfig(red_traffic, fill=red[0])
    TrafficSemaphor.itemconfig(green_traffic, fill=green[1])
    #setting b1 state to clickable again
    b1.config(state="normal")
    root.after(10000)
    #2.8.Światło zielone dla samochodu gaśnie

b1 = tkinter.Button(text="PRESS\nTHE\nBUTTON", font=30, background='yellow', height=10, width=20, command=step_one)
b1.place(x=600, y=250)

root.mainloop()