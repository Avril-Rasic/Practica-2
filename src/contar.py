def contar_rondas (rounds):
    final = {}
    num = 0
    for round  in rounds: 
        for personaje,datos in round.items():
        #Si no cree el dicc del personaje
            if personaje not in final:
                final[personaje] = {'kills': 0, 'assists': 0,'deaths': 0}

        #Aumento los datos 
            final[personaje]['kills'] += datos['kills']
            final[personaje]['assists'] += datos['assists']
            if datos['deaths'] == True: 
                final[personaje]['deaths'] += datos['deaths']
        num = num + 1

        print(f"Resultado ronda {num}")
        print(f"|{'Personaje':<9}|{'Kills':<5}|{'Assists':<7}|{'Deaths':<6}|")
        print(f"|{'-'*9}|{'-'*5}|{'-'*7}|{'-'*6}|")
        for personaje, datos in final.items():
            print(f'|{personaje:<9}|{datos['kills']:<5}|{datos['assists']:<7}|{datos['deaths']:<6}|')
        print("")
    return final