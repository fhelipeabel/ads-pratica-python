# Sistema de controle de notas de alunos

# Função para adicionar as notas na lista
def adicionar_notas():
    notas = []
    print("--- Cadastro de Notas ---")

    # O While True aqui é importante para garantir que o ciclo continue aceitando novas entradas, até que o usuário digite o comsndo de parada ("s").
    while True:
        entrada = input("Digite uma nota de 0 a 10 (ou 's' para sair e gerar o relatório): ")
        
        # Condição de saída da repetição
        if entrada.lower() == 's':
            # Quando se usa o break, ele encerra este aninhamento e retorna ao aninhamento ou loop anterior, mas como aqui este loop não está aninhado à outro, ele simplismnte encerra o sistema e gera o relatório mesmo.
            break
            
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota) # Adiciona a nota à lista existente
        else:
            print("Valor inválido! Por favor, digite uma nota entre 0 e 10.")
            
    return notas

# Função para calcular a média das notas inseridas
def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

# Função com estrutura condicional para determinar a situação do aluno
def determinar_situacao(media):
    if media >= 7.0:
        return "Aprovado"
    else:
        return "Reprovado"

# Função para exibir o relatório final
def relatorio_final(notas, media, situacao):
    print("\n" + "="*30)
    print("       RELATÓRIO FINAL")
    print("="*30)
    print(f"Notas inseridas: {notas}")
    print(f"Média calculada: {media:.2f}")
    print(f"Situação do aluno: {situacao}")
    print("="*30)

# --- EXECUÇÃO PRINCIPAL DO PROGRAMA ---
notas_aluno = adicionar_notas()

if len(notas_aluno) > 0:
    media_aluno = calcular_media(notas_aluno)
    situacao_aluno = determinar_situacao(media_aluno)
    relatorio_final(notas_aluno, media_aluno, situacao_aluno)
else:
    print("\nNenhuma nota foi inserida... O relatório não pode ser gerado.")