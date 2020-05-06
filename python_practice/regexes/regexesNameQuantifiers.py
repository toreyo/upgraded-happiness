import re

text2search = '''
Mr. Johnson
Mr Kim
Mr. Jim
Mrs Rodgers
Mrs Juno
Ms. Jimbo
Mrs. Kanto
Mr Higa
Mr H
Mr. Rodriguez

'''

names = re.compile(r'(Mr|Mrs|Ms)\.?\s[A-Z]\w*')

mo = names.finditer(text2search)
for n in mo:
    print(n)

