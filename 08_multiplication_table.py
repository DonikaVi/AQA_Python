"""
Hometask 08_multiplication_table.

# Given 0 < number (integer) <= 11
# You need to print multiplication table based on this number

"""

# Make input for enter number
num = int(input('Please enter a positive integer between 1 and 11: '))

for row in range(1, num + 1):
    for col in range(1, num + 1):
        print(row * col, end='\t')
    print()
