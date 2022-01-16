import time
import Tkinter as tk

class Application(tk.Frame):
    quit=False

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()

        f = open('userData.txt','r')
        i=0
        arr=f.readlines()
        PersonList = [None] * len(arr)
        f.seek(0)
        for li in f:
            PersonList[i]=li[13:index_of_nth(li,',',2)]
            i+=1
        f.close()

        #User Interaction
        self.selectedOption = tk.StringVar()
        self.selectedOption.set(PersonList[0])
        self.selectedOption.trace('w', self.callback)
        self.om = tk.OptionMenu(self, self.selectedOption, *PersonList)
        self.om.grid(row=0,column=0, columnspan=2,sticky='WE')

        self.input = tk.Entry(self)
        self.input.grid(row=1, column=0, columnspan=2,sticky='WE')
        self.input.insert(1,"Please only numbers")
        self.quitButton = tk.Button(self, text='Quit', command=self.quitTrue)
        self.quitButton.grid(row=2,column=0)
        self.enterButton = tk.Button(self, text='Enter', command=self.saveText)
        self.enterButton.grid(row=2,column=1)
        self.text = tk.Text(self, height=3, width=41, wrap='word',highlightthickness=1)
        self.text.grid(row=3,column=0,columnspan=2)
        self.text.insert('insert',getDocNotes(getNumber_fromUser(self.selectedOption.get())))

        self.drawWidgets()

    def callback(self, *args):
        #print 'switch'
        self.text.delete(1.0, 'end')
        self.text.insert('insert',getDocNotes(getNumber_fromUser(self.selectedOption.get())))

    def clearWidgets(self):
        self.name.grid_remove()
        self.phone.grid_remove()
        self.appTime.grid_remove()
        self.waitTime.grid_remove()

    def drawWidgets(self):
        #User output
        self.name = tk.Label(self, text='Name: '+self.selectedOption.get())
        self.name.grid(row=4,column=0, columnspan=2, sticky='W')
        self.phone = tk.Label(self, text='Phone: +'+str(getNumber_fromUser(self.selectedOption.get())))
        self.phone.grid(row=5,column=0, columnspan=2, sticky='W')
        self.appTime = tk.Label(self, text='Appointment Time: '+str(getPrettyAppTime(getNumber_fromUser(self.selectedOption.get()))))
        #print '[selectedOption]'+self.selectedOption.get()
        self.appTime.grid(row=6,column=0, columnspan=2, sticky='W')
        self.waitTime = tk.Label(self, text='Time to Appointment: '+str(getWaitTime(getNumber_fromUser(self.selectedOption.get()))))
        self.waitTime.grid(row=7,column=0, columnspan=2, sticky='W')

    def saveText(self):
        addWaitTime(getNumber_fromUser(self.selectedOption.get()), self.input.get())
        setDocNotes(getNumber_fromUser(self.selectedOption.get()), self.text.get('1.0','end-1c'))

    def quitTrue(self):
        self.quit=True

def driver():
    # DRIVER

    # note - to standardize, removed '+' from number, so it will be 1:12

    number='17344183290'
    # number='00000000000'
    # number='11111111111'
    # number='22222222222'
    # number='33333333333'
    # number='44444444444'
    # number='55555555555'
    # number='66666666666'
    # number='77777777777'
    # number='88888888888'
    # number='99999999999'

    if (inUserData(number)): # return user
        print('==================================')
        print(msgReturnUser(number))
        print('==================================')
    else: # new user
        print('==================================')
        setNewNumber(number)
        print('Prompt name: ')
        setNewName(raw_input(),number)
        setNewAppTime() # currently set to autocalculate
        setNewDocNotes(number)
        print(msgNewUser(number))
        print('==================================')

    DocApp = Application()
    DocApp.master.title('Doctor Application')
    # DocApp.mainloop()
    while True:
        time.sleep(.1)
        DocApp.update()
        DocApp.update_idletasks()
        DocApp.clearWidgets()
        DocApp.drawWidgets()
        if (DocApp.quit):
            break

    # DRIVER END

# Retrieving Data

def inUserData(n):
    f = open("userData.txt", 'r')
    for line in f: #'looping over file object' - print(line) will print that line 
        if (line[1:12] == n):
            f.close()
            return True
    f.close()
    return False

def getNumber(i): # i=line number (marked in txt file - start at 1)
    f = open("userData.txt", 'r')
    line = f.readlines()
    foo = line[i-1] # now i refers to line number in txt file
    f.close()
    return foo[1:12]

