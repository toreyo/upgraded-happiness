#! python3

print('''The ranges of BMI are as followed: 

Underweight: 18.5 or lower
Normal: 18.5 - 24.9
Overweight: 25.0 - 29.9
Obese: 30.0 - 34.9
Severely Obese: 35.0 -39.9
Morbidly Obese: 40.0 or greater ''')
print('-'*70)



ht = input('''Please input your height in inches. (eg. if 5'8" please enter 5.8) : 
''')
wt = input('''Please enter your weight in lbs (eg. if 145 lbs please enter 145) : 
''')

def BMICalc():
    '''takes first value (feet), converts it to inches and adds it with second value (inches) to give total height in inches'''
    htInch = ht.split('.')
    htFeet = int(htInch[0]) * 12
    htTotal = htFeet + int(htInch[1])
    BMI = int(wt) * 703 // int(htTotal) **2
    if BMI < 18.5:
        return(f"your BMI is {BMI}, you're underweight.. Don't forget to eat pls.. ")
    elif 18.5 < BMI < 24.9:
        return((f"your BMI is {BMI}, you are normal weight :) "))
    elif 25 < BMI < 29.9:
        return(f"your BMI is {BMI}, getting up there buddy... ")
    elif BMI > 30:
        return(f"your BMI is {BMI}, yo..careful what you're eating..let's exercise with torey :)")

print(BMICalc())












