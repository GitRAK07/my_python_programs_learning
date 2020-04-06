class User():
    def sigin(self):
        print ("Signed in")

class Wizard():
    def __init__(self,name,power):
     self.name=name
     self.power=power
     print ("hi")

    def attack(self):
      print(f"User '{self.name}' has '{self.power}' no. of powers'")    

class Archer():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("bye")

    def details(self):
     print(f"The user '{self.name}' is of age: '{self.age}")

class Hybrdid(Wizard,Archer):    #Definition of Hybrid Inheritance
     def __init__(self, name, age , power):
          Archer.__init__(self,name, age)
          Wizard.__init__(self,name,power)
print(Hybrdid.mro()) # shows the method resolution order to know the order of inheritance
h=Hybrdid('Kumar',20,100)     #Definition of Hybrid Inheritance
print(h.attack()) #Definition of Hybrid Inheritance
print(h.details()) #Definition of Hybrid Inheritance
w=Wizard('Anand', 100)
a=Archer('Anand',29)
print(w.attack())
print(a.details())
        
        
        