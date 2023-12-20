#List of Names 
names_list=['Frank Harrelson', 'Bob Sharles', 'Bob Tranklin', 'Bob Grody', 'Hank Charles', 'Bob Rarrelson', 
'Mack Slobson', 'John Jonones', 'Rob Wranklin', 'Tom Simpsonian', 'Rob Rearrelson', 'John Moodys', 
'Frank Shones', 'John Harrelson','Frank Quhorles', 'Tom Pharles', 'Frank Fwanklin', 'Frank Charleston', 
'John Arles', 'John Georanklin', 'Frank Dobsonsoson', 'Diane Johnston', 'Dob Scone', 'Michael Scarn', 
'Goldie Hawn', 'Billie Holliday', 'Woody Harrelson', 'Arthur Rubinstein', 'Thomas Edison', 'Robert Goulet']

# Sort by last name
sorted_names = sorted(names_list, key=lambda name: name.split()[-1])

# Print the sorted names
print(sorted_names)

# Create the five and two names
five_and_two_usernames = list(map(lambda name: name.split()[-1][:5] + name.split()[0][:2], names_list))

# Print the five and two names
print(five_and_two_usernames)