
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


def verificar_aprovacao(media):
    if media >= 6:
        return "Aprovado"
    else:
        return "Reprovado"


def gerar_relatorio(nome, media, situacao):
    print("\n--- RELATÓRIO DE DESEMPENHO ---")
    print(f"Aluno: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")


nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = calcular_media(nota1, nota2)
situacao = verificar_aprovacao(media)

gerar_relatorio(nome, media, situacao)

