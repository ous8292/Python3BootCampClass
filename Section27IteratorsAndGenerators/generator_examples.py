

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

count_up_to(5)