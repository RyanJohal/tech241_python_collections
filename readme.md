# Intro to collectibles

### Lists and tuples
Here I made a list, accessed different parts, changed specific elements, added to it, removed from it, used the pop function to remove specific parts of it but keep them in existence. 
Mixed data type lists to store multiple data types.
List slicing is used to accessing specific parts of the list for example contents between the second and fourth index.
Tuples are immutable lists, therefore they cannot be changed. 
```python
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

```
### Dictionaries
Here I made a dictionary, accessed different parts of it, changed values, and printed the dictionary keys and values.
```python
# Dictionaries

# Key - Value pairs

# Key is the name/reference, Value is the data stored

# Making a dictionary

student_1 = {
    "name": "ryan",
    "stream": "devops",
    "completed_lessons": 4,
    "completed_lessons_names": ["variables", "git", "data_types"]
}

print(student_1)

# How to access

print(student_1["stream"])
print(student_1["completed_lessons_names"][0])

# Changing a value

student_1["completed_lessons"] = 3
print(student_1["completed_lessons"])

student_1["completed_lessons_names"].remove("data_types")
print(student_1["completed_lessons_names"])

# Dictionary methods

print(student_1.keys())
print(student_1.values())

```
### Sets and frozen sets
Sets are lists but unordered. Frozen sets are lists but unordered and immutable.
```python
# Sets and Frozen Sets

# {} - list but unordered

car_parts = {"wheels", "windows", "exhaust", "streering wheel"}
print(car_parts)

# add to a set

car_parts.add("doors")
print(car_parts)

# remove from set

car_parts.remove("doors")
print(car_parts)

# frozen set

x = frozenset(["one", "two", "three", "four"])
print(x)

```
### 1. Define a list
```python
# 1. List of things I'll buy once I am rich

dream_purchases = ["home gym", "wellness centre", "personal chef", "urus", "pt"]

print(dream_purchases)
print(type(dream_purchases))

# Printing different parts of the list
print(dream_purchases[0])
print(dream_purchases[1])
print(dream_purchases[-1])

# Replacing a part of the list
dream_purchases[4] = "masseuse"
dream_purchases[3] = "G wagon"
print(dream_purchases)

# Adding and removing an item
dream_purchases.append("doberman")
dream_purchases.remove("wellness centre")
print(dream_purchases)

# Removing without specifying
dream_purchases.pop()
print(dream_purchases)

```

### 2. Making a program that allows users to order from a menu
```python
# Indian restaurant

# Listing menu
starters = ["samosa", "kale chaat", "pakora", "chilli paneer", "aloo tikki"]
mains = ["chana masala", "bindhi", "saag", "saag aloo","rice"]
desserts = ["pistachio kulfi", "gulab jaman", "cheesecake"]

# Printing menu for customer
print(f'the starter menu: {starters}')
print(f'the main menu: {mains}')
print(f'the dessert menu: {desserts}')

# Allowing user to input
starter_order = input("What would you like to start?: ")
main_order = input("What would you like for mains?: ")
dessert_order = input("What would you like for dessert?: ")

# Printing order back to them using a loop through each list
order = []
for i in starters:
    if i == starter_order:
        order.append(i)

for i in mains:
    if i == main_order:
        order.append(i)

for i in desserts:
    if i == dessert_order:
        order.append(i)

print(f'Your starter is: {order[0]}')
print(f'Your main is: {order[1]}')
print(f'Your dessert is: {order[2]}')


```



### Hero story using dictionaries
```python
# 3. Hero story

story_1 = {
    "start": "boy bullied in school",
    "middle": "gets bitten by shark and becomes a water bender",
    "end": "falls in love with bottom of the ocean and decides to live there"
}
print(story_1)
print(story_1.keys())
print(story_1.values())
print(story_1["start"])
print(story_1["middle"])
print(story_1["end"])

story_1["hero"] = "shark boy"
print(story_1)

```