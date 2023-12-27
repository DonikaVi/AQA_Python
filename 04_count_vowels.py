"""
Hometask 4 Count vowels.

The English language has five vowels: A, E, I, O, and U
Please count each vowel occurrence in text bellow
(total sum of lower and capital cases)
and write output as table smth like this
#  -----------------
#  | vowel | count |
#  -----------------
#  |   a   |  11   |
#  |   e   |  23   |
# ...
# -----------------

then modify text where each vowel replaced with
A->À;  a->à ; E-> É ; e->é; I->Í , i->í ; O->Ó ; o->ó; U->Ú; u->ú
ex. "Í wàndéréd lónély...."   and print it


poem_text = ""I wandered lonely as a cloud
That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze.

Continuous as the stars that shine
And twinkle on the Milky Way,
They stretched in never-ending line
Along the margin of a bay:
Ten thousand saw I at a glance,
Tossing their heads in sprightly dance.""
"""


poem_txt = """I wandered lonely as a cloud
That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze.

Continuous as the stars that shine
And twinkle on the Milky Way,
They stretched in never-ending line
Along the margin of a bay:
Ten thousand saw I at a glance,
Tossing their heads in sprightly dance."""

sep_num = 25
print('-' * sep_num)
print(f"| {'Vowel':^9} | {'Count':^10} |")
print('-' * sep_num)

poem_txt_low = poem_txt.lower()
counts = {i: 0 for i in 'aeiou'}
for char in poem_txt_low:
    if char in counts:
        counts[char] += 1

for k, v in counts.items():
    print(f'| {k:^10}|  {v:^9} |')
print('-' * sep_num)

# modifying text
translation_table = str.maketrans('AaEeIiOoUu', 'ÀàÉéÍíÓóÚú')
modified_text = poem_txt.translate(translation_table)
print(modified_text)
