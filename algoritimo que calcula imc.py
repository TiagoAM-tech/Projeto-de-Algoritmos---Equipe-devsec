# Solicita o peso e a altura ao usuário
print("Informe o peso (em kg): ")
peso = float(input())
print("Informe a altura (em metros): ")
altura = float(input())  # Corrigido para coletar a altura corretamente

# Calcula o IMC
imc = peso / altura ** 2

# Exibe o IMC
print(f"Índice IMC é: {imc:.2f}")

# Interpreta o IMC
print("INTERPRETAÇÃO DO IMC:")
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Peso normal")
elif 25 <= imc < 29.9:
    print("Sobrepeso")
elif 30 <= imc < 34.9:
    print("Obesidade grau I")
elif 35 <= imc < 39.9:
    print("Obesidade grau II")
else:
    print("Obesidade grau III")

