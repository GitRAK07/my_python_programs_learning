name= input("What is your name")
age= input("Enter your age:")
age= int(age)>20
exp= input("Enter your eperience")
exp = int(exp) > 5
print(age)
if age and exp:
 print("You are major")
else:
 print("You are minor")
is_friend=True
can_message="message allowed" if is_friend else "not allowed to message"
print (can_message)

####
#List cannot be compared to be equal
a=[1,2,3]
b=[1,2,3]
print( a is b )