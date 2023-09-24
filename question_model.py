import data
import random


escolhidos_lista = []
lista = data.question_data

def escolher_lista():
    def aleatorio():  
        tamanho_aleatorio = random.randint(0, len(lista) - 1)
        return tamanho_aleatorio
    escolhido = aleatorio()
    while escolhido in escolhidos_lista:
       escolhido = aleatorio()
    escolhidos_lista.append(escolhido)
    return escolhido

def escolher_pergunta():
    pergunta_valor = lista[escolher_lista()]
    return pergunta_valor
    


