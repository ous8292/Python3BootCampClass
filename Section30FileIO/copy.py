#copy of a file
def copy(file_name, new_file_name):
    with open(file_name) as file:
        text = file.read()

    with open(new_file_name, "w") as new_file:
        new_file.write(text)







#reversing a copy of a file
def copy_and_reverse(file_name, new_file_name):
    with open(file_name) as file:
        text = file.read()

    with open(new_file_name) as file:
        new_file_name.write(text[::-1]) #text[::-1] reverses the string


