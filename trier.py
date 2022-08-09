print("combien de nombres voulez-vous saisir?")
even_count, odd_count = 0, 0
numbre_entres = int(input())
entres = []
for i in range(1,  numbre_entres+1):
    print("Saisir entre numero {}".format(i))
    entres.insert(i-1, int(input())) # entres[i-1] = input()
print(entres)

for i in entres:
    if i % 2 == 0:
        #print("Ce nombre est pair")
        even_count += 1 
    else:
        # print("Ce nombre est impair")
        odd_count += 1

print(f"Le nombre de pair est de: {even_count}" )
print(f"Le nombre d'impair est de: {odd_count}" )

    

