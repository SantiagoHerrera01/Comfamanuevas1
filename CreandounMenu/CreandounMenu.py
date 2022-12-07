opcion=100

print("Empanadas el machetico")
print("************************\n")

print("1. Registrar Empanada ")
print("2. Ver Empanada ")
print("0. SALIR ")


empanadas=[]
while opcion != 0:
    opcion=int(input("Digita una opcion: "))
    
    if opcion==1:
        empanada=input("Digite el nombre de la empanada: ")
        empanadas.append(empanada)

    elif opcion==2:
        for empanada in empanadas:
            empanada.pop(1)
            print (f'La empanada que selecciono es: {empanada}')  
    elif opcion==0:
        print("Gracias por comprar, Vuelva pronto...")
        break
    else:
        print("Selecionar opcion valida...")

