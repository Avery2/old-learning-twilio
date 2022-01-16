# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio import twiml
import time
 
app = Flask(__name__)
 
username = 'error'
step = 0
runTimeError = 'Error Message Red'
 
@app.route("/sms", methods=['GET', 'POST'])
# DRIVER METHOD
def sms_ahoy_reply():
	# Twilio Stuff
    number = request.form['From']
    # Note number being changed to remove '+' but if twilio uses number for value, change back and make diff var
    number = number[1:]
    message_body = request.form['Body']
    global step
    resp = MessagingResponse()
   
    # Response Handling

    # Return User
    if (inUserData(number) and step==0):
        resp.message('Welcome back '+str(getUser(number))+'!\nAppointment: '+getPrettyAppTime(number)+'\nTime until appointment: '+str(getWaitTime(number))+' minutes')
        return str(resp)
 
 	# New User Start
    if step==0: # Save Number, Prompt to get username
    	setNewNumber(number)
        resp.message('Welcome to Huron\'s Hospital '+number+' . What is your name?')
        step+=1
        return str(resp)

    if step==1:
    	setNewName(message_body, number)
    	setNewAppTime()
    	setNewDocNotes('')
        resp.message('Thanks '+getUser(number)+',\nYour appointment is at '+getPrettyAppTime(number)+"\nType anything to get updated info.")
        step=0
        return str(resp)

    print("Error out of Step: "+str(step)) # Error message
    return str(resp)
# END OF DRIVER METHOD

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

# Utility

def index_of_nth(haystack, needle, n):
    index = haystack.find(needle)
    while index >= 0 and n > 1:
        index = haystack.find(needle, index+len(needle))
        n -= 1
    return index

# Somthing I'm not to mess with
if __name__ == "__main__":
    app.run(debug=True)