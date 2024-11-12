def max_subarray_sum(arr):
    max_sum = float('-inf')  # Initialize max sum as a smallest nummber
    max_subarray = []

    # Generate all possible subarrays
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            subarray = arr[i:j+1]  # to get the subarray by slicing arr
            current_sum = sum(subarray)  # Calculate sum of current subarray

            # Update max sum and max subarray
            if current_sum > max_sum:
                max_sum = current_sum
                max_subarray = subarray

    return max_sum, max_subarray

# Example
arr = [5,20,-3,-4,1]
max_sum, subarray = max_subarray_sum(arr)
print("Maximum sum is:", max_sum)
print("Subarray is:", subarray)