def palindrome(mot):
    Y = 'est un palindrome.'
    N = 'n\'est pas un palindrome'

    C = mot
    C2 = C[::-1]
    l = [i for i in C]
    l2 = [i for i in C2]

    if C == C2:
        return Y

    else:
        return N

A = input('Entrez un mot : ')

X = palindrome(A)
print('Le mot \"',A,'\"',X)