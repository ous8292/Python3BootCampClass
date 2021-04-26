

#nested lists
#lists that contain any kind of element, even other lits!

nested_lists = [[1,2,3], [4,5,6], [7,8,9]]

print(nested_lists[0][1])
print(nested_lists[1])


for lis in nested_lists:
    print(lis)

for l in nested_lists:
    for val in l:
        print(val)


[[print(val) for val in l] for l in nested_lists]


#another example

board = [[num for num in range(1,4)] for val in range(1,4)]
print(board) #[[1,2,3], [1,2,3], [1,2,3]]

var = [["x" if num % 2 != 0 else "O" for num in range(1, 4)] for val in range(1, 4)]
print(var)