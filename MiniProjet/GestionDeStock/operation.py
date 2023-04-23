def add_item(id: int, qte: int, title=" ", pu=0, qtmin=0):
    list_products = []
    add = False
    find = False
    with open("produits.csv", "r") as pds:
        for line in pds:
            list_products.append(line.split(','))
        for i in range(len(list_products)):
            if list_products[i][0] == id:
                list_products[i][3] = str(int(list_products[i][3]) + qte)
                find = True
                add = True
                break
        if not find:
            list_products.append([id, title, pu, qte, qtmin])
            add = True
    pds = open("produits.csv", "w")
    for tab in list_products:
        line = ",".join(tab)
        pds.writelines(line)
    pds.close()
    return add


def list_items():
    with open("produits.csv", "r") as pds:
        for line in pds:
            eclate = line.split(',')
            print("Title:", eclate[1], "Price:", eclate[2], "quantity:", eclate[3], "Minial quantity:", eclate[4])


def research(value, criteria):
    with open("produits.csv", "r") as pds:
        for line in pds:
            eclate = line.split(',')
            if criteria == 1:
                if eclate[1] == value:
                    print("Title:", eclate[1], "Price:", eclate[2], "quantity:", eclate[3], "Minial quantity:",
                          eclate[4])
                    break
            elif criteria == 2:
                if eclate[3] == value:
                    print("Title:", eclate[1], "Price:", eclate[2], "quantity:", eclate[3], "Minial quantity:",
                          eclate[4])
            elif criteria == 3:
                if eclate[1] == value:
                    print("Title:", eclate[1], "Price:", eclate[2], "quantity:", eclate[3], "Minial quantity:",
                          eclate[4])


def range_items():
    list_products = []
    lengh = 0
    with open("produits.csv", "r") as pds:
        for line in pds:
            list_products.append(line.split(','))
            lengh = len(list_products)
    for i in range(lengh):
        mini = i
        for j in range(i+1, lengh):
            if float(list_products[j][2]) < float(list_products[mini][2]):
                mini = j
        tem = list_products[i]
        list_products[i] = list_products[mini]
        list_products[mini] = tem
    for eclate in list_products:
        print("Title:", eclate[1], ", Price:", eclate[2], ", quantity:", eclate[3], ", Minimal quantity:", eclate[4])


def stock_value():
    with open("produits.csv", "r") as pds:
        price = 0
        for line in pds:
            eclate = line.split(',')
            price += float(eclate[2]) * float(eclate[3])
        return price


def delete(id):
    list_products = []
    rm = []
    find = False
    with open("produits.csv", "r") as pds:
        for line in pds:
            list_products.append(line.split(','))
        for i in range(len(list_products)):
            if list_products[i][0] == id:
                rm = list_products.pop(i)
                find = True
                break
    pds = open("produits.csv", "w")
    for tab in list_products:
        line = ",".join(tab)
        pds.writelines(line)
    pds.close()
    return find, ",".join(rm)


def sell(id, quantity):
    list_products = []
    sell = False
    with open("produits.csv", "r") as pds:
        for line in pds:
            list_products.append(line.split(','))
        for i in range(len(list_products)):
            if list_products[i][0] == id:
                if int(list_products[i][3]) >= quantity:
                    list_products[i][3] = str(int(list_products[i][3]) - quantity)
                    sell = True
                    break
    pds = open("produits.csv", "w")
    for tab in list_products:
        line = ",".join(tab)
        pds.writelines(line)
    pds.close()
    return sell
