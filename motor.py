while gameplay_exit == 0:
    days_played += 1
    recuento_recursos(energy,  cooling_system, server_capacity, user_amount, days_played)
    gameplay_exit = win_con(days_played, gameplay_exit)
    if gameplay_exit > 0:
        break
    salto = input("Next day... (Press ENTER)")
    
