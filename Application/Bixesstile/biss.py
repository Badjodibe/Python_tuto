
year = int(input("Entrer une année:"))
if ((year%4 == 0) and (year%400 != 0)):
    print("L'année ", year, "est une année bissextile")
elif (year%400 == 0):
    print("L'année ", year, "est une année bissextile")
else:
    print("L'année ", year, "n'est une année bissextile")

