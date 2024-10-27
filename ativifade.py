print(f"\n{'-' * 20} olá, professores! {'-' * 20}")
print(f"\n{'-' * 23} Notas finais{'-' * 23}")

def calcular_nota_final(n1, n2):
    return (0.4 * n1 + 0.6 * n2) / 2

# Solicitar a quantidade de alunos
quantidade_alunos = int(input("Digite a quantidade de alunos, em sua matéria: "))

# Lista para armazenar os dados dos alunos
alunos = []

# Loop para coletar os dados de cada aluno
for i in range(quantidade_alunos):
    nome = input(f"\nDigite o nome do aluno {i + 1}: ")
    n1 = float(input(f"Digite a nota 01 (N1) de {nome}: "))
    n2 = float(input(f"Digite a nota 02 (N2) de {nome}: "))
    
    # Calcular a nota final
    nota_final = calcular_nota_final(n1, n2)

# Criar dicionário com os dados do aluno
    aluno = {
'numero': i + 1,  # Número do aluno
        
 
'nome': nome,     # Nome do aluno
        'n1': n1,         # Nota 01
        'n2': n2,         # Nota 02
        'nota_final': nota_final,  # Nota final ponderada
        'status': 'Aprovado' if nota_final >= 6 else 'Reprovado'  # Status de aprovação
    }
    
    # Adicionar o aluno à lista
    alunos.append(aluno)

    
# Imprimir a tabela de resultados
print(f"\n{'Número':<10} {'Nome':<20} {'Nota 01':<10} {'Nota 02':<10} {'Nota Final':<10} {'Status':<10}")
print("-" * 80)
for aluno in alunos: 
 print(f"{aluno['numero']:<10} {aluno['nome']:<20} {aluno['n1']:<10} {aluno['n2']:<10} {aluno['nota_final']:<10.2f} {aluno['status']:<10}")