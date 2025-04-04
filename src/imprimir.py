def imprimir_ronda(final,num):
    print(f"Ranking ronda {num}")
    #imprimo cabecera de la tabla
    print("-"*15)
    print(f"| {'Jugador'} | {'Kills'} | {'Assists'} | {'Deaths'} |")
    print("-"*15)
    #imprimo datos de cada personaje
    for personaje, elem in final.items(): 
        print(f"| {personaje} | {elem['kills']} | {elem['assists']} | {elem['deaths']} | ")
