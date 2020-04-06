def multiply_by2(arr):
    new=[]
    for item in arr:
        new.append(item*2)
    return new

print(multiply_by2([1,2,3]))

#map function #Compare with above program without map
my_list=[6,4,2]
def divide_by2(arr):
    return arr/2
print(list(map(divide_by2,my_list))) #my_list argument will not get changed
print(my_list)

#NOTE: map doesn't actually call the function . You can see there is no () in it