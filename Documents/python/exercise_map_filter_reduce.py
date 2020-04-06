from functools import reduce

my_pets = ['sisi', 'bibi', 'titi', 'carla']
def cap(capi):
    return capi.upper()

print(list(map(cap,my_pets)))
#1 Capitalize all of the pet names and print the list
#my_pets = ['sisi', 'bibi', 'titi', 'carla']


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
print(tuple(zip(my_strings,sorted(my_numbers))))
print(my_numbers)


def score(s):
    return ((s / 100)*100) > 50
scores = [73, 20, 65, 19, 76, 100, 88]
print(list(filter(score,scores)))
#3 Filter the scores that pass over 50%
#scores = [73, 20, 65, 19, 76, 100, 88]

def accumulator(acc, item):
    print (acc,item)
    return acc + item

print(reduce(accumulator, (my_numbers + scores)))
#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
