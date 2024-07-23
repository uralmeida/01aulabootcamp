

bonus_constante = 1000

# 1) Solicita ao usuário que digite seu nome

nome_usuario = input("Digite o seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário

salario = float(input("Digite seu salário: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido

valor_bonus = float(input("Digite o valor do seu bonus: "))

# 4) Calcule o valor do bônus final

bonus_valor = bonus_constante + salario * valor_bonus

# 5) Imprime a mensagem personalizada incluindo o nome do usuário e o valor do bonus

print(f"{nome_usuario}, o valor do seu bonus é de {bonus_valor}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?

