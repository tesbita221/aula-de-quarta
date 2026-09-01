def calcular_media(nota1, nota2, nota3):
    """Calcula a média aritmética de três notas."""
    notas = (nota1, nota2, nota3)

    if any(nota < 0 or nota > 10 for nota in notas):
        raise ValueError("A nota deve estar entre 0 e 10.")

    soma = sum(notas)
    return soma / len(notas)


def verificar_situacao(media):
    """Classifica o aluno conforme a média informada."""
    if not 0 <= media <= 10:
        raise ValueError("A média deve estar entre 0 e 10.")

    if media >= 7:
        return "Aprovado"
    if media >= 5:
        return "Recuperação"
    return "Reprovado"
