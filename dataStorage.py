f = open('database.txt','w') 

#f.write('Hello World')
#f.write('Hello World2')
#f.write('Hello World3')

#print r.readline()
#print r.readline()
#print r.readline()

f.close()
f = open('database.txt','r')

if f.mode == 'r':
	contents =f.read()
	print contents
#Cannot use both at same time, one will end up reading nothing WITHOUT > seek(0)
f.seek(0)

fl = f.readlines()
for x in fl:
	print (x + 'hi')

f.close()


'''

'r'	This is the default mode. It Opens file for reading.
'w'	This Mode Opens file for writing. 
	If file does not exist, it creates a new file.
	If file exists it truncates the file.
'x'	Creates a new file. If file already exists, the operation fails.
'a'	Open file in append mode.
	If file does not exist, it creates a new file.
't'	This is the default mode. It opens in text mode.
'b'	This opens in binary mode.
'+'	This will open a file for reading and writing (updating)

'''


'''header1,header2,header3,header4
x,y,z,m
q,w,e,r
t,y,u,i
o,p,a,s
d,f,g,h'''

'''
username,waitTime,placeInLine
Surya,10,1
Avery,10,2
'''












