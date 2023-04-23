from operation import *
continuer = True
while continuer:
    print("Voici la liste des opérations possible choisissez un numero")
    print("1:Lister votre stock")
    print("2:Ajouter un produits")
    print("3:Rechercher un produit")
    print("4:Lister les produits rangés par quantité")
    print("5:Calculer la valeur du stock")
    print("6:Vendre un produit")
    print("7:Supprimer un produit")
    choix = int(input("\033[94mVotre choix:\033[0m"))
    if choix == 1:
        list_items()
    elif choix == 2:
        print("1: Le produit existe")
        print("2: C'est un nouveau produit")
        choix = int(input("\033[94mVotre choix:\033[0m"))
        id = input("Entrer d'identifiant du produit:")
        qte = input("Entrer la quantité á ajouter:")
        if choix == 1:
            add = add_item(id=id, qte=qte)
            if add:
                print("\033[92mVotre produit á été ajouter avec succes\033[0m")
        else:
            title = input("Entrer le libéle du produit:")
            price = input("Entrer le prix du produit:")
            qtmin = input("Entrer la quantité minimal du produit:")
            add = add_item(id=id, qte=qte, title=title, pu=price, qtmin=qtmin)
            if add:
                print("\033[92mVotre produit á été ajouter avec succes\033[0m")

    elif choix == 3:
        print("1:Par le nom")
        print("2: Par quantité")
        print("3: Qui sont dans la zone rouge")
        choix = int(input("\033[94mVotre choix:\033[0m"))
        valeur = input("Maintenant la valeur de recherche:")
        research(criteria=choix, value=valeur)
    elif choix == 4:
        range_items()
    elif choix == 5:
        print("\033[92mLa valeur du stock est:\033[0m", stock_value())
    elif choix == 6:
        iden = input("Entrer l'identifiant du produit á vendre")
        quantity = int(input("Maintenant la quantité a ventre"))
        sell = sell(iden, quantity)
        if sell:
            print("\033[92mVotre produit á vendu avec succes\033[0m")
        else:
            print("\033[91mUne erreur s'est produit la quantité n'est pas suffisante\033[0m")
    else:
        iden = input("Entrer l'identifiant du produit")
        delete, product = delete(iden)
        if delete:
            print("\033[92mVotre produit á été supprimé avec succès, le produit supprimer est {}\033[0m".format(product))
    continuer = bool(input("\033[94mVoulez vous effectué un autre traitement? si oui entre True sinon entrer "
                           "False:\033[0m"))










