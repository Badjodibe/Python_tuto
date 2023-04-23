for year in range(1900, 2024, 1):
    if ((year%4 == 0) and (year%400 != 0)):
        print("L'année ", year, "est une année bissextile")
    elif (year%400 == 0):
        print("L'année ", year, "est une année bissextile")
    else:
        print("L'année ", year, "n'est une année bissextile")
