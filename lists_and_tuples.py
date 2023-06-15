# Lists and Tuples

# Making a list in python



shopping_list = ["eggs", "bacon", "bananas", "bread", "haggis"]

print(type(shopping_list))
print(shopping_list)

# Accessing certain parts of list

print(shopping_list[0])

# change a specific element of my list

shopping_list[4] = "orange juice"
print(shopping_list)

# list methods

shopping_list.append("butter")
print(shopping_list)

shopping_list.remove("butter")
print(shopping_list)

shopping_list.pop()
print(shopping_list)

x = shopping_list.pop(0)
print(x)
print(shopping_list)

# Mixed data type list

mixture = [1, 2, 3, "one", "two", "three"]
print(mixture)

# list slicing

print(mixture[1:3])
print(mixture[::2]) # 1, 3, "two"

# Tuples

# () - Tuples are immutable, so they cannot be changed.

essentials = ("bread", "eggs", "milk")
print(essentials)
print(essentials.count("bread"))

