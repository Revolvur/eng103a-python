# Dictionaries

# Key-Value Pairs

my_dict = {'key': 'value'}  # value can be anything

table = {
    'name': 'The Table',
    'colour': 'light brown',
    'dimensions': {
        'height': 120,
        'length': 200,
        'width': 150
    }
}

print(table)
print(table['colour'])  # DICTIONARY NAME [ KEY ]

# table['height'] = 125
# table['price'] = 99.99
# print(table)

table.update({'price': 99.99, 'height': 125})
print(table.get('price'))
print(table['price'])

## difference is 'get looks for price, finds it and prints it
## square brackets looks for the key price and then prints it

# get() method returns a default value (none) if the key is missing
#
# dict_in_dict = {'dict': {'key': 'value'}, 'dict2': {'key2': 'value2'}}
#
# print(dict_in_dict, type(dict_in_dict))
# print(dict_in_dict['dict'])
#
# print(dict_in_dict.get('dict').get('key'))
# print(dict_in_dict['dict']['key'])

print(table.keys())
print(table.values())
print(table.items())