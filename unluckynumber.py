# Exercise
#Loop through 1-20 (inclusive)
#for 4 and 13, print "x is unlucky"
#for even numbers, print "x is even"
# for odd numbers, print "x is odd"



for num in range(1, 21):
    if num == 4 or num == 13:
        print(str(num) + "is unlucky")
    if num % 2 == 0:
        print(str(num) + "is even")
    else:
        print(str(num) + "is odd")


# to find how a number is even we use % modulo (the remainder operator
# num % 2 == 0, if number does not have a remainder.. then it's even
# for unlucky part:
#cant make a seperate if statement since it will print 2 numbers
#elif must be used on top, since it will first check if 4 is even, prints 13 as unlucky due to 13 being odd
