def check_Ispalindrome(s):
    return s == s[::-1]
# find palindrom substrings
def palindrome_substrings(s):
    palindromes = set()  # No duplicates in sets
    n = len(s)
    
    #iterate the string
    for i in range(n):
        for j in range(i + 1, n + 1): 
            substring = s[i:j]
            # Palindromes greater than 1 character are considered
            if check_Ispalindrome(substring) and len(substring) > 1:  
                palindromes.add(substring)
    
    return list(palindromes)

# Example
input_string = "babad"
result = palindrome_substrings(input_string)
print("Posible palindrome substrings:", result)