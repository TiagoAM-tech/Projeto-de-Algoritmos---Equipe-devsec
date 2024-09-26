# Algoritmo que calcula a média de 30 alunos

# Inicializa o contador de alunos com o valor 1
cont = 1

# Define a constante QTDALUNOS com o número total de alunos (30)
QTDALUNOS = 30

# Inicia um loop 'while' que será executado enquanto o contador for menor ou igual a QTDALUNOS
while cont <= QTDALUNOS:
    # Exibe uma mensagem indicando qual aluno está sendo processado no momento
    print(f"\nVamos calcular a média do aluno {cont}")
    
    # Solicita a primeira nota do aluno e converte o valor de entrada para um número decimal (float)
    nota1 = float(input(f"Digite a nota 1 do aluno {cont}: "))
    
    # Solicita a segunda nota do aluno
    nota2 = float(input(f"Digite a nota 2 do aluno {cont}: "))
    
    # Solicita a terceira nota do aluno
    nota3 = float(input(f"Digite a nota 3 do aluno {cont}: "))
    
    # Calcula a média das três notas
    media = (nota1 + nota2 + nota3) / 3
    
    # Exibe a média do aluno formatada com duas casas decimais
    print(f"A média do aluno nº {cont} é: {media:.2f}")
    
    # Verifica se o aluno está aprovado ou reprovado
    if media >= 6:
        print("O aluno está aprovado!")
    else:
        print("O aluno está reprovado!")
    
    # Incrementa o contador 'cont' em 1 para passar para o próximo aluno
    cont += 1


    