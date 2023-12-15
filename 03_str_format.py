"""
Hometask 3 String Format.

we have norway text in old style formatting
re-write the same text as:
#1 string with format() call
#2 f-string
use linter(https://github.com/wemake-services/wemake-python-styleguide)
to check your new created python module for possible linter errors
try to run code from pycharm/command line

norway_text = 'Automatisering akselererer %syeblikket da
roboter vil erobre planeten v%sr. (%s)' % ('ø', 'å', 'Æ')
print(norway_text)
"""

norway_text = ('Automatisering akselererer %syeblikket da '
               'roboter vil erobre planeten v%sr. (%s)')

text_old_style = norway_text % ('ø', 'å', 'Æ')
print(text_old_style)


'#1 string with format() call'
text_format = ('Automatisering akselererer {0}yeblikket da roboter vil '
               'erobre planeten v{1}r. ({2})'.format('ø', 'å', 'Æ'))
print(text_format)


'#f-string '
first_letter = 'ø'
second_letter = 'å'
third_letter = 'Æ'
text_f_string = (f'Automatisering akselererer {first_letter}yeblikket '
                 f'da roboter vil '
                 f'erobre planeten v{second_letter}r. ({third_letter})')
print(text_f_string)
