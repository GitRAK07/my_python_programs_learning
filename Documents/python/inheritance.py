
class User():
    def sign_inn(self):
     print("Logged in")
class Wizard(User):
    print("wizard")
w1=Wizard()
print(w1.sign_inn())

class User1():
    def sign_in(self):
     print("Logged in")
     #return self
class Wizard1(User1):
    print("wizard")
    def __init__(self,name,power):
        self.name=name
        self.power=power
        print(f"Wizard block")
    def attack(self):
         print(f"Wizard , {self.name} has power of {self.power}")
w2=Wizard1('Anand',50)
#print(w2.sign_in())
print(w2.attack())
print(w2.sign_in())
print(isinstance(w1,User))
print(isinstance(w1,Wizard))
print(isinstance(w1,Wizard1))
print(isinstance(w2,Wizard1))
print(isinstance(w2,Wizard))
print(isinstance(w2,object))
