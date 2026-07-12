import numpy as np

np.set_printoptions(suppress=True, precision=2)

matriz = []



while True:

    largura = float(input("Digite a largura: ").replace(",", "."))
    comprimento = float(input("Digite o comprimento: ").replace(",", "."))

    matriz.append([largura, comprimento])

    continuar = input("Deseja adicionar outro par? (s/n): ").lower()
    if continuar != "s":
        break

matriz = np.array(matriz)

print(matriz)

print("\nMedidas cadastradas:\n")

for i, (largura, comprimento) in enumerate(matriz, start=1):
    print(f"{i:02d} | Largura: {largura:8.2f} | Comprimento: {comprimento:8.2f}")