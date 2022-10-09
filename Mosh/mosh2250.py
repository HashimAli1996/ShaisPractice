#Type conversion
# birth_year = input('Birth year: ')
# print(type(birth_year))
# age = 2022 - int(birth_year)
# print(type(age))
# print(age)

#Exercise
# lbs_weight = input('Weight in pounds(lbs)?: ')
# kgs_weight = int(lbs_weight) * 0.45
# print(kgs_weight)

#Strings
course = "Python's course for Beginners"
print(course)

course2 = 'Pythons course for "Beginners"'
#Python's apostrophe cant be put in single quotes.  Has to be done like the first "course" variable.
# and Beginners double quotes has to be done within single quotes to show.
print(course2)

#multiple line string using triple apostrophes.
course3 = '''Dear Sir/Madam

example paragraph lines
example paragraph lines

Regards,
Support team
'''
print(course3)


course4 = 'Python for beginners'
#          0123456789...
another = course[:]
# Using numbers in brackets will print the character. 13 is the g in beginners if you count from left to right INCLUDING spaces. but if you use minus numbers, it starts from right to left.
# Using ratios [:9] or [0-9] will give 0 - 3 characters. It prints UPTO that character but not itself. i.e 3 will not be shown, will have to change to 4 to be shown.
print(course4[0])
print(course4[13])
print(course4[-1])
print(course4[0:9])
print(another)

name = "Jennifer"
print(name[1:-1])   










