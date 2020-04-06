#function-- Inuilt function and defined function. Method is different. string.method() like.. a.captialize() / a.add(). These are methods

def hello_world():  # Define a function
     print("Hellow World!")
     

hello_world() #Call a function

def parameters(a,b): #Parameters
    print(f"hello {a} {b}")

parameters(2,':P') #Arguments


def hello(name='Anand',age=25): #Default parameters. 
     print(f"Hello {name}, Your age is {age}")

hello('Kumar',16)
hello() #Example of calling the default parameterss
