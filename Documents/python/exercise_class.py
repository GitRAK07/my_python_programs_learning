#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
def old(*args):
      return max(args)
      

class1=Cat('Meow',2)
class2=Cat('Meow2',3)
class3=Cat('Meow3',1)

print(f"The oldest cat is {old(class1.age, class2.age, class3.age)} years old.")
# 1 Instantiate the Cat object with 3 cats



# 2 Create a function that finds the oldest cat



# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2