
#with Blocks

#Option 1
file = open("story.txt")
file.read()
file.close()

#file.closed #true

#the idea from reading_files.py file

#Option 2
with open("story.txt") as file:
    file.read()

#file.closed #true

#this is a slighty different syntax that basically closes the file automatically, after the code inside the block runs