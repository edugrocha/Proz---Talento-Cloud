# -*- coding: utf-8 -*-
"""ATIVIDADE6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KKiallQE-V-i1oZLeZnfBtRzHFxE8M3Y
"""

print("Digite seu nome")
nome = input()

executar = True

while executar:
    print("Digite o ano do seu nascimento:")
    try:
        ano = int(input())
        if ano < 1922 or ano > 2021:
            print("Precisa ser entre os anos de 1922 e 2021.")
        else:
            idade = 2022 - ano
            print(nome, "completará ou completou", idade, "anos de idade em 2022")
            executar = False
    except ValueError:
        print("Utilize apenas números para escrever os anos.")