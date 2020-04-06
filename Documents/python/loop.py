for i in range(2):
    print(list(range(10)))


for i in range(0,100,1):
    print(i)
# to do it reverse
# for i in range(0,10,-1) : #This will not work.
for i in range(10,0,-1):
    print(i)
 
for i in [1,2,3,4]:
    for j in {1,2,3,4}:
        print((i),(j))
print("End of 1st")

for i in range(100):
   print(i)

#dictionary
user = {
    'name': 'Anand',
    'Age': 20,
    'Sex': 'Male'
}
for i in user:
    print(user.keys())

# Enumerate -- It is used to print the index
for i,char in enumerate(list(range(100))):
    if char is 55:
     print(i,char)
# while statement-- Use break and else statements.
i=0
while i < 4:
   print(i)
   i+=1
   break
else:
  print("out of loop")


while True:
    response = input( "say something")
    if response =='bye':
     break