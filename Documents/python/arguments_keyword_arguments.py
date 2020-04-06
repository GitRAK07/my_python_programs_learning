#argument and keyword arguments:
def func(*args):
    print(*args)
    print(args)
    return sum(args)

print(func(1,2,3,4,5))
#Keyword arguments
def func_kw(*args,**kwargs):
    print(*args)
    print(args)
    print(kwargs)
    s=0
    for i in kwargs.values():
     s+=i
    return sum(args)+s

print(func_kw(1,2,3,4,5,a=40,b=2))