class Color():
    def __init__(self, color, ascii):
        self.color = color
        self.ascii = ascii
        self.list = ['Anand','kumar']
        print(f"Color is {self.color}")

    # Modifying the dunder methods / customizing it
    def __str__(self):
       return f'{self.ascii}'
    def __call__(self): # An object can be called using __call__ method.
        return "Calling"
    def __getitem__(self,i):
        return f'{self.list[i]}'

color = Color('red', 'asdbe234f')
print(color)
print(str(color))
#del(color)   #Deletes the function /class
print(color.__str__())
print(color()) # Dunder call method calling function
print(color[1]) #Refer getitem dunder method
