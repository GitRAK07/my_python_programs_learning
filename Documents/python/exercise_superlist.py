class SuperList(list): # list method can be inherited to the class like this.
  def __len__(self):
    return 1000

super_list1 = SuperList()

print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print(issubclass(list, object))




class SuperLists():
    def __init__(self, list1):
        self.list1 = list1
    
sl=SuperLists(['A','B','C'])
print(sl.list1)
print(len(sl.list1))
sl.list1.append('D')
print(sl.list1)
print(sl.list1[2])