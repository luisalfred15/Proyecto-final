from requests import get
from Module_1 import *
from Module_2 import *
from Module_3 import *
from Module_4 import *
from functions import *

def main():
    db = get_json()

    players = create_objects_players(db)
    load_data('Players_DB.txt', players)
    stadiums = create_objects_stadiums(db)
    load_data('Stadiums_DB.txt', stadiums)
    teams = create_objects_teams(db, players, stadiums)
    load_data('Teams_DB.txt', teams)
    referees = get_referees(db)
    load_data('Referees_DB.txt', referees)
    products = create_objects_products(db)
    load_data('Products_DB.txt', products)
    clients = create_txt('Clients.txt')
    games = create_txt('Games.txt')
    invoices = create_txt('Invoices.txt')
    invoices_rest = create_txt('InvoicesRestaurant.txt')
    
    print('         ******************************************************************')
    print('         *********** Bienvenido al sistema de la liga El Saman! ***********')
    print('         ******************************************************************')

    while True:
        option = comprobar_opcion('''Ingrese la operacion que desea realizar:
        1. Buscar equipos
        2. Crear partidos
        3. Abrir venta de entradas
        4. Vender entradas
        5. Cerrar venta de entradas y ver resultados de partidos
        6. Buscar comidas o bebidas
        7. Adquirir un producto del restaurante
        8. Reiniciar base de datos
        9. Salir del sistema
        -> ''', 9)

        # Modulo 1
        
        if option == 1:
            show_teams(teams)
            
        # Modulo 2
        
        elif option == 2:
            
            games = create_game(teams, stadiums, referees, games)
            
            load_data('Games.txt', games)

        elif option == 3:
            
            games = download_data('Games.txt', [])
            change_status_game(games)
            load_data('Games.txt', games)
        
        
        elif option == 4:
            clients = download_data('Clients.txt', [])
            invoices = download_data('Invoices.txt', [])
            games = download_data('Games.txt', [])

            everything_closed = verify_games_opened(games) # Aqui el verificador ayuda para conocer si hay partidos abiertos o si es necesario imprimir el mensaje
            
            if everything_closed == True:
                print('No se pueden vender entradas ya que no hay partidos disponibles')
            else:
                clients, invoices = register_client_and_invoice(games, clients, invoices)
            
            load_data('Invoices.txt', invoices)
            load_data('Clients.txt', clients)
        
        
        elif option == 5:
            
            games = download_data('Games.txt', [])

            if len(games) > 0:
                decision = comprobar_opcion('''Seleccione la opcion que desea realizar: 
                1. Cerrar un juego
                2. Ver resultados de un juego
                -> ''', 2)
                
                if decision == 1:    
                    close_game(games)
                else:
                    generate_result(games)
            else:
                print('No se puede cerrar ningun partido ya que no hay partidos en curso')
            
        # Modulo 3
        
        elif option == 6:
            
            products = download_data('Products_DB.txt', [])
            show_products(products)

        # Modulo 4
        
        elif option == 7:
            products = download_data('Products_DB.txt', [])
            clients = download_data('Clients.txt', [])
            invoices_rest = download_data('InvoicesRestaurant.txt', [])

            vip_client, invoices_rest = register_client_restaurant(clients, products, invoices_rest)
            if vip_client == -1:
                pass
            elif vip_client == -2:
                print('El cliente VIP no pudo ser encontrado')
            
            load_data('Clients.txt', vip_client)
            load_data('Products_DB.txt', products)
            load_data('InvoicesRestaurant.txt', invoices_rest)
        
        elif option == 8:

            db = get_json()
            restart_data_1(db)
            restart_data_2(db)
            restart_data_3(db)
            restart_data_4()
            
            print('Base de datos reiniciada con exito')

        else:
            break

main()