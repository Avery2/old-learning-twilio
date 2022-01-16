# BLOCK !/usr/bin/env python
import Tkinter

class Application(Tkinter.Frame):
    def __init__(self, master=None):
        Tkinter.Frame.__init__(self, master)
        self.grid()

        optionList = ['train', 'plane', 'boat']
        self.v = Tkinter.StringVar()
        self.v.set(optionList[0])
        self.om = Tkinter.OptionMenu(self, self.v, *optionList)
        self.om.grid(row=0,column=0, columnspan=2)

        #self.input = Tkinter.Entry(self)
        #self.input.grid(row=0, column=0, columnspan=2)
        #self.input.insert(0,"Default Text")
        self.quitButton = Tkinter.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid(row=1,column=0)
        self.actionButton = Tkinter.Button(self, text='Action', command=self.printTest)
        self.actionButton.grid(row=1,column=1)

        #User output
        self.name = Tkinter.Label(self, text='Name:')
        self.name.grid(row=2,column=0, columnspan=2, sticky='W')
        self.phone = Tkinter.Label(self, text='Phone:')
        self.phone.grid(row=3,column=0, columnspan=2, sticky='W')
        self.appTime = Tkinter.Label(self, text='Appointment Time:')
        self.appTime.grid(row=4,column=0, columnspan=2, sticky='W')
        #self.read = Tkinter.Text(height=20, width=40)
        #self.read.grid(row=2, column=0)
        #self.read.insert(self,"Default text.")

    def printTest(self):
        print(self.getUserInput())
        print(self.input.get())

    def getUserInput(self):
        return self.input.get()

app = Application()
app.master.title('Doctor Application')
app.mainloop()

#.cget() gets settings of widget
#.config() change any option