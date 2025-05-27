#write a program to clear the clutter inside a folder in your computer

import os

files=os.listdir("cluttered")
i=1
for file in files:
    if file.endswith(".jpg"):
        print(file)
        os.rename(f"cluttered/{file}",f"cluttered/{i}.jpg")
        i=i+1