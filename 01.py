
########## Strings ##########

nome = "LuiZa"

print(nome.upper())

print(nome.lower())

print(nome.title())

texto = "  Ola, meu nome é Luiza    "

print(texto.strip() + "!")

print(texto.lstrip() + "!")

print(texto.rstrip() + "!")

menu = "Pizza"

print("####" + menu + "####")
print(menu.center(20))
print(menu.center(20, "-"))
print("-".join(menu))
print(menu.ljust(20))


########## Fatiamento de Strings ##########

nome = "Luiza Marques"

print(nome[0])
print(nome[:5])
print(nome[:4])
print(nome[6:])
print(nome[6:13])
print(nome[6:13:2])
print(nome[:])
print(nome[::-2])

