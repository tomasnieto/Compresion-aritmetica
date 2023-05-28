import math

flag = True
distribucion = []
input = ""
suma = 0
with open("funcion.txt", "r") as r:
    for linea in r:
        if flag:
            input = linea
            flag = False
            continue
        letra, prob = linea.strip().split(" ")
        prob = float(prob)
        suma += prob
        distribucion.append((letra, suma))

print(input)
print(distribucion)

intervalo = (0, 1)
for letra in input:
    print(intervalo)
    indice =  0
    prob = 0
    for elemento in distribucion:
        if elemento[0] == letra:
            prob = elemento[1]
            break
        else:
            indice += 1 
    if indice == 0:
        intervalo = (intervalo[0], intervalo[0] + (intervalo[1]-intervalo[0]) * prob)
    
    else:
        prob_anterior = distribucion[indice - 1][1]
        intervalo = (intervalo[0] + (intervalo[1]-intervalo[0]) * prob_anterior, intervalo[0] + (intervalo[1]-intervalo[0]) * prob)

intervalo = (intervalo[1], intervalo[0])
bits_necesarios = math.ceil(math.log2(1/(intervalo[1] - intervalo[0]))) + 1
print(bits_necesarios)

binary = ""
decimal = intervalo[0]
while decimal > 0:
    decimal *= 2
    binary += str(int(decimal))
    decimal -= int(decimal)

print(binary[:bits_necesarios])


    


