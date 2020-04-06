amazon_cart=['Shoes','Shirts','Phones','baskets']
print(amazon_cart)
amazon_cart[0]='Jackets' #original value will get changed
print(amazon_cart)
new_cart=amazon_cart #This will assign the original variable itself instead of just values
new_cart=amazon_cart[:] #This is the way to assign values to the new variable
print(new_cart)
new_cart[0]='Pencil'
print(amazon_cart)
print(new_cart)
matrix=[
[1,0,1],
[1,0,1],
[1,0]
]
print(matrix[2][1])
#string=[1,2,2,3]
string=['a','b']
a="anand"
print(type(matrix),type(new_cart),type(string),type(a))