def calcReajuste(salario):
    if salario > 5000:
        return salario * 1.10
    else: 
        return salario * 1.15
    
salario = float(input("Insira o salario atual: R$"))
novoSalario = calcReajuste(salario)
print(f"Novo salario após o reajuste: R${novoSalario:.2f}")