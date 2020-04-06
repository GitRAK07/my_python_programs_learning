books=[1,2,3,4,5]
print(books)
books.append(6) #Adds at the end and only one argument is allowed. To allow multiple use extend method
print(books)
books.insert(6,7) #Insert by mentinoing the index place
print(books)
print(books[6])
books.extend([8,9])
print(books )
books.pop()   #Removes the last index value
print(books)
books.pop(0) #Removes the 1st index value
print(books)
books.remove(3) #Removes the value mentioned but not the index.
print(books)
books.clear() #Clears the list completely.
print(books)
name='Anand'
last_name=['k','u','m','a','r']
print(name.index('an')) #Provides the index of the first occurance of the char provided.
print(last_name.index('m'))
print(name.index('A',0,2)) #Provide the index of the first occurance of the char provided with the range 0-2 indexes
print('a' in name) #To check if any char is present in the string or not. Boolean output.
print('x' in 'Anand')
print(name.count('n')) #Prints the number of occurance of the char
#last_name.sort()
print(last_name.sort()) #Sort() method will not work in the first attempt.. You can print in the next line after using the sort command.
print(last_name)
print(sorted(last_name)) #Sorts at the time of using but the original value will not get modified.
print(last_name)
last_name.reverse() #Reverses the string.
print(last_name)
print(list(range(1,100)))
#List Unpacking
a,b,c,*others,d=[1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(others)
print(d)
####################