import numpy as np

# Defina uma função para calcular a entropia de uma fonte de informação
def calcular_entropia(probabilidades):
    return -np.sum(probabilidades * np.log2(probabilidades))

# Gere símbolos aleatórios e suas probabilidades associadas
num_simbolos = 6
simbolos = [f'S{str(i)}' for i in range(num_simbolos)]
probabilidades = np.random.rand(num_simbolos)
probabilidades /= probabilidades.sum()  # Normaliza as probabilidades para somarem 1

# Calcule a entropia da fonte de informação
entropia = calcular_entropia(probabilidades)

# Exiba os símbolos, suas probabilidades e a entropia
for simbolo, prob in zip(simbolos, probabilidades):
    print(f'Símbolo: {simbolo}, Probabilidade: {prob:.4f}')
print(f'Entropia da fonte de informação: {entropia:.4f} bits por símbolo')
