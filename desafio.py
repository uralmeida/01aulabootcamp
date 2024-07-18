# Bonus constante

constante_bonus = 1000

# 1) Solicite ao usuário que digite seu nome

nome_usuario = input("Digite seu nome: ")

# 2) Solicite ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

salario_usuario = float(input("Digite o valor do seu salário: "))

# 3) Solicite ao usuário que digite o valor do bônus recebido 
# Converte a entrada para um número de ponto flutuante

bonus_usuario = float(input("Digite o valor do bônus recebido: "))

# 4) Calcule o valor do bônus final

valor_do_bonus = constante_bonus + salario_usuario * bonus_usuario


# 5) Imprime a mensagem personalizada incluindo o nome de usuário , sálario e bônus
# f quando for ter variáveis

print(f"O usuário {nome_usuario} possui o bonus de {valor_do_bonus}")

# Bônus: quantos bugs e riscos você consegue identificar nesse programa?





