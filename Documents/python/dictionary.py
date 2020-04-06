####### Dictionary  ########
user = {
    'name': 'Anand',
    'Age': 26,
    'occupation': 'Software Engineer'
}
print(user['name'],user['Age'])
print(user.get('age')) #Use get method to avoid the program throwing the errors.
print(user.get('Age', 90)) #Returns value 90 if Age value is not found in the dict.
print( 'name' in user.keys())   #Checks the value 'name' in the keys of the variable 'user' and returns boolean
print( 'name' in user.values()) #Checks the value 'name' in the values of the variable 'user' and returns boolean
print( 26 in user.values())
print(user.items()) #List the items of the dictionary.
user.popitem() #Removes the last item from the dictionary
user.update({'Ages':55})
print(user)