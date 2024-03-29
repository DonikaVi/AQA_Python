"""
Hometask 5 List of tuple.

Given list of tuples (people list ->
name, surname, age, profession, City location)
# 1 - Add your new record with similar random data
# to the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5
#  (1<->5) and print result
# 3 - check condition that all people in modified list
# with records indexes 6, 10, 13
#     have age >=30 and print result

people_records = [
    ('John', 'Doe', 28, 'Engineer', 'New York'),
    ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
    ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
    ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
    ('Michael', 'Brown', 22, 'Student', 'Seattle'),
    ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
    ('David', 'Miller', 33, 'Software Developer', 'Austin'),
    ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
    ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
    ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
    ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
    ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
    ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
    ('Ava', 'White', 42, 'Journalist', 'San Diego'),
    ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')

]
"""

people_records = [
    ('John', 'Doe', 28, 'Engineer', 'New York'),
    ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
    ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
    ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
    ('Michael', 'Brown', 22, 'Student', 'Seattle'),
    ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
    ('David', 'Miller', 33, 'Software Developer', 'Austin'),
    ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
    ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
    ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
    ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
    ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
    ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
    ('Ava', 'White', 42, 'Journalist', 'San Diego'),
    ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix'),
]

# 1 - Add your new record with similar random data
# to the beginning of the given list
people_records.insert(0, ('James', 'Bond', '30', 'Secret agent', 'New York'))
print(people_records)

# 2 - In modified list swap elements with
# indexes 1 and 5  (1<->5) and print result
people_records[1], people_records[5] = people_records[5], people_records[1]
print(people_records)

# 3 - check condition that all people in modified list
# with records indexes 6, 10, 13
#     have age >=30 and print result

people_records_2 = [list(ele) for ele in people_records]
print(people_records_2)

if people_records_2[6][2] >= 30:
    print(people_records_2[6])
else:
    print('This person is under 30 years old')
if people_records_2[10][2] >= 30:
    print(people_records_2[10])
else:
    print('This person is under 30 years old')
if people_records_2[13][2] >= 30:
    print(people_records_2[13])
else:
    print('This person is under 30 years old')
