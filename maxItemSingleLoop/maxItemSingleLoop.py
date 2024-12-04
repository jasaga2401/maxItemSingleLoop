
# Single 
def find_max_single_pass(lst):
    max_value = lst[0]
    for x in lst:
        if x > max_value:
            max_value = x
    return max_value


numbers = [3, 5, 7, 2, 8, 10, 6]


# Resource-efficient algorithm
max_single_pass = find_max_single_pass(numbers)
print(f"Max using single pass: {max_single_pass}")


