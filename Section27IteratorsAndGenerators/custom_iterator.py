#in for loops loop calls iter() being called on object, that returns the iterator, which then the for loop keeps calling the next() on
# until it reaches the end

class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration


c = Counter(0,10)
iter(c)

for x in Counter(0,10):
    print(x)