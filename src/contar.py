def contar_rondas (round):
    final = {}
    for personaje, datos in round:
        #Si no cree el dicc del personaje
        if personaje not in final:
            final[personaje] = {'kills': 0, 'assists': 0,'deaths': 0}

        #Aumento los datos 
        final[personaje]['kills'] += datos['kills']
        final[personaje]['assists'] += datos['assists']
        if datos['deaths'] == True: 
            final[personaje]['deaths'] += datos['deaths']
    return final