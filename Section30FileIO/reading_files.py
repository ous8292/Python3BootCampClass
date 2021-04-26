file = open("story.txt")
file.read() #after this is run cursor is at the end of the story


file.seek(0) #now the cursor goes back to the start
#you can pass in any number.. they stand for the first index of the file


file.readline() #reads only the first line of chartacters.. still moves the cursor to the end of the first line

file.readlines() #returns all the lines, but puts them as a list

#these connections are open.. if you make a change in the file.. it will contnue to read it if you use file read
file.close() #closes the file

