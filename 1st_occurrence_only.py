
def recherche_naif(chain, schain):
    """ recherche d'un motif donner dans un chain donner avec l'algorithme naïf"""
    # mettez nos chaînes en majuscules
    chain = chain.upper()
    schain = schain.upper()
 

    # calculer la taille des chaînes
    len_chain = len(chain)
    len_schain = len(schain)

    # le compteur
    nb_com = 0

    i = 0
    # tq'on a des caractère à comparer on boucle
    while (i < len_chain - len_schain + 1):
        j = 0

        # tq le carracter de la chain = le carracter de motif on boucle
        while (j < len_schain) and (chain[i+j] == schain[j]):
            j += 1

        nb_com = nb_com + (j+1)

        # si on trouve la 1er occurrence de motif dans la chain on return la position
        if j == len_schain:
            return i

        i += 1



def fun_bords(schain):
    """ calculer des bords """
    schain = schain.upper()
    len_schain = len(schain)
    bord = []

    # initialisation des tableaux des bords avec des vide
    for pos in range(0, len_schain+1):
        bord.append(None)

    i = -1
    bord[0] = -1
    # calculé de valeur et remplir le tableau
    for j in range(0, len_schain):
        while i >= 0 and schain[i] != schain[j]:
            i = bord[i]
        i += 1

        bord[j+1] = i

    return bord


def fun_mp_v2(chain, schain):
    """ recherche d'un motif donner dans un chain donner avec l'algorithme de morris prete"""
   
    # mettez nos chaînes en majuscules
    chain = chain.upper()
    schain = schain.upper()


    # calculer la taille des chaînes
    len_chain = len(chain)
    len_schain = len(schain)

    # le compteur
    nb_com = 0

    # calculer de bord do motif
    bord = fun_bords(schain)

    i = 0
    j = 0

    while i < len_chain - len_schain+1:
        while j < len_schain and chain[i+j] == schain[j]:
            j += 1
            nb_com += 1
        # si on trouve la 1er occurrence de motif dans la chain on return la position
        if j == len_schain:
            return i

        i = i+j-bord[j]
        if bord[j] > 0:
            j = bord[j]
        else:
            j = 0
        nb_com += 1



def fun_mil_bord(schain):
    """ calculer des meilleur bords"""

    schain = schain.upper()
    len_schain = len(schain)
    mil_bord = []

    # initialisation des tableaux des bords avec des vide
    for pos in range(0, len_schain+1):
        mil_bord.append(None)

    mil_bord[0] = -1
    i = -1

    # calculé de valeur et remplir le tableau
    for j in range(0, len_schain):
        while (i >= 0) and (schain[i] != schain[j]):
            i = mil_bord[i]

        i += 1
        try:
            if (i == len_schain-1) or (schain[j+1] != schain[i]):
                mil_bord[j+1] = i
            else:
                mil_bord[j+1] = mil_bord[i]
        except IndexError:

            if (i == len_schain-1) or ("" != schain[i]):
                mil_bord[j+1] = i
            else:
                mil_bord[j+1] = mil_bord[i]

    return mil_bord


def fun_kmp(chain, schain):
    """ recherche d'un motif donner dans un chain donner avec l'algorithme de Knuth-Morris-Pratt """

    # mettez nos chaînes en majuscules
    chain = chain.upper()
    schain = schain.upper()

    # calculer la taille des chaînes
    len_chain = len(chain)
    len_schain = len(schain)

    # le compteur
    nb_com = 0

    # calculer de bord do motif
    mil_bord = fun_mil_bord(schain)

    i = 0
    j = 0

    while i < len_chain-len_schain+1:
        while j < len_schain and chain[i+j] == schain[j]:
            j += 1
            nb_com += 1
        # si on trouve la 1er occurrence de motif dans la chain on return la position
        if j == len_schain:
           
            return i
        i = i+j-mil_bord[j]

        if mil_bord[j] > 0:
            j = mil_bord[j]
        else:
            j = 0

        nb_com += 1


def fun_rk(chain, schain):
    """ recherche d'un motif donner dans un chain donner avec l'algorithme de rabin karp"""

    # mettez nos chaînes en majuscules
    schain = schain.upper()
    chain = chain.upper()
    # l'alphabet est le poid de cheque letter
    alpha = {
        "A": 1,
        "T": 4,
        "C": 2,
        "G": 3
    }

    # nombre premier
    q = 2147483647

    # calculer la taille des chaînes
    len_shcain = len(schain)
    len_chain = len(chain)

    my_schain_hash = 0  # hash de motif
    my_text_hash = 0  # hash de n carracter de la chain

    nb_com = 0
    # calculer de 1er fenêtre
    for i in range(0, len_shcain):
        my_schain_hash = (4*my_schain_hash + alpha[schain[i]]) % q
        my_text_hash = (4*my_text_hash + alpha[chain[i]]) % q

    for i in range(len_chain-len_shcain + 1):
        # text found
        if my_schain_hash == my_text_hash:
            # tester le text carrecter par carrcter
            if chain[i:i+len_shcain] == schain[::]:
                return i

        # text not found
        # recalculer le hash de text avec le carrecter svuiant
        if i < len_chain-len_shcain:
            nb_com += 1
            my_text_hash = (
                (my_text_hash - (alpha[chain[i]] * 4**(len_shcain-1)))*4 + alpha[chain[i+len_shcain]]) % q

