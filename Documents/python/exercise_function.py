def even(*args):
    high=[]
    for i in args:
     if i %2 == 0:
         high.append(i)
    return max(high)
     

print(even(2,3,6,8,23,54365,56,3,456,123121))