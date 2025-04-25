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

# f=open('myfile2.txt','a')

# f.write('how are you')

# f.close()

# #another method by using with---------------------------//////////////////////////////////
# with open('myfile2.txt','a') as f:

#     f.write("use of with")


#readline method is used to read file line by line////////////////////////////////////////

# f=open('myfile.txt','r')
# while True:
#     line=f.readline()
#     if not line:
#         break
#     print (line)

#another use case////////////////////////////////////////////////////////////////////////////////

# f=open('myfile3.txt','r')
# i=0
# while True:
#     i=i+1
#     line=f.readline()
#     if not line:
#         break
#     m1=int(line.split(",")[0])
#     m3=int(line.split(",")[2])
#     m2=int(line.split(",")[1])
#     print(f"marks of student {i} in maths is: {m1*2}")
#     print(f"marks of student {i} in English is: {m2*2}")
#     print(f"marks of student {i} in Computer is: {m3*2}")

    
#     print(line)

 #wrtieline method is used to write items of list to the file////////////////////////
# f=open('myfile3.txt','w')
# lines=['line 1\n','line 2\n','line 3\n']
# f.writelines(lines)
# f.close()


#seek() and tell()//////////////////////////////////////////////////////////////////////////////////

# with open('file.txt','r') as f:
#     print(type(f))
#     f.seek(10) #reads file from 10th character position

#     print(f.tell()) #tells to which point fn is seeked
#     data=f.read(5) #reads 5 bytes from 10th character position
#     print(data)


#truncate()
with open('file.txt','w') as f:
    f.write('Hello by truncate')
    f.truncate(5) #tells there should be only 5 chars in file

with open('file.txt','r') as f:
    print(f.read())