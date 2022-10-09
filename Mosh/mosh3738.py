# Formatted Strings
firstname = 'John'
lastname = 'Smith'

# message = firstname + ' [' + lastname + ']' is a coder <- shows error.
#use of f'' and curly braces to get around error.

msg = f'{firstname} [{lastname}] is a coder'
print(msg)


course = 'Python for beginners'
print(len(course))
# len function is used to display how many characters there are (including spaces)

print(course.upper()) # .upper() makes it all characters uppercase. theres also a .lower() function

print(course.find('n')) #this finds the character first to come up with what you're searching for.

print(course.replace('beginners', 'Absolute Beginners')) #Case sensitive.

print('Python' in course) #this finds 'Python' in the course variable and shows as True as False.