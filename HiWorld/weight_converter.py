weight=int(input("Weight: "))
units=input("Is this lbs or kg pls enter 'l' or 'k': ")

if units.lower() == 'l':
    converted_weight= weight *.45
    print(f"This is your weight '{converted_weight}' in kg")
if units.lower() =='k':
    converted_weight=weight/.45
    print(f"This is your weight '{converted_weight}' in lbs")

