#1) solicitar ao usuário que digite seu nome

nome_valido = False 
salario_valido = False 
bonus_valido = False

while nome_valido is not True:
    try:
        nome_valido= input("Digite o seu nome: ")

        if len(nome_valido) == 0:
            raise ValueError("O nome não pode estar vazio.")
        elif nome_valido.isdigit():
            raise ValueError("O nome não deve conter números.")
        else:
            nome_valido = True
            print("Nome válido",nome_valido)
    except ValueError as e:
        print(e)

while salario_valido is not True:
    try:
        salario_valido = float(input("Digite o valor do seu salário: "))
        if salario_valido < 0:
            print("Por favor, digite um número positivo para o salário.")
        else:
            salario_valido = True
    except ValueError:
        print("Entrada inválida para o salário. Por favor, digite um número")

while bonus_valido is not True:
    try:
        bonus_valido = float(input("Digite o valor do bônus recebido: "))
        if bonus_valido < 0:
            print("Por favor, digite um valor positivo para o bônus.")
        else:
            bonus_valido = True
    except ValueError:
        print("Entrada inválida para o bônus. Por favor, digite um número")

bonus_recebido = 1000 + salario_valido * bonus_valido

print(f"{nome_valido}, seu salário é R${salario_valido:.2f} e seu bônus final é R$ {bonus_recebido}")