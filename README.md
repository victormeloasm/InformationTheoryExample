
# Calculadora de Entropia da Teoria da Informação

Este repositório contém uma implementação em Python da equação de Shannon para calcular a entropia de uma fonte de informação. A entropia é uma medida da incerteza ou da quantidade média de informação transmitida por símbolo em um sistema de comunicação.

## Equação de Shannon

A equação de Shannon é dada por:

```
H(X) = -Σ P(x_i) * log2(P(x_i))
```

- `H(X)`: Entropia da fonte de informação.
- `P(x_i)`: Probabilidade de ocorrência do símbolo `x_i`.
- `log2`: Logaritmo na base 2.

## Como Usar

1. Clone este repositório:

```bash
git clone https://github.com/victormeloasm/InformationTheoryExample.git
```

2. Navegue para o diretório clonado:

```bash
cd InformationTheoryExampl
```

3. Execute o script Python para calcular a entropia da fonte de informação:

```bash
python ExampleEntropy.py
```

4. Insira as probabilidades dos símbolos quando solicitado.

## Exemplo

Vamos gerar aleatoriamente seis símbolos e suas probabilidades associadas e, em seguida, calcular a entropia da fonte de informação. Execute o script e insira as probabilidades quando solicitado.

## Dependências

Este projeto requer o Python 3 e a biblioteca NumPy. Você pode instalá-la com o seguinte comando:

```bash
pip install numpy
```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) e enviar solicitações de pull (pull requests) para aprimorar este projeto.

## Licença

Este projeto está sob a [Licença MIT](LICENSE).
