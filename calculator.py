
print("Bienvenue dans cet espace destiné à vos calculs")
print("Vous retrouverez ci-dessous les différentes opérations que nous possédons")
print (" 1. Addition_et_multiplication\n","2. soustraction_et_division\n","3. Division\n","4. Multiplication\n")
print("Quelle opération voulez-vous effectuer?")
opération = float(input())

print("Entrez votre 1ère valeur")
première_valeur = float(input())
print("Entrez votre 2nde valeur")
seconde_valeur = float(input())


def addition_et_multiplication(a,b,c): 
    A=(a+b)*c
    return A  

def soustraction_et_division(a,b,c):
    S=(a-b)/c
    return S

def division(a, b):
    D=a/b
    return D

def multiplication(a, b):
    M=a*b
    return M

if opération == 1: 
    print("Veuillez entrer une 3ème valeur")  
    troisième_valeur = float(input())
    print(f"le résultat de votre opération est {addition_et_multiplication(première_valeur,seconde_valeur,troisième_valeur)}")
    print("({première_valeur} + {seconde_valeur}) * {troisième_valeur} is {output}".format(première_valeur = première_valeur, seconde_valeur = seconde_valeur,troisième_valeur = troisième_valeur, output = addition_et_multiplication(première_valeur, seconde_valeur, troisième_valeur)))

if opération == 2:
    print("Veuillez entrer une 3ème valeur")  
    troisième_valeur = float(input())
    print(f"le résultat de votre opération est {soustraction_et_division(première_valeur, seconde_valeur,troisième_valeur)}")
    print("({première_valeur} - {seconde_valeur}) / {troisième_valeur} is {output}".format(première_valeur = première_valeur, seconde_valeur = seconde_valeur,troisième_valeur = troisième_valeur, output = soustraction_et_division (première_valeur, seconde_valeur, troisième_valeur)))


if opération == 3:
    print(f"le résultat de votre opération est {division(première_valeur, seconde_valeur)}")

if opération == 4:
    print(f"le résultat de votre opération est {multiplication(première_valeur, seconde_valeur)}")
