import os
import time
def limpaTela():
    os.system("cls")
def jogadores(desafiador, desafiado):
    nomesparti=[]
    nomesparti.append(desafiador)
    nomesparti.append(desafiado)
    return nomesparti
def dica(dica1, dica2, dica3):
    dica=[]
    dica.append(dica1)
    dica.append(dica2)
    dica.append(dica3)
    return dica
def desenhoforca(erros):
    print("  _______     ")
    print(" |/      |    ")
    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \ /   ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \ /   ")
        print(" |      /     ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \ /   ")
        print(" |      / \   ")
        print(" |            ")
    print(" |            ")
    print("_|___         ")
    print()










