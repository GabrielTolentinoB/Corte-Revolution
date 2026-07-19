import numpy as np
import tkinter as tk
import math



#Essas são todas as listas que vão armazenar os valores inseridos, os resultados em metro quadrado e as sobras
RevolutionMedidas = [] # Tecla R - Quantidade de medidas que seão geradas de revoltion
TodosOsValoresInseridos = [] # Tecla V - Todos os valores inseridos
ResultadosEmMetroQuadrado = [] # Tecla T - Resultados em metro quadrado
SobrasRevolution = [] # Tecla S - Sobras de Revolution
OrcamentoPecas = [] # Tecla O - Orçamento de peças

# Função para ler números com ou sem vírgula, aceitando valores como 10 ou 10,50
# Isso evita erros caso o usuário não use ponto ou vírgula corretamente.

Valor_Revolution = 1300.0

#formatando os números para duas casas decimais
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


def calcular_revolution(medidas):
    for largura, comprimento in medidas:
        if largura < 2:
            larguraSobra = 2 - largura #Deve ser colocada dentro da martriz Sobras
            SobrasRevolution.append([larguraSobra, comprimento])
            OrcamentoPecas.append([largura, comprimento])

        elif largura % 2 == 0:
            OrcamentoPecas.append([largura, comprimento])

        elif largura > 2:
            larguraNecessaria = math.ceil(largura / 2) * 2
            larguraSobra = larguraNecessaria - largura
            SobrasRevolution.append([larguraSobra, comprimento])
            OrcamentoPecas.append([largura, comprimento])

       
#Isso aqui é para apenas aparecer duas casas decimais e não aparecer em notação científica
np.set_printoptions(suppress=True, precision=2)



# O Programa principal começa aqui
while True:
    comando = input("O que você deseja fazer? (V = adicionar medidas, T = Dados Inseridos, S = Sobras, R = Revolution, Q = sair): ").strip().lower()

#Se o comando digitado for V, ele vai abrir o cadastro de medidas
    if comando == "v":
        print("Abrindo cadastro de medidas")
        while True:
            largura = ler_numero("Digite a largura: ")
            comprimento = ler_numero("Digite o comprimento: ")

            par_medida = [largura, comprimento]
            TodosOsValoresInseridos.append(par_medida)

            metro_quadrado = largura * comprimento
            ResultadosEmMetroQuadrado.append([largura, comprimento, metro_quadrado])

            calcular_revolution(TodosOsValoresInseridos)

            continuar = input("Deseja adicionar outro par? (s/n): ").lower()
            if continuar != "s":
                break

    elif comando == "s":
        print("Sobras de Revolution:")
        for i, (largura, comprimento) in enumerate(SobrasRevolution, start=1):
            print(f"{i:02d} | Largura: {largura:8.2f} | Comprimento: {comprimento:8.2f}")
#Comando para mostrar os resultados em metro quadrado e todos os valores inseridos
    elif comando == "t":
        for i, (largura, comprimento, metro_quadrado) in enumerate(ResultadosEmMetroQuadrado, start=1):
            print(f"{i:02d} | Largura: {largura:8.2f} | Comprimento: {comprimento:8.2f} | m²: {metro_quadrado:8.2f}")
    elif comando == "q":
        print("Saindo...")
        break
    else:
        print("Comando inválido. Digite V, T, S, R ou Q.")