nombreAnneebix = 0
year = 2023
while(nombreAnneebix < 5):
    if ((year%4 == 0) and (year%400 != 0)):
        print("L'année ", year, "est une année bissextile")
        nombreAnneebix+= 1
    elif (year%400 == 0):
        print("L'année ", year, "est une année bissextile")
        nombreAnneebix+= 1
    else:
        print("L'année ", year, "n'est une année bissextile")
    year+=1

