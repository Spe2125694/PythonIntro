weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")

if unit.upper() == 'K':
    convert = float(weight) / 0.45
    print("Weight in Lbs: " + str(convert))
else:
    convert = weight * 0.45
    print("Weight in Kgs: " + str(convert))
