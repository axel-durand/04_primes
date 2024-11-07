from math import sqrt

#### Fonction secondaire


def isprime(p):

    # votre code ici
premier = True
s = int(math.sqrt(p))
for i in range(2,s+1):
if p%i == 0:
    premier=False
    
return premier
    pass

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
