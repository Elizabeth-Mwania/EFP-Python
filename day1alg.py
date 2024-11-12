def sum_one_fuc(arr, number):
    indices_map = {}  # store indices
    for idx, num in enumerate(arr):
        complement = number - num  # Find the number we need to pair with `num` to get `number`
        if complement in indices_map:  # Check if we've already seen this complement
            return [indices_map[complement], idx]  # Return the indices of the complement and current number
        indices_map[num] = idx  # Store index of the current number
    return []  # Return empty list if no such pair exists

# application
arr = [3, 7, 11, 15]
target_number = 18

result = sum_one_fuc(arr, target_number)
print("Indices:", result)