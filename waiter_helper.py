# # 1. List of things I'll buy once I am rich
#
# dream_purchases = ["home gym", "wellness centre", "personal chef", "urus", "pt"]
#
# print(dream_purchases)
# print(type(dream_purchases))
#
# # Printing different parts of the list
# print(dream_purchases[0])
# print(dream_purchases[1])
# print(dream_purchases[-1])
#
# # Replacing a part of the list
# dream_purchases[4] = "masseuse"
# dream_purchases[3] = "G wagon"
# print(dream_purchases)
#
# # Adding and removing an item
# dream_purchases.append("doberman")
# dream_purchases.remove("wellness centre")
# print(dream_purchases)
#
# # Removing without specifying
# dream_purchases.pop()
# print(dream_purchases)


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


# # 3. Hero story
#
# story_1 = {
#     "start": "boy bullied in school",
#     "middle": "gets bitten by shark and becomes a water bender",
#     "end": "falls in love with bottom of the ocean and decides to live there"
# }
# print(story_1)
# print(story_1.keys())
# print(story_1.values())
# print(story_1["start"])
# print(story_1["middle"])
# print(story_1["end"])
#
# story_1["hero"] = "shark boy"
# print(story_1)