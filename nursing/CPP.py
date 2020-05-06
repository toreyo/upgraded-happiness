#! python3

# CPP = MAP - ICP
print('''CPP ref range: 60-80 mmHg.
CPP < 60 = risk of neural injury from cerebral hypoperfusion. 
NI: Bring MAP up w/vasopressors or lower CPP via mannitol or elevating head of bed. 
''')

sbp = input('What is the systolic blood pressure? ')
dbp = input('What is the diastolic blood pressure? ')

sbp = int(sbp)
dbp = int(dbp)

map = (sbp + 2*dbp)/3
map = int(map)

icp = input('What is the ICP? ')
icp = int(icp)

cpp = map - icp
print('Your cranial perfusion pressure is ' + cpp)

