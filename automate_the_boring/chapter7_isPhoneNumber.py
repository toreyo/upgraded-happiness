def isPhoneNumber(text):
    if len(text) != 12:
        return False
    if text[3] != '-':
        return False
    if text[7] != '-':
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print("is 808-305-7561 a phone number?")
print(isPhoneNumber('808-305-7561'))
print("is 'hi dere' a phone number?")
print(isPhoneNumber('hi dere'))

message = 'Call me at 808-456-7890 or you can reach me at my office number at 808-972-4513'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk )

