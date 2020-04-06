my_list=[1,2,3,4]
def odd(number):
    return number % 2 != 0

print(list(filter(odd,my_list)))