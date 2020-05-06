import re

emails = '''
johnMSmith@gmail.com
john.smith@university.edu
john-321-smith@my-work.net
'''

regexEmails = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|net|edu)')


mo = regexEmails.finditer(emails)
for x in mo:
    print(x)
