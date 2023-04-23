class Student:
    """
    This class is the abstraction of a student. it contains
    the following students information
    """
    student_number = 0

    def __init__(self, first_name, last_name, option, age):
        self.first_name = first_name
        self.last_name = last_name
        self.option = option
        self.age = age
        self.notes = []
        self.student_number += 1

    def mean(self):
        mean_ = 0
        for i in self.notes:
            mean_ += i
        return mean_/(len(self.notes))

    def add_note(self, note):
        self.notes.append(note)
        print("Note add with success")

    def validate(self):
        validate = False
        if self.mean() > 10:
            validate = True
        return validate

    def same_mean(self, student):
        same = False
        if self.mean() == student.mean():
            same = True
        return same


class BMW:

    marque = "BMW"
    prorietaire = "Allemagne"

    def __init__(self, immat, coul, prix):
        self.immatriculation = immat
        self.couleur = coul
        self.prix = prix


    @classmethod
    def repr(cls):
        return "la marque est " + cls.marque + " et le proprietaire est " + cls.prorietaire


    @classmethod
    def marque_(cls, marque):
        cls.marque = marque

    def __str__(self):
        return "La couleur de la voiture est " + self.couleur + "immatriculer " + self.immatriculation

    def __gt__(self, other):

        return self.prix > other.prix

    def __ge__(self, other):

        return  self.prix >= other.prix


class Identity:

    def __init__(self, n, num, nati, adr, d, at, pro):
        self.nom = n
        self.numero = num
        self.nationalite = nati
        self.dure = d
        self.adress = adr
        self._etat = at
        self.__profession = pro

    def __marie(self):
        return self._etat == "Marié"

    def _duree(self):
        return self.dure

    def ok(self):
        return self.__marie()








