'''
file input\output
'''
import os

with open("mydata.txt", mode = "w", encoding = "utf-8") as myFile:
    myFile.write("Some random text\nMore random text\nEven more random txt")

with open("mydata.txt", encoding = "utf-8") as myFile:
    print(myFile.read())

os.rename("mydata.txt", "mydata2.txt")

os.remove("mydata2.txt")

os.mkdir("mydir")

print("Current Directory: ", os.getcwd())
