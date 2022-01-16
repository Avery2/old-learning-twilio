import time

print(time.time()) #Number of ticks since 12:00am, January 1, 1970
localtime = time.asctime( time.localtime(time.time()) )
print(localtime)
name="Surya"
time=input(name+": Time: ")
print("Saved "+name+" appointment for "+str(time)) 

n='+17344183290'
f = open("userData.txt", 'r')
fl = f.readlines()
if f.read() == None:
	print(False)
for x in fl:
    print (str(x[0:12]==n))
for x in fl:
    print (str(x[0:12]))