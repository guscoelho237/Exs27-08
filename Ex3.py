def  calcAreaTriangulo (base, altura):

    area = (base * altura) / 2
    return area

base = float(input("Insira o comprimento da base do triangulo: "))
altura = float(input("Insira a altura do triangulo: "))

area = calcAreaTriangulo(base, altura)
print(f"A area do triangulo é: {area:.2f}")