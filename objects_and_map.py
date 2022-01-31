# 4️⃣ Objects & Map ✌️
class Person:
    department = 'AI Specification'

    def __init__(self):
        self.name = 'Init Val'
        self.location = None

    def set_name(self, new_name):
        self.name = new_name

    def set_location(self, new_location):
        self.location = new_location


person = Person()
person.set_name('Shatha')
person.set_location('Gaza, Palestine !')

print('{} live in {} and works in the department {}'.format(person.name, person.location, person.department))

# example of mapping the `min` function between two lists.
store1 = [10.00, 11.00, 12.34, 2.34]
store2 = [9.00, 11.10, 12.34, 2.01]
cheapest = map(min, store1, store2)
print(cheapest)

for item in cheapest:
    print(item)
