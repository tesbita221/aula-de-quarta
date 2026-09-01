import pytest

from calculo_notas import calcular_media, verificar_situacao


def test_calcular_media_com_notas_validas():
    assert calcular_media(8, 7, 9) == 8


def test_calcular_media_com_notas_baixas():
    assert calcular_media(5, 6, 4) == 5


def test_aluno_aprovado():
    assert verificar_situacao(8) == "Aprovado"


def test_aluno_em_recuperacao():
    assert verificar_situacao(6) == "Recuperação"


def test_aluno_reprovado():
    assert verificar_situacao(4) == "Reprovado"


def test_nota_invalida():
    with pytest.raises(ValueError):
        calcular_media(8, 11, 7)


def test_media_invalida():
    with pytest.raises(ValueError):
        verificar_situacao(12)
