
nom = "baba"
password = "$_y12"
nomN = input("Entrer votre nom d'utilisateur:")
passwordN = input("Enter votre mot de pass")
if(nomN == nom) and (passwordN==password):
    print("Voici votre espace")
else:
    print("Authenfication echoué")


n = int(input("Entre un nombre:"))
if n < 0:
    print("Ce nombre est negatif")
else:
    print("ce nombre est positif")
