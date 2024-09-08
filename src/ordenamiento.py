def evaluar(numero1, numero2, numero3, numero4):
    # TODO: Coloca aquí el código del ejeercicio 5: Ordenamiento
   for i in range(4):
        num = int(input(f"Ingrese numero {i+1}: "))
        numeros.append(num)

    numeros.sort()
    
    print("Números ordenados de menor a mayor:")
    for num in numeros:
        print(num, end=" ")

if __name__ == '__main__':
    print("Número 1:", end="")
    numero1 = int(input())
    print("Número 2:", end="")
    numero2 = int(input())
    print("Número 3:", end="")
    numero3 = int(input())
    print("Número 4:", end="")
    numero4 = int(input())
        
    respuesta = evaluar(numero1, numero2, numero3, numero4)
    print(respuesta)
