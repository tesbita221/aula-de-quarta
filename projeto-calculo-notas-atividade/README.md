# Projeto Cálculo de Notas

## Objetivo

Este projeto foi desenvolvido para a atividade de **Testes Automatizados com Pytest e GitHub Actions**. O sistema realiza o cálculo da média de três notas e classifica a situação do aluno.

## Funções implementadas

### `calcular_media(nota1, nota2, nota3)`

Calcula a média aritmética de três notas.

- Aceita notas de 0 a 10.
- Retorna a média calculada.
- Gera `ValueError` quando alguma nota está fora do intervalo permitido.

### `verificar_situacao(media)`

Classifica o aluno de acordo com a média:

- Média maior ou igual a 7: **Aprovado**
- Média entre 5 e 6,99: **Recuperação**
- Média abaixo de 5: **Reprovado**
- Gera `ValueError` quando a média está fora do intervalo de 0 a 10.

## Testes automatizados

Foram desenvolvidos **7 casos de teste**, contemplando situações válidas e inválidas:

1. Cálculo de média com notas válidas.
2. Cálculo de média com notas baixas.
3. Aluno aprovado.
4. Aluno em recuperação.
5. Aluno reprovado.
6. Nota inválida utilizando `pytest.raises`.
7. Média inválida utilizando `pytest.raises`.

Os testes utilizam `assert` para verificar os resultados esperados.

## Como executar os testes localmente

Instale as dependências:

```bash
pip install -r requirements.txt
```

Depois execute:

```bash
pytest tests -v
```

## GitHub Actions

O workflow está em:

```text
.github/workflows/python-tests.yml
```

Ele é executado automaticamente a cada `push` no repositório. O workflow:

1. Usa um ambiente Linux (`ubuntu-latest`);
2. Baixa o código do repositório;
3. Configura o Python 3.13;
4. Instala as dependências do `requirements.txt`;
5. Executa os testes localizados no diretório `tests`.

A configuração segue a orientação da documentação oficial do GitHub para projetos Python com GitHub Actions e Pytest.

## O que acontece quando um teste falha?

Se algum teste falhar, o comando `pytest` retorna um código de erro. Com isso, o job do GitHub Actions é marcado como **falha**, e a execução aparece como reprovada na aba **Actions**.

Depois que o código for corrigido e um novo `push` for realizado, o workflow será executado novamente. Quando todos os testes passarem, a execução será marcada como **sucesso**.

## Resultado

**Testes locais: 7 testes aprovados.**

A execução na aba **Actions** depende do envio deste projeto para um repositório público no GitHub e de pelo menos um `push` no repositório.
