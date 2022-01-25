# Split

text = "It was the best of times."

text_list = text.split(" ")
print(text_list, type(text_list))

csv = "12,235,3456,456,67,78"
csv_list = csv.split(",")
print(csv_list)

# Join

print(" ".join(text_list))
print("---".join(text_list))
print("".join(csv_list))

n = [56, 32, 56, 678, 23, 1, 0]

print(n)
n.sort()
print(n)
