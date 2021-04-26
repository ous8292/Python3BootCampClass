


numbers = [1, 2, 3, 4, 5, 6]

even = [num for num in numbers if num % 2 == 0]

odd = [num for num in numbers if num % 2 != 0]

#using else keyword
with_else = [num*2 if num % 2 == 0 else num/2 for num in numbers]

#using in keyword
with_vowles = "this is so much fun!"
''.join(char for char in with_vowles if char not in "aeiou") #ths s s mch fn!