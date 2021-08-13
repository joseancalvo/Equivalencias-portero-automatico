#Marcas de portero automático convencional
Tegui = "1-2-3-4-5"
Fermax = "4-3-1-2-6"
Golmar = "0-3-P1-5-10"
Alcad = "6-2-1-3-4"
Auta = "12-4-10-3-7"
Guinaz = "P-5-8-6-7"
Fringe = "4-1-2-3-6"
Bticino = "14-10-1-8-9"
Farfisa = "6-3-5-1-2"
Comelit = "1-4-P1-3-2"


print()
print(" ____________")
print("|            |")    
print("|            |    ______")
print("|            |   |      |")
print("|     %%     |   |  --  |")
print("|     %%     |   |      |")
print("|            |   |      |")
print("|            |   |      |")
print("|            |   |  ..  |")
print("|            |   |______|")
print("|____________|    S")
print("          S       S")
print("          S       S")
print("          SSSSSSSSS")

print()
print()
print("Equivalencias porteros 4+n")
print("Programado por Jose Angel Calvo")
print()
print()


viejo = str(input("¿Tu telefonillo es viejo o nuevo?"))
if viejo == "nuevo":
    print("Revise las conexiones, por favor")
    exit()

#Si el telefonillo se marca como nuevo, se da por finalizado el programa

#Menú para escoger la marca del telefonillo viejo
print()
print("Elige la marca del telefono instalado")
print("""
    1)Tegui
    2)Fermax
    3)Golmar
    4)Alcad
    5)Auta
    6)Guinaz
    7)Fringe
    8)Bticino
    9)Farfisa
    10)Comelit
""")

#Selecciona una opción
tfViejo = int(input("Introduce el número:"))

#Menú de la marca de telefonillo universal a instalar
print("Elige la marca del telefono a instalar")
print("""
    1)Tegui
    2)Fermax
    3)Golmar
    4)Alcad
    5)Auta
""")

#Selecciona una opción
tfNuevo = int(input("Introduce el número:"))

print()

#Dependiendo de la opción escogida se imprime en pantalla la marca escogida
print("Bornes teléfono instalado")
if tfViejo == 1:
    print(Tegui)

if tfViejo == 2:
    print(Fermax)

if tfViejo == 3:
    print(Golmar)

if tfViejo == 4:
    print(Alcad)

if tfViejo == 5:
    print(Auta)

if tfViejo == 6:
    print(Guinaz)

if tfViejo == 7:
    print(Fringe)

if tfViejo == 8:
    print(Bticino)

if tfViejo == 9:
    print(Farfisa)

if tfViejo == 10:
    print(Comelit)

#Dependiendo de la opción escogida se imprime en pantalla la marca escogida
print()
print("Bornes teléfono a instalar")

if tfNuevo == 1:
    print(Tegui)

if tfNuevo == 2:
    print(Fermax)

if tfNuevo == 3:
    print(Golmar)

if tfNuevo == 4:
    print(Alcad)

if tfNuevo == 5:
    print(Auta)

if tfNuevo == 6:
    print(Guinaz)

if tfNuevo == 7:
    print(Fringe)

if tfNuevo == 8:
    print(Bticino)

if tfNuevo == 9:
    print(Farfisa)

if tfNuevo == 10:
    print(Comelit)

print()
print("¡¡No olvides revisar!!")
print("el tipo de llamada y las masas")