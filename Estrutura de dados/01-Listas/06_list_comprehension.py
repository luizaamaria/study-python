numeros = [0, 2, 10, 45, 87, 3, 9]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
        
########################################

pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)
