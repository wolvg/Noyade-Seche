def distance_hamming(mot1,mot2):
    distance = 0
    L=len(mot1)
    L2=len(mot2)
    if L == L2:
        for i in range(L):
            if mot1[i] != mot2[i]:
                distance += 1
        return distance
    else:
        print('Attention : Les 2 mots doivent êtres de la même longueur !!')

A = input('Entrez un premier mot : ')
B = input('Entrez un deuxième mot qui comporte le même nombre de lettre : ')

X = distance_hamming(A,B)
print('La distance de Hamming entre', A, 'et', B, '=', X)