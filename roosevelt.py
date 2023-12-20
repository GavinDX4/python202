# Initialize phrase
original_phrase = "The only thing we have to fear is fear itself"

# Convert phrase to list
phrase_list = original_phrase.split()

# Create an empty list
result_list = []

# Inspect Each Word and Modify
for word in phrase_list:
    if word[0].lower() in "aeiou" and word[0].lower() != 'y':
        modified_word = word + "way"
    else:
        modified_word = word[1:] + word[0] + "ay"
    result_list.append(modified_word)

# Convert the new list to a string
final_result = ' '.join(result_list)

# Print the result
print(final_result)