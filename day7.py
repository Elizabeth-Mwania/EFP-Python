def count_characters(input_string):
    character_count = {}
    #count each character frequency
    for char in input_string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
            
    # Sort the dictionary by count in decreasing order
    sorted_character_count = dict(sorted(character_count.items(), key=lambda item: item[1], reverse=True))
    
    # return sorted_character_count
    return list(sorted_character_count.keys())

# Example:
input_string = "world's joke of the day"
result = count_characters(input_string)
print(result)