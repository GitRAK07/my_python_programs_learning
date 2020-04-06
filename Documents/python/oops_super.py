class User():
    def __init__(self, email):
        self.email = email
        print(f"Logged in as {email}")
        
    def sigin(self):
        print("Welcome")

class Wizard(User):
    def __init__(self,name,age,email):
        #User(email)
        super().__init__(email)
        self.name=name
        self.age=age
        print(f"The user {name} is of age {age}")

w=Wizard('Anand',26,'anand@gmail.com')
print(w)
print(dir(Wizard.sigin)) #Lists all the objects / attributes of the class / function ( called Introspection)
    