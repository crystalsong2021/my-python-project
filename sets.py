"""
Unordered and unchangeable
- Items in a set do not have a defined order
- items cannot be referred to by index
- Items cannot be changed, only added/removed

"""
my_sets = {"January", "February", "March", "January"}
# order always changes, that's why it's unordered
print(my_sets)


# iterate the sets
for month in my_sets:
    print(month)

# adding element to the set
my_sets.add("April")
print(my_sets)

# remove the element
my_sets.remove("March")
print(my_sets)