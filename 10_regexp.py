"""
Hometask 17 regexp.

# open input.txt file and find all small
english letters that match such conditions:

# target small letter round exactly with three capital
 english letters on the left and on the right

# Match examples:
# sdTRYaUVKn  -> matches "a" because 'TRY' on the left
( 3 capital letters ) and 'UVK' on the right ( 3 capital letters)
# NTRSjARTb   -> no match ( not exactly 3 capital letters
on the left ('NTRS' = 4 letters) )
# zDFGbOPNq   -> matches "b"
# Print Output as : "Result: "string of found letters">

# Note:
#  - Result will be human-readable string up to 10-15 characters
#  - Some usefull regexp constructions
# [A-Z]  - match any capital letter
# [^A-Z] - match any character except capital letter
# [a-z]  - match small letter
# do not forget about possible PRE and POST regexp searches

"""

import re

with open('input.txt') as fh:
    data = fh.read()
# """Find no more than three capital letters"""
around_pattern = '[A-Z]{3}(?<![A-Z]{4})(?![A-Z])'
"""Find small letters"""
search_pattern = '[a-z]{1}'
full_pattern = around_pattern + search_pattern + around_pattern
all_letters = re.findall(full_pattern, data)
str_of_list = ''.join(all_letters)
only_small_letters = re.findall('[^A-Z]', str_of_list)
sm_all = ''.join(only_small_letters)
print(f'Result: "{sm_all[0:6]} {sm_all[6:10]}"')
