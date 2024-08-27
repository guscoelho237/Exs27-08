def contador(inicio, fim, passo):
    
    if passo == 0:
        print("O passo não pode ser 0.")
        return
    
    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ')
    else:
        for i in range(inicio, fim - 1, -passo):
            print(i, end=' ')
    print()

# Contagem exemplo 1: de 1 até 10, de 1 em 1  
contador(1, 10, 1)

# Contagem exemplo 2: de 10 até 0, de 2 em 2
contador(10, 0, 2)