def contar_rondas (rounds):
    final = {}
    num = 0
    kills = 0
    for round  in rounds: 
        for personaje,datos in round.items():
        #Si no cree el dicc del personaje
            if personaje not in final:
                final[personaje] = {'kills': 0, 'assists': 0,'deaths': 0,'mvp':0,'puntaje':0}

        #Aumento los datos 
            final[personaje]['kills'] += datos['kills']
            final[personaje]['assists'] += datos['assists']
            if datos['deaths'] == True: 
                final[personaje]['deaths'] += datos['deaths']

        #puntaje
            contar = 0
            if (datos['kills']>0):
                contar += datos['kills']*3
            if(datos['assists']>0):
                contar += datos['assists']
            if(datos['deaths'] == True):
                contar -= 1
            final[personaje]['puntaje'] = contar

    #MVP de la ronda
        puntaje = 0
        for jugador, datos in final.items(): 
            if datos['puntaje']>puntaje: 
                puntaje = datos['puntaje']
                nombre = jugador
        final[nombre]['mvp'] += 1
        

        num = num + 1
        print(f"Resultado ronda {num}")
        print(f"|{'Personaje':<9}|{'Kills':<5}|{'Assists':<7}|{'Deaths':<6}|{'Mvp':<6}|{'Puntos':<6}|")
        print(f"|{'-'*9}|{'-'*5}|{'-'*7}|{'-'*6}|")
        for personaje, datos in final.items():
            print(f'|{personaje:<9}|{datos['kills']:<5}|{datos['assists']:<7}|{datos['deaths']:<6}|{datos['mvp']:<3}|{datos['puntaje']:<6}')
        print("")
    return final