'''module qui permet de déterminer si un nombre est premier ou non'''
from math import sqrt

#### Fonction secondaire


def isprime(p):

    # votre code ici
    '''
    retourne un booléen, vrai si le nombre passé en paramètre 
    est premier et faux dans le cas contraire
    '''
    premier = True
    s = int(sqrt(p))
    if p==1:
        premier = False
    for i in range(2,s+1):
        if p%i == 0:
            premier=False
            break
    return premier

#### Fonction principale


def main():
    '''permet de faire des appels de la fonction isprime()'''
    # vos appels à la fonction secondaire ici
    print(isprime(5))
    print(isprime(57))
    print(isprime(95))

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
