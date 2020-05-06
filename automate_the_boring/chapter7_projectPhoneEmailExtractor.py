#! python3

# This program will take the task of finding phone numbers and emails.
# paste into the program
# then copy back onto clipboard

# HOWITWORKS:
# Ctrl + A all data you want to sort
# Ctrl + C to copy data onto clipboard
# Run this program
# Ctrl + V onto new document to have all phone numbers and emails

import re, pyperclip



regexEmail = re.compile(r'''(
[a-zA-Z0-9-._%.]+             # username part of email address
@
[a-zA-Z0-9-.]+                # domain name, period is optional in domain. 
(\.[a-zA-Z]{2,4})            # dot - something 
)''', re.VERBOSE)

regexPhone = re.compile(r'''(
(\d{3}|\(\d{3}\))?              # area code or area code in brackets 
(\s|\.|-)?                      # space between area code and number
(\d{3})                           # first three digits 
(\s|\.|-)                       # next separator
(\d{4})                           # next 4 digits 
(\s*(x|ext|ext.)\s*(\d{2,5}))?  # ext phrase
)    
''', re.VERBOSE)


preData = str(pyperclip.paste())

matches = []
for groups in regexPhone.findall(preData):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x'+groups[8]
    matches.append(phoneNum)
for groups in regexEmail.findall(preData):
    matches.append(groups[0])

if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard! ')
    print('\n'.join(matches))
else:
    print('There were no matches found')







# findEmail = regexEmail.findall(preData)
# findPhone = regexPhone.findall(preData)
#
# for x in findEmail and findPhone:
#     if findPhone or findEmail == None:
#         print('No matches found')
#     else:
#         copiedData = pyperclip.copy()
#         print('Here is the email address ' + findEmail + ' and here is the phone number: ' + findPhone)


