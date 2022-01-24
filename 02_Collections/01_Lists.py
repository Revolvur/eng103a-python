# # # Lists
# #
# # shopping_list = ["eggs", "bread", "bananas", "tea"]
# # print(shopping_list, type(shopping_list))
# #
# # print(len(shopping_list))
# #
# # print(shopping_list[-1])
# #
# # shopping_list[2] = "milk"
# # print(shopping_list)
# # # shopping_list[4] = "biscuits"  # assigning to index has to be within existing range
# #
# # shopping_list.append("biscuits")  # append is a method that changes the list as we apply it
# # print(shopping_list)  # append can only be done item by item
# #
# # shopping_list.append("bread")
# # shopping_list.append("bread")
# #
# #
# # shopping_list.remove("bread")
# # print(shopping_list)
# #
# # print(shopping_list.pop(-1)) # does action and also returns it
# # print(shopping_list) # remove is based on values and pop is based on the position/index
# #
# # last_item = shopping_list.pop()  # does action and also returns it
# # print(shopping_list)
# # print(last_item)
#
# mixed = [1, 2, "three", True, None, ["another", "list"]]
# print(mixed)
#
# mixed[1] = 2.0
# print(mixed)
# #
# # # LISTS ARE MUTABLE
# #
# # print(mixed[2:4])
# # print(mixed[:4])
# # print(mixed[2:7:2])
# # print(mixed[7:2:-1])
# # print(mixed[::3])
# #
# # print(mixed[5][0])  # to grab a list in a list
# # print(mixed[5][0][0])  # to grab a list in a list
#
# sublist = mixed[5]
# print(sublist)
# #mixed[5] = ['a', 'b']  # replaced the list in the list with this list
# print(mixed)
# mixed[5][1] = 'b'
# print(mixed)
# print(sublist)

# Tuples

colours = ("red", "blue", "green")
print(colours, type(colours))

print(colours[0])


# Unlike lists, tuples are immutable (so they can't be changed)

print(colours.count("red"))
print(colours.index("red"))

list_in_tuple = (
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
)

print(len(list_in_tuple))
list_in_tuple[0][-1] = "SUCCESS"
print(list_in_tuple)  # changing the list in a tuple
