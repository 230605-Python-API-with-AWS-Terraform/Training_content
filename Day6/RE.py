"""

s='sample1234'

print('12' in s)
print(s.find('125'))
print(s.index('125'))


import re
print(re.search('12',s))
print(re.search('[0-9][0-9][0-9][0-9][0-9]',s))

"""

"""

Character(s)------------------------	Meaning

.	Matches any single character except newline
^	∙ Anchors a match at the start of a string
    ∙ Complements a character class
$	Anchors a match at the end of a string
*	Matches zero or more repetitions
+	Matches one or more repetitions
?	∙ Matches zero or one repetition
∙ Specifies the non-greedy versions of *, +, and ?
    ∙ Introduces a lookahead or lookbehind assertion
    ∙ Creates a named group
{}	Matches an explicitly specified number of repetitions
\	∙ Escapes a metacharacter of its special meaning
    ∙ Introduces a special character class
    ∙ Introduces a grouping backreference
[]	Specifies a character class
|	Designates alternation
()	Creates a group
:
#
=
!	Designate a specialized group
<>	Creates a named group

"""

import re

# Matching a pattern using metacharacters
pattern = r"gr.y"
strings = ["gray", "grey", "grxy", "glory"]
for string in strings:
    if re.search(pattern, string):
        print(f"Match found: {string}")
    else:
        print(f"No match: {string}")

# Using character classes
pattern = r"[a-z][0-9]"
string = "Hello, World1!"
vowels = re.findall(pattern, string, re.IGNORECASE)
print(f"Vowels found: {vowels}")

# Using quantifiers
pattern = r"\s{3}-\d{3}-\d{4}"
strings = ["   -456-7890", "555-5555", "1-800-123-4567"]
for string in strings:
    if re.match(pattern, string):
        print(f"Valid phone number: {string}")
    else:
        print(f"Invalid phone number: {string}")

    