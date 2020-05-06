import re

preg1 = re.compile(r'^\d{1,3}(,\d{3})*$')

mo = preg1.search('70')
print(mo)


name = 'Haruo Watanabe'

nameRegex = re.compile(r'([A-Z][a-z]*)\sWatanabe')
x = nameRegex.search(name)
print(x)

# phrase must match sentence where the first word is either Alice, Bob, or Carol;
# the second word is either eats, pets, or throws;
# the third word is apples, cats, or baseballs;
# and the sentence ends with a period
phrase = 'Alice pets baseballs.'

phraseRegex = re.compile(r'''
(Alice|Bob|Carol)\s
(eats|pets|throws)\s
(apples|cats|baseballs)
\.
''', re.VERBOSE|re.I)

y = phraseRegex.search(phrase)
print(y)
