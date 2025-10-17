from hsDecoder import decode
from tkinter import *
import json

def verify():
    code =codeTxt.get()
    genuine,score,mode = decode(code)
    if genuine:
        outputLbl1.config(text='Genuine!')
        outputLbl2.config(text='Score: '+str(score))
        scoreVar.set(int(score))
        outputLbl3.config(text="Mode: "+mode)
        modeVar.set(mode)
    else:
        outputLbl1.config(text='Invalid')
        outputLbl2.config(text='This score has not been recorded')
        outputLbl3.config(text='If this is a bug contact developer')
def view():
    viewGUI = Tk()
    viewGUI.title('Leaderboard')
    def show(x):
        listElement.delete(0,END)
        mode = dropdownVar.get()
        f = open('HSdata.txt','r')
        if mode == 'easy':
            index = 0
        elif mode == 'normal':
            index = 1
        elif mode == 'hard':
            index = 2
        elif mode == 'impossible':
            index = 3
        dictionary = json.load(f)[index]
        for key in dictionary:
            stringInsert = f'{key}: {dictionary.get(key)}'
            listElement.insert(0,stringInsert)
    dropdownVar = StringVar(viewGUI)
    options = ['easy','normal','hard','impossible']
    dDropdown = OptionMenu(viewGUI,dropdownVar,*options,command=show)
    dDropdown.grid(column=0,row=0)
    listElement = Listbox(viewGUI,height=20)
    listElement.grid(column=0,row=1)
    viewGUI.mainloop()
def add():
    def confirm():
        with open('HSdata.txt','r') as f:
            namedict = json.load(f)
        mode = modeVar.get()
        if mode == 'easy':
            index = 0
        elif mode == 'normal':
            index = 1
        elif mode == 'hard':
            index = 2
        elif mode == 'impossible':
            index = 3
        namedict[index].update({nametxt.get():scoreVar.get()})
        sortedName = sorted(namedict[index].items(), key=lambda x:x[1], reverse=False)
        namedict[index] = dict(sortedName)
        nameGui.destroy()
        with open('HSdata.txt','w') as f:
            json.dump(namedict,f)
    nameGui = Tk()
    nameGui.title('Enter Name: ')
    nametxt = Entry(nameGui, width=40)
    nametxt.grid(column=0,row=0)
    nameBtn = Button(nameGui, text="Add",command=confirm)
    nameBtn.grid(column=0,row=1)
    nameGui.mainloop()
    f.close()

try:
    f = open('HSdata.txt','r')
except:
    f = open('HSdata.txt','w')
    json.dump([{},{},{},{}],f)
f.close()

gui = Tk()
gui.title('Leaderboard')
scoreVar = IntVar(gui)
modeVar = StringVar(gui)
codeTxt = Entry(gui,width=40)
codeTxt.grid(column=0,row=0)
verifyBtn = Button(gui,text="Verify",command=verify)
verifyBtn.grid(column=1,row=0)
infoLbl = Label(gui,text="Your result is...")
infoLbl.grid(column=0,row=1)
outputLbl1 = Label(gui,text="")
outputLbl1.grid(column=0,row=2)
outputLbl2 = Label(gui, text="")
outputLbl2.grid(column=0,row=3)
outputLbl3 = Label(gui, text="")
outputLbl3.grid(column=0,row=4)
addBtn = Button(gui, text='Add Name to Leaderboard',command=add)
addBtn.grid(column=0,row=5)
showBtn = Button(gui, text='View Leaderboards',command=view)
showBtn.grid(column=0,row=6)
gui.mainloop()