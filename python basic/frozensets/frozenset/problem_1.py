my_sets={1,2,3,4,5}
print(type(my_sets))
my_sets.add(10)
print(my_sets)

# convert this set into frozenset
my_frozenset=frozenset(my_sets)
print(my_frozenset)
my_frozenset.add(20)
print(my_frozenset)