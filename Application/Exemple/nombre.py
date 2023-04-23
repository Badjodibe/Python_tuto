import numpy as np # télécharger numpy 
nombre = np.random.randint(low= 0, high= 100) # cette instruction génère un nombre aléatoire compris entre 0 et 100
monNombre = 0
while(monNombre!=nombre):
    if(monNombre > nombre):
        print("Votre nombre est superieur au nombre a deviner")
    elif(monNombre < nombre):
        print("Votre nombre est inferieur au nombre a deviner")
    monNombre = int(input("Entrer un autre nombre:"))
print("Bravo vous avez trouver le nombre et c'est:", monNombre)
