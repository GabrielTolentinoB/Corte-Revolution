import numpy as np
import math


# Função para ler números com ou sem vírgula, aceitando valores como 10 ou 10,50
# Isso evita erros caso o usuário não use ponto ou vírgula corretamente.
def ler_numero(mensagem):
    while True:
        texto = input(mensagem).strip().replace(" ", "")

        if "," in texto:
            texto = texto.replace(",", ".")

        try:
            valor = float(texto)
            return round(valor, 2)
        
        except ValueError:
            print("Valor inválido. Digite um número válido.")


#Isso aqui é para apenas aparecer duas casas decimais e não aparecer em notação científica
np.set_printoptions(suppress=True, precision=2)

#Essas são todas as listas que vão armazenar os valores inseridos, os resultados em metro quadrado e as sobras
TodosOsValoresInseridos = []
ResultadosEmMetroQuadrado = []
sobras = []

# O Programa principal começa aqui
while True:
    comando = input("O que você deseja fazer? (V = adicionar medidas, T = outra função, Q = sair): ").strip().lower()


    if comando == "v":
        print("Abrindo cadastro de medidas")
        while True:
            largura = ler_numero("Digite a largura: ")
            comprimento = ler_numero("Digite o comprimento: ")

            par_medida = [largura, comprimento]
            TodosOsValoresInseridos.append(par_medida)

            metro_quadrado = largura * comprimento
            ResultadosEmMetroQuadrado.append([largura, comprimento, metro_quadrado])

            continuar = input("Deseja adicionar outro par? (s/n): ").lower()
            if continuar != "s":
                break

        TodosOsValoresInseridos = np.array(TodosOsValoresInseridos)
        ResultadosEmMetroQuadrado = np.array(ResultadosEmMetroQuadrado)




    elif comando == "t":
         for i, (largura, comprimento, metro_quadrado) in enumerate(ResultadosEmMetroQuadrado, start=1):
            print(f"{i:02d} | Largura: {largura:8.2f} | Comprimento: {comprimento:8.2f} | m²: {metro_quadrado:8.2f}")









    elif comando == "q":
        print("Saindo...")
        break

    else:
        print("Comando inválido. Diqgite V, T ou Q.")


