# BLOCK !/usr/bin/env python
import Tkinter

class DoctorApplication(Tkinter.Frame):
    def __init__(self, master=None):
        Tkinter.Frame.__init__(self, master)
        self.grid()

        #User Interaction
        PersonList = [getUser(getNumber(2)),
        getUser(getNumber(3)),
        getUser(getNumber(4)),
        getUser(getNumber(5)),
        getUser(getNumber(6)),
        getUser(getNumber(7)),
        getUser(getNumber(8)),
        getUser(getNumber(9)),
        getUser(getNumber(10)),
        getUser(getNumber(11))]
        self.selectedOption = Tkinter.StringVar()
        self.selectedOption.set(PersonList[0])
        self.om = Tkinter.OptionMenu(self, self.selectedOption, *PersonList)
        self.om.grid(row=0,column=0, columnspan=2,sticky='W')

        self.input = Tkinter.Entry(self)
        self.input.grid(row=1, column=0, columnspan=2)
        self.input.insert(1,"Default Text")
        self.quitButton = Tkinter.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid(row=2,column=0)
        self.actionButton = Tkinter.Button(self, text='Action', command=self.printTest)
        self.actionButton.grid(row=2,column=1)

        self.drawWidgets()

    def drawWidgets(self):
        #User output
        self.name = Tkinter.Label(self, text=self.selectedOption.get())
        self.name.grid(row=3,column=0, columnspan=2, sticky='W')
        self.phone = Tkinter.Label(self, text=getNumber_fromUser(selectedOption.get()))
        self.phone.grid(row=4,column=0, columnspan=2, sticky='W')
        self.appTime = Tkinter.Label(self, text='Appointment Time:')
        self.appTime.grid(row=5,column=0, columnspan=2, sticky='W')

    def printTest(self):
        print(self.getUserInput())
        print(self.input.get())

    def getUserInput(self):
        return self.input.get()

def getNumber(i): #i=line number (marked in txt file - start at 1)
    f = open("userData.txt", 'r')
    line = f.readlines()
    foo = line[i-1] # now i refers to line number in txt file
    f.close()
    return foo[1:12]

def getNumber_fromUser(username):
    f = open("userData.txt", 'r')
    skippedOnce=False
    for line in f:
        print('[getNumber_fromUser]')
        if (skippedOnce==True and line[13:line.index(',',line.index(',',13))] == username):
            f.close()
            return line[1:12]
        skippedOnce=True
    f.close()
    return 0

def getUser(n):
    f = open("userData.txt", 'r')
    for line in f:
        #print('[getUser](line[0:12])'+line[0:12])
        #print('[getUser](n)'+str(n))
        if (line[1:12] == str(n)):
            f.close()
            return line[13:line.index(',',line.index(',',13))]
    f.close()
    return 'default'

DocApp = DoctorApplication()
DocApp.master.title('Doctor Application')
#DocApp.mainloop()
while True:
    time.sleep(3)
    DocApp.update()
    DocApp.update_idletasks()
    DocApp.drawWidgets()

#.cget() gets settings of widget
#.config() change any option