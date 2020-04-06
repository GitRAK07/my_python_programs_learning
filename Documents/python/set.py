#### Set is a unique set of values ####

my_set={1,2,2,4,5,6,7,6,5,}
print(my_set)
my_set.update({9,2})
print(my_set)

my_list={1,2,3,4,5,6,7,4,3}
print(set(my_list))
print(list(my_list))
print(my_list.difference(my_set)) #Will list the difference of set1 with comparison to set2
#my_list.difference_update(my_set) # The only difference values will get updated.
print(my_list)
print(my_list.isdisjoint(my_set)) # If there is no common value , it will return True ( Disjoint ) . If the two circle joints , then faluse ( not a disjoin )
print(my_list.union(my_set)) #Prints all the values of both the sets and eliminates the duplicate values.
print(my_list|my_set) # Alternate symbol for union is |
print(my_list.issuperset(my_set))
