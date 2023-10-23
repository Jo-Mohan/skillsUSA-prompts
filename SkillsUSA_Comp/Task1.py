import tkinter as tk
from tkinter import *

m=tk.Tk()
m.title('Contestant ID: 2198, Task 1, Future Value Calculator Program')
m.geometry("400x400")
final = 1


def calculate():
    p = float(principal.get('1.0', 'end'))
    t = float(numberYears.get('1.0', 'end'))
    r = float(rate.get('1.0', 'end'))

    global final
    if(radio.get() == 1):
        final = p*((1+r/12)**(12*t))

    if(radio.get() == 2):
        final = p*((1+r)**(t))

    final= round(final, 2)
    total.insert('1.0',final)

def resetVals():
    principal.delete("1.0","end")
    numberYears.delete("1.0","end")
    total.delete("1.0","end")
    rate.delete("1.0","end")
    print(radio.get())

    

#Button creations
calc = tk.Button(m, text='Calculate', width=25, command = calculate)
exit = tk.Button(m, text='Exit', width=25, command=m.destroy)
reset = tk.Button(m, text='Reset', width=25, command= resetVals)


#Labels
curVal = tk.Label(m, text="Present Value")
numYears = tk.Label(m, text="Number of Years")
output = tk.Label(m, text="Total")
cType = tk.Label(m, text="Type of Compounding")
lrate = tk.Label(m, text="Interest Rate In Decimal Form")

def select():
    print(radio.get())

#Radio
radio = IntVar()
r1 = Radiobutton(m, text="Monthly",variable = radio, value=1, command = select)
r2 = Radiobutton(m, text="Yearly", variable = radio, value=2, command = select)




#Entry Boxes
principal = Text(m, height = 1)
numberYears = Text(m, height = 1)
total = Text(m, height = 1)
rate = Text(m, height = 1)

#Grid
calc.grid(row=0,column=0)
exit.grid(row=0,column=1)
reset.grid(row=0,column=2)

curVal.grid(row=1,column=0)
principal.grid(row = 1, column = 1)

numYears.grid(row=2,column=0)
numberYears.grid(row=2,column=1)

lrate.grid(row=3,column=0)
rate.grid(row=3,column=1)

cType.grid(row=4,column=0)
r1.grid(row=4,column=1)
r2.grid(row=4,column=2)

output.grid(row=5,column=0)
total.grid(row=5,column=1)



m.mainloop()