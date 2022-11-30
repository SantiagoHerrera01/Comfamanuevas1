#entradas del prblema
niveldeagua = int(input("Digita el nivel de agua: "))

#evaluando caminos multiples
if niveldeagua<=100:
    print ("Bajo nivel de agua")
elif niveldeagua >100 and niveldeagua <400:
    print ("Operación optima")
elif niveldeagua<=400:
    print("peligro")
else:
    print("Nivel de agua no valido ")