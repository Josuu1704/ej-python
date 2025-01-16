vector =[]

for i in range(10):
    num = float(input(f"Dime un numero {i+1} del vector: "))
    vector.append(num)

valor_max = max(vector)

repeticion = vector.count(valor_max)

print(f"El valor maximo es: {valor_max} y se repite {repeticion} veces")