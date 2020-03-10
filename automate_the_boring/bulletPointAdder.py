#! python3
# bulletPointAdder.py adds Wikipedia bullet points to start
# of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

# TODO: Separate lines and add stars

lines = text.split('\n')
for i in range(len(lines)): #loop through all indexes in the "lines" list
    lines[i] = '*' + lines[i] #add start to each string in "lines" list
text = '\n'.join(lines)

pyperclip.copy(text)


