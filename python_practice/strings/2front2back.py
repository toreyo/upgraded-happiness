x = 'w3resource'
y = 'w3'
z = 'w'

def strReturn(strr):
    if len(strr) >= 2:
        return strr[:2] + strr[-2:]
    elif len(strr) < 2:
        return 'empty'


print(strReturn(y))
