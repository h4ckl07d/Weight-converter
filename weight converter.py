weight = input("What is your weight: ")
unit = input("(L)bs or (k)g: ")

if unit.upper() == "L":
    conversion = 0.45 * int(weight)
    print(f'you are {conversion} kilogram')
elif unit.upper() == "K":
    conversion = int(weight) // 0.45
    print(f'you are {conversion} pounds')
else :
    print("error: invalid unit")