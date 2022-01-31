# 5️⃣ List Comprehensions ✌️


# Normal Way
my_list = []
for number in range(0, 1000):
    if number % 2 == 0:
        my_list.append(number)

print(my_list)

# Using List Comprehensions
my_list_2 = [num for num in range(0, 1000) if num % 2 == 0]
print(my_list_2)
