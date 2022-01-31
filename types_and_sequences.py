# 2️⃣ Types & Sequences ✌️
name = 'ali'
type(name)  # str

# EX : Tuples
x = (1, 'a', 2, 'b')
type(x)

# EX : List
x = [1, 'A', 2, 'B']
type(x)

x.append(2.4)
print(x)

# For Loop
for item in x:
    print(item)

# While
startPoint = 0
while startPoint != len(x):
    print(x[startPoint])
    startPoint = startPoint + 1

# Use `*` to repeat lists.
var = [1] * 3
print(var)

# Use the `in` operator to check if something is inside a list.
x = 1 in [1, 2, 3]
print(x)

# Now let's look at strings. Use bracket notation to slice a string.
desc = 'This is a string'
print(desc[3:])

# Dictionaries associate keys with values.
myMap = {'Shatha Naami': 'shatha@gmail.com', 'Bill Gates': 'billg@microsoft.com'}
for email in myMap.values():
    print(email)

# There are exception here 🔴
# print('Chris' + 2)

# Correct in previous is !
print('Shatha' + str(1999))

# How pass params:
sales_record = {
    'price': 3.24,
    'num_items': 4,
    'person': 'Shatha', }

sales_statement = '{} bought {} item(s) at a price of {} each for a total of {}'

print(sales_statement.format(sales_record['person'],
                             sales_record['num_items'],
                             sales_record['price'],
                             sales_record['num_items'] * sales_record['price']))
