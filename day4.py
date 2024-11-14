#quadduplets
def quadruplet_subarray(arr, target):
    subarrays = set()  # create set et to store unique subarrays
    n = len(arr)

    # find subarrays of length 4
    for i in range(n - 3):  # set range
        subarray = arr[i:i + 4]  # Extract the subarray of 4 elements
        
        # Condition to check if the subarray has unique elements and sums to the target
        if len(set(subarray)) == 4 and sum(subarray) == target:  # Check uniqueness and sum
            subarrays.add(tuple(subarray))  # Add as tuple to the set for uniqueness

    return [list(subarray) for subarray in subarrays]  # Convert back to list

# Example:
input_array = [1, 2, 3, 4, 5, 6, 1, 2]
target_sum = 10
result = quadruplet_subarray(input_array, target_sum)
print(result)