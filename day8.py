import itertools

def generate_permutations(s1, s2):
    # Generate all permutations of s1
    permutations = itertools.permutations(s1)
    
    # Convert permutations from tuples to strings and store in perm_set 
    perm_set = {''.join(p) for p in permutations}
    
    # Check if s2 is in the set of permutations of s1
    return s2 in perm_set

# Example
s1 = "code"
s2 = "doce"
print(generate_permutations(s1, s2))
