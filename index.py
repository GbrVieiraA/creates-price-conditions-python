# Sistema desenvolvido por [Gabriel Vieira De Abreu]
print("Sistema desenvolvido por Gabriel Vieira De Abreu")

# Solicita o valor base do plano e a idade do cliente
valorBase = float(input("Nos Informe o valor base do plano Por Gentileza: "))
idade = int(input("Confirme a idade do cliente: "))

# Inicializa a variável valorMensal
valorMensal = 0.0

# Aplica as regras de cálculo com base na idade
if 0 <= idade < 19:
    valorMensal = valorBase * (100 / 100)  # 100%
elif 19 <= idade < 29:
    valorMensal = valorBase * (150 / 100)  # 150%
elif 29 <= idade < 39:
    valorMensal = valorBase * (225 / 100)  # 225%
elif 39 <= idade < 49:
    valorMensal = valorBase * (240 / 100)  # 240%
elif 49 <= idade < 59:
    valorMensal = valorBase * (350 / 100)  # 350%
elif idade >= 59:
    valorMensal = valorBase * (600 / 100)  # 600%
else:
    print("Idade inválida.")

# Exibe o valor mensal do plano, se a idade for maior ou igual a 29
if idade >= 29:
    print(f"O valor mensal do plano é: R$ {valorMensal:.2f}")

