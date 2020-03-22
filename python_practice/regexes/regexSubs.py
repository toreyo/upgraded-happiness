import re

matcher = re.compile(r'agent \w+', re.I)
matcherNew = matcher.sub('CENSORED', 'Agent alice gave the documents to Agent Bob')

print(matcherNew)


codeSentence = 'Agent Bill told AGENT jim about AgeNt rodgers story about AgEnT judeth'

codeNames = re.compile(r'agent (\w)\w*', re.I)
nameHider = codeNames.sub(r'\1****', codeSentence)

print(nameHider)

# re.VERBOSE to make identifying the regular expression more legible
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)
