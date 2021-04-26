
#Writing files


with open("story.txt", "w") as file:
    file.write("Writing to the file is great!\n")
    file.write("another text line!!\n")
    file.write("closing now, goodbye!")


#this over wrote everything.. because of the w flag.. which overwrites everything

#you can also create a new file buy putting the desired file name in

# a - appends to end, previous original
#no control over cursor
# with open("story.txt", "a") as file:
#     file.seek(0)
#     file.write("huzzah!\n")



#r+
with open("story.txt", "a") as file:
    file.write("ADDED using r+ mod")

#r+ always starts at the beginning of the file.. also over writes everything in it's way
#r+ will not create a new file, only edits