def getUser(n):
    f = open("userData.txt", 'r')
    for line in f:
        #print('[getUser](line[1:12])'+line[1:12])
        #print('[getUser](n)'+str(n))
        if (line[1:12] == str(n)):
            f.close()
            return line[13:index_of_nth(line,',',2)]
    f.close()
    return 'default'

def getAppTime(n): # returns string
    f = open("userData.txt", 'r')
    for line in f:
        if (line[1:12] == n):
            f.close()
            return line[index_of_nth(line,',',2)+1:index_of_nth(line,',',3)]
    f.close()
    return 999

def getDocNotes(n):
    f = open("userData.txt", 'r')
    for line in f:
        if (line[1:12] == n):
            f.close()
            return line[index_of_nth(line,',',3)+1:index_of_nth(line,',',4)]
    f.close()
    return 'default'

def getPrettyAppTime(n):
    return str(time.asctime(time.localtime(int(getAppTime(n)))))

def getWaitTime(n): # returns in minutes(ticks)
    appTime=getAppTime(n)
    return ((float(appTime))-time.time())/60

def getNumber_fromUser(username):
    f = open("userData.txt", 'r')
    for line in f:
        if (line[index_of_nth(line,',',1)+1:index_of_nth(line,',',2)] == username):
            f.close()
            return line[1:12]
    f.close()
    return 0

# Modify Data

def addWaitTime(n, time):
    #gets wait time, and uses it to change app time to correct amount by wait time in repsect to current time
    f = open('userData.txt','r')
    arr = f.readlines()
    time = str(int(getAppTime(n))+int(time)*60)
    i=0
    for line in arr:
        if (line[1:12] == n):
            arr[i]=line[0:index_of_nth(line,',',2)]+','+time+line[index_of_nth(line,',',3)]+'\n'
        i+=1
    f.close()
    f = open('userData.txt','w')
    for line in arr:
        f.write(line)
    f.close()

def setDocNotes(n, notes):
    f = open('userData.txt','r')
    arr = f.readlines()
    i=0
    for line in arr:
        if (line[1:12] == n):
            arr[i]=line[:index_of_nth(line,',',3)]+','+notes.strip('\n')+line[index_of_nth(line,',',4):].rstrip()+','
        i+=1
    f.close()
    f = open('userData.txt','w')
    for line in arr:
        f.write(line)
    f.close()

# Record New User (triggered by new number)

def setNewNumber(n):
    f = open('userData.txt','r')
    arr = f.readlines()
    f.close()
    f = open('userData.txt','a')
    if (len(arr)==0):
        f.write('+'+str(n)+',')
    else:
        f.write('\n+'+str(n)+',')
    f.close()

def setNewName(username, n):
    f = open('userData.txt','a')
    f.write(str(username)+',')
    f.close()

def setNewAppTime(): # sets for 5 minutes later
    #waitTime=input("USER WAITTIME: ")
    waitTime=int(time.time()+300)
    f = open('userData.txt','a')
    f.write(str(waitTime)+',')
    f.close()

def setNewDocNotes(n):
    f = open('userData.txt','a')
    f.write(',')
    f.close()

# Responding

def msgReturnUser(n):
    username = getUser(n)
    waitTime = getWaitTime(n)
    return 'Welcome back '+str(username)+'!\nAppointment: '+getPrettyAppTime(n)+'\nTime until appointment: '+str(getWaitTime(n))+' minutes'

def msgNewUser(n):
    #
    return 'Welcome to Huron\'s Hospital '+n+' . What is your name?'

# Utility

def index_of_nth(haystack, needle, n):
    index = haystack.find(needle)
    while index >= 0 and n > 1:
        index = haystack.find(needle, index+len(needle))
        n -= 1
    return index

driver()

# Saved userData.txt test values
'''

+00000000000,Fugi,1547588944.31,Their name is Fugi. And now their notes are updated.kjads.,
+11111111111,Dan,1547594470.52,Their name is Dan,
+22222222222,Fas,1547596869.32,Their name is Fas.,
+33333333333,Gerl,1547596881.99,Their name is Gerl,
+44444444444,Carl,1547596893.23,Their name is Carl,
+55555555555,Hob,1547596902.65,Their name is Hob. He has a wart.,
+66666666666,Koop,1547596911.16,Their name is Koop,
+77777777777,Sheep,1547596922.84,Their name is Fugi.,
+88888888888,Larry,1547596934.87,Their name is Larry,
+99999999999,Jerald,1547596947.01,Their name is Jerald,
'''