def evaluar(peso, estatura, edad):
    # TODO: Coloca aquí el código del ejerciccio 8: Índice de masa corporal
     imc = peso / (estatura ** 2)
    if imc < 18.5:
        return "bajo"
    elif 18.5 <= imc < 24.9:
        return "medio"
    else:
        return "alto"

if __name__ == '__main__':
    print("Peso:", end="")
    peso = int(input())
    print("Estatura:", end="")
    estatura = float(input())
    print("Edad:", end="")
    edad = int(input())
        
    respuesta = evaluar(peso, estatura, edad)
    print(respuesta)
