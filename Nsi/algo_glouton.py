def CalculateEquivalent(x, one_value):
    r = x/one_value
    return r

def GiveBackMostLittle(amount, possibilities):
    """
        amount: It's the amount to give | It can be float() or int() \n
        possibilities: It's how we can give it. | It's a list
    """

    if type(possibilities) is list:
        used = []
        while amount != 0:
            for i in range(1, len(possibilities)+1):
                if possibilities[-i] <= amount:
                    used.append((possibilities[-i], amount//possibilities[-i])) # Just used to have statistics
                    amount -= possibilities[-i]*(amount//possibilities[-i])
        print(used, amount)

def PickMostObjects(limit, inv):
    sort = False
    status = 0
    taken = []; indices = []
    for obj in inv:
        if len(indices) != len(inv):
            indices.append([obj[1], inv.index(obj)])
    indices.sort()
    for obj_weight in indices:
        if status+obj_weight[0] <= limit:
            status += obj_weight[0]
            taken.append(inv[obj_weight[1]])
    print(f"For a weight of: {status} kg, we took:")
    for obj in taken:
        print(f"\t- {obj[0]}")

def PickMostValuableObjects(limit, inv):
    sort = False
    status = 0; value = 0
    taken = []; indices = []
    for obj in inv:
        if len(indices) != len(inv):
            indices.append([obj[2], obj[1], inv.index(obj)])
    indices.sort()
    indices.reverse()
    for obj_data in indices:
        if status+obj_data[1] <= limit:
            status += obj_data[1]
            value += obj_data[0]
            taken.append(inv[obj_data[2]])
    print(f"For a value of: {value}$ with a size limit of {limit}kg, we took:")
    for obj in taken:
        print(f"\t- {obj[0]}")
    print(f"We've taken {len(taken)} objects with us")

def SetSendingOrder(to_send, order):
    """
        to_send: a list with the files to send | Compisition required: (name, size) \n
        order: one of the three possibilities: \n
        \t- 'crois' for a croissant order \n
        \t- 'decrois' for a reversed croissant order \n
    """
    print(to_send, "\n\n\n")
    to_send_sorted = []; to_send_temp = []
    if order == "crois" or order == "decrois":
        for elem in to_send:
            to_send_temp.append([elem[1], to_send.index(elem)])
        to_send_temp.sort()
        for final_elem in to_send_temp:
            to_send_sorted.append(to_send[final_elem[1]])
        if order == "crois":
            return to_send_sorted
        else:
            to_send_sorted.reverse()
            return to_send_sorted
    else:
        return to_send

def SendMostLittleMails(to_send, size_limit):
    pass




#print(CalculateEquivalent((2*741-1000), 0.14))
print("Exercice 1:\n\tIl me rend:", 2*741-1000, "Ƀ")
money_possibilities = [1, 3, 7, 31, 47, 223, 741]
inventory = [ ### Composition: ("Name", weight, price)
    ("Service à thé", 1.3, 1000), ("Bibelot", 0.35, 400), ("Appareil Photo", 1.385, 2500),
    ("Statuette en Porcelaine", 0.475, 1080), ("Autre statuette", 0.645, 950), ("Bols gravés", 0.325, 1020),
    ("Service cuillers en céramique", 0.348, 520), ("Traducteur électronique", 0.450, 890), ("Bouteille de Kombutcha", 1.118, 250)]
videos_to_send = [ ### Composition: ("Name", file_size (Mo))
    ("Visite de l'aéroport", 785), ("Visite d'un temple", 1225), ("Plus grand tobogan du monde", 385), ("Marché", 150),
    ("Petit déjeuner", 1465), ("Rencontre avec Naja", 75), ("Cours après la rencontre", 1125), ("Musée du ticket de métro", 1378),
    ("Nage avec les raies", 425), ("Visite de la capitale", 505)]
#print()
GiveBackMostLittle(2*741-1000, money_possibilities)
PickMostObjects(5, inventory)
PickMostValuableObjects(5, inventory)
print(SetSendingOrder(videos_to_send, "decrois"))
