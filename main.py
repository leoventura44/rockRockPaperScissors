# Pedra, Papel e Tesoura

import random


def jogo():
    usuario = input('digite "P" para PEDRA, "A" para PAPEL ou "T" para TESOURA:\n')
    computador = random.choice(['P', 'A', 'T'])

    if usuario == computador:
        return 'EMPATE'

    # P > T, T > A, A > P
    if vitoria(usuario, computador):
        return 'VOCÊ GANHOU!'

    return 'VOCÊ PERDEU!'


def vitoria(jogador, oponente):
    if (jogador == 'P' and oponente == 'T') or (jogador == 'T' and oponente == 'A') \
            or (jogador == 'A' and oponente == "P"):
        return True


print(jogo())
