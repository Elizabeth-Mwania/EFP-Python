# should i print the bracketed string?

import math
# Given string
s = "code"
# Calculate the length of the string
length_of_string = len(s)

# Print the length
print(f"The length of the string is: {length_of_string}")

# use catalan number to identify the number of bracket arrangement
n = length_of_string
catalan_number = math.factorial(2 * n) // (math.factorial(n + 1) * math.factorial(n))

# Print the result
print(f"The number of valid arrangements of brackets for {s}: {catalan_number}")