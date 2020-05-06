#! python3
# MAP = (SBP + 2*DBP)/3

sbp = input('What is the systolic blood pressure? ')
dbp = input('What is the diastolic blood pressure? ')

sbp = int(sbp)
dbp = int(dbp)

def mapCalc():
    map = (sbp + 2*dbp)/3
    return map

print(mapCalc())
