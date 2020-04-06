class MyownClass:
    membership=True
    def __init__(self, name,age):
      self.name=name #attributes
      self.age=age
      print(self.name,self.age)
      print(name,age)

class1= MyownClass('Anand',23)
print(class1)
print(class1.name,class1.age)
print(MyownClass.membership)
