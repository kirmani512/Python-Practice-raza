#file handling in python has several functions for creating, reading, updating and deleting files
#the function for working with files is open() function, it takes two parameters i.e filename and mode
#r for read this is default mode
#w for write
#a for append i.e opens a file for appending and creates the file if not exists
#x creates the file and returns an error if already exists
#rb this will opens file as binary mode and read it i.e jpg or etc
#rt this will opens file as text mode and read it



#reading a file------------------------------------------------///////////////////////////////
# f=open('myfile.txt','r')

# text=f.read()

# print(text)

#this wil create the new file

# f=open('myfile2.txt','w')

# text=f.read()

# print(text)




#writing a file----------------------------////////////////////////////////

# f=open('myfile2.txt','w')

# f.write('Hello')

# f.close()

#to append data

f=open('myfile2.txt','a')

f.write('how are you')

f.close()

#another method by using with---------------------------//////////////////////////////////
with open('myfile2.txt','a') as f:

    f.write("use of with")
