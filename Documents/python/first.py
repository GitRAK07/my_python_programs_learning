name='anand'
age=22
## String Indexes ##
print(name[0:5:2])
print(name[:-1])
print(name[-1])
print(name[::-1])
###################
#Uppercase
print(name.upper())   #All the characters are in upper case.
print(name.capitalize()) #only the first char is in Upper Case.
print(name.find('andw'))  #Finds and tells where the index of it starts
print(name.replace('a','A'))
name=name.replace('a','A')  
print(name)
########## BOOLEAN
print(bool(0))
print(bool(1))
print(bool(-1))
##########INPUT Variables###########
work=input("What are you doing to survive")
print(work)