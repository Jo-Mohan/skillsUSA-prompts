import tkinter as tk
from tkinter import *

m=tk.Tk()
m.title('Contestant ID: 2198, Task 2, Asset Inventory Tracking Program')
m.geometry("400x400")
perYear = 0


def calculate():
    start = float(startVal.get('1.0', 'end'))
    end = float(salvage.get('1.0', 'end'))
    time = int(numYears.get('1.0', 'end'))
    name = assetName.get('1.0', 'end')

    global perYear

    perYear = (start - end) / time
    perYear = round(perYear, 2)

    year = 0
    for i in range(0, time + 1):
        DepSched.insert('end', "Year: " + str(year) + " " )
        DepSched.insert('end', "Current Value $" + str(start)  + " \n")
        year = year + 1
        start = start - perYear
        start = round(start, 2)
    
    DepSched.insert('1.0', "Asset Name " + name + ' :' + " \n ")
     



def resetVals():
    assetName.delete("1.0","end")
    numYears.delete("1.0","end")
    startVal.delete("1.0","end")
    salvage.delete("1.0","end")
    DepSched.delete("1.0","end")
    

    

#Button creations
calc = tk.Button(m, text='Calculate', width=25, command = calculate)
exit = tk.Button(m, text='Exit', width=25, command=m.destroy)
reset = tk.Button(m, text='Reset', width=25, command= resetVals)


#Labels
lAssetName = tk.Label(m, text="Asset Name")
lStartVal = tk.Label(m, text="Starting Price")
lnumYears = tk.Label(m, text="Years to Depreciate")
lSalvage = tk.Label(m, text="Salvage Value")
lDepSched = tk.Label(m, text="Depreciation Schedule")




#Entry Boxes
assetName = Text(m, height = 1)
startVal = Text(m, height = 1)
numYears = Text(m, height = 1)
salvage = Text(m, height = 1)
DepSched = Text(m, height = 10)


#Grid
calc.grid(row=0,column=0)
exit.grid(row=0,column=1)
reset.grid(row=0,column=2)

lAssetName.grid(row=1,column=0)
assetName.grid(row = 1, column = 1)

lStartVal.grid(row=2,column=0)
startVal.grid(row = 2, column = 1)

lnumYears.grid(row=3,column=0)
numYears.grid(row=3,column=1)

lSalvage.grid(row=4,column=0)
salvage.grid(row=4,column=1)

lDepSched.grid(row=7,column=0)
DepSched.grid(row=7,column=1)



m.mainloop()