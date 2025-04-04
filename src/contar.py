
from imprimir import imprimir_ronda
def contar_rondas (rounds):
    final = {}
    for round in rounds: 
        for personaje, datos in round.items():

            #Si no cree el dicc del personaje
            if personaje not in final:
                final[personaje] = {'kills': 0, 'assists': 0,'deaths': 0}

            #Aumento los datos 
            final[personaje]['kills'] += datos['kills']
            final[personaje]['assists'] += datos['assists']
            if datos['deaths'] == True: 
                final[personaje]['deaths'] += datos['deaths']
    return final