my_list=[1,2,3]
your_list=['4','5','6']
another_list=(6,7,8,9)

print(tuple(zip(my_list,your_list,another_list)))

###Reduce function

from functools import reduce
def accumalator(acc,item):
    acc+=item
    print(acc)
    return acc

print("The accumlator returned as below:")
print(reduce(accumalator,my_list,0))
