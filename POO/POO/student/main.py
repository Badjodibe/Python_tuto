from student import *

""" 
ama = Student("Koffi", "Kodjo", "MIP", 19)
roger = Student("Roger", "Gouver", "BCG", 23)

ama.add_note(19)
ama.add_note(13)
ama.add_note(17)
ama.add_note(9)

print("La moyenne d'ama est:", ama.mean())
if ama.validate():
    print("Ama a valide l'année")
else:
    print("Ama n'as pas valider l'année")

notes = [9, 19, 17, 10]
for note in notes:
    roger.add_note(note)

print(ama.same_mean(roger))

print(voiture1.repr())
print(BMW.repr())
voiture1.marque_("Toyota")
print(BMW.repr())

voiture1 = BMW("bm1298894", "jaune", 150000)
voiture2 = BMW("BMW", "Noir", 300000)

print(voiture2)

print("Le prix de la voiture 2 est supérieur a celui de 1", voiture2 > voiture1)
print("Le prix de la voiture 2 est inferieur ou equal a celui de 1", voiture2 <= voiture1)
print(voiture2 == voiture1)
ama = Student("Koffi", "Kodjo", "MIP", 19)
"""

koffi = Identity("koffi", "Ma12442", "Togolaise", "Togo", 5, "Marié", "Enseignant")
print(koffi.ok())
