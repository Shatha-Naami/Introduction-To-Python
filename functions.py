# This Is Only Introduction For Python, Let's Start !

# 1️⃣ Functions ✌️

def sum_numbers(a, b):
    return a + b


sum_numbers(2, 5)  # 7


####################
def sum_numbers(a, b, c=None):
    if c is None:
        return a + b
    else:
        return a + b + c


sum_numbers(3, 5)  # 8
sum_numbers(3, 5, 1)  # 9

summationProcess = sum_numbers(2, 6, 8)  # Assign function `sum_numbers` to variable `summationProcess`.
print(summationProcess)
