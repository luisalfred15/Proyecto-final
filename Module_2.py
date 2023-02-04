from functions import *
from Game_ import *
from GeneralClient_ import *
from VIPClient_ import *
from Invoice_ import *
import random

# Genera los datos de los arbitros

def get_referees(db):
    referees = []
    for referee in db['referees']:
        referees.append(referee)
    return referees

def create_game(teams, stadiums, referees, games):
    team1, team2 = select_teams(teams)
    stadium = select_stadium(stadiums)
    referee = select_referee(referees)
    new_game = Game(team1, team2, 0, 0, stadium.general_seats, stadium.vip_seats, stadium, referee)
    games.append(new_game)
    return games

# Seleccion de todo lo necesario para crear un partido

def select_teams(teams):
    print('*** EQUIPOS ***')
    for team in teams:
        print(f'{teams.index(team) + 1}. {team.name}')
    selection_team1 = comprobar_opcion('Seleccione el primer equipo para el partido: ', len(teams))
    team1 = teams[selection_team1 - 1]
    selection_team2 = comprobar_opcion('Seleccione el segundo equipo para el partido: ', len(teams))
    while selection_team1 == selection_team2:
        selection_team2 = comprobar_opcion('Erros, no se puede seleccionar el mismo equipo. Por favor, seleccione un equipo: ', len(teams))
    team2 = teams[selection_team2 - 1]
    return team1, team2

def select_stadium(stadiums):
    print('*** ESTADIOS ***')
    for stadium in stadiums:
        print(f'{stadiums.index(stadium) + 1}. {stadium.name}')
    selection_stadium = comprobar_opcion('Seleccione el estadio donde desea que se de el juego: ', len(stadiums))
    stadium_selected = stadiums[selection_stadium - 1]
    return stadium_selected

def select_referee(referees):
    selection_referee = random.randint(0, len(referees) - 1)
    referee_selected = referees[selection_referee]
    print(f'El arbitro del partido sera {referee_selected}')
    return referee_selected

# Cambiar el estatus del partido 
                        
def change_status_game(games):
    counter = 0
    for game in games:
        if game.status == False:    
            print(f'                                    ID: {games.index(game) + 1}')
            game.print_game()
        else:
            counter += 1
    if counter != len(games):
        game_selected = comprobar_opcion('Seleccione el partido al que desea habilitar la venta de entradas: ', len(games))
        games[game_selected - 1].status = True
    else:
        print('No se puede cambiar el estatus de algun juego ya que no hay ninguno creado o todos estan cerrados')

# Verificador de los juegos abiertos

def verify_games_opened(games):
    games_not_opened = 0
    everything_closed = False
    for game in games:
        if game.status == False:
            games_not_opened += 1
    if games_not_opened == len(games):
        everything_closed = True
    return everything_closed

def close_game(games):
    for game in games:
        if game.status == True:    
            print(f'                    ID: {games.index(game) + 1}')
            game.print_game()
    id_game_selected = comprobar_opcion('Seleccione el partido al que desea cerrar la venta de entradas: ', len(games))
    game_selected = games[id_game_selected - 1]
    game_selected.status = False

# Crea el resultado del partido

def generate_result(games):
    points1 = 0
    points2 = 0
    counter = 0
    for game in games:
        if game.status == False and game.result == '':
            print(f'            ID: {games.index(game) + 1}')    
            game.print_game()
    id_game_selected = comprobar_opcion('Seleccione el partido que desea ver resultados: ', len(games))
    game_selected = games[id_game_selected - 1]
    while counter < 30:
        ref_num = str(random.randint(0, 10000))                              # Se emplea la libreria random para calcular los puntos de los equipos y jugadores
        if ref_num[-1] == '1':
            points1 += 1
            ref_num2 = random.randint(0, len(game_selected.team1.lineup) - 1)
            game_selected.team1.lineup[ref_num2].points += 1
        elif ref_num[-1] == '2':
            points2 += 1
            ref_num2 = random.randint(0, len(game_selected.team2.lineup) - 1)
            game_selected.team2.lineup[ref_num2].points += 1
        game_selected.points1 = points1
        game_selected.points2 = points2
        counter += 1
    
    x = f'********************* \n Puntos de {game_selected.team1.name}:' # Se emplean las variables auxiliares 'x' y 'y' para una impresion mas ordenada
    for player in game_selected.team1.lineup:
        if player.points > 0:
            x += f'\n {player.name}: {player.points}'
    
    y = f'********************* \n Puntos de {game_selected.team2.name}:'
    for player in game_selected.team2.lineup:
        if player.points > 0:
            y += f'\n {player.name}: {player.points}'
    
    result = f'''       {game_selected.team1.name}: {points1} | {game_selected.team2.name}: {points2}
            {x}
            {y}'''

    game_selected.result = result
    game_selected.print_final_game()
    
# Registro de cliente y factura

def register_client_and_invoice(games, clients, invoices):
    dict_seats = {}                                                                # Se hace uso de un diccionario para poder deseleccionar el asiento deseado
    client_seats = []
    name = comprobar_str('Introduzca el nombre del cliente: ')
    id = comprobar_num('Introduzca la cedula del cliente: ')
    age = comprobar_num('Introduzca la edad del cliente: ')
    for game in games:
        if game.status == True:
            print(f'                        ID: {games.index(game) + 1}')
            game.print_game()
    id_selected_game = comprobar_opcion('Introduzca el ID del juego que desea ver: ', len(games))
    selected_game = games[id_selected_game - 1]
    selection_ticket = comprobar_opcion('''Seleccione que tipo de entrada desea comprar:
    1. General
    2. VIP
    -> ''', 2)
    if selection_ticket == 1:
        selection_ticket = 'General'
        quantity_seats = comprobar_num('Ingrese la cantidad de asientos que desea comprar: ')
        selected_seats = selected_game.select_general_seats(quantity_seats, dict_seats, client_seats)
        if len(selected_seats) > 0:
            cost, discount, tax, total = calculate_invoice(selected_seats, id, selection_ticket)
            print(f'Total: {total}')
            proceed = comprobar_opcion('''Desea proceder a la compra?
            1. Si
            2. No
            -> ''', 2)
            if proceed == 1:
                new_invoice = generate_invoice(selected_seats, selection_ticket, cost, discount, tax, total)
                new_client = GeneralClient(name, id, age, selected_game, selected_seats, new_invoice)
                new_invoice.print_invoice()
                clients.append(new_client)
                invoices.append(new_invoice)
                print('Pago realizado con exito')
                return clients, invoices
            else:
                return clients, invoices
        else:
            return clients, invoices
    else:
        selection_ticket = 'VIP'
        quantity_seats = comprobar_num('Ingrese la cantidad de asientos que desea comprar: ')
        selected_seats = selected_game.select_vip_seats(quantity_seats, dict_seats, client_seats)
        if len(selected_seats) > 0:
            cost, discount, tax, total = calculate_invoice(selected_seats, id, selection_ticket)
            print(f'Total: {total}')
            proceed = comprobar_opcion('''Desea proceder a la compra?
            1. Si
            2. No
            -> ''', 2)
            if proceed == 1:
                new_invoice = generate_invoice(selected_seats, selection_ticket, cost, discount, tax, total)
                new_client = VIPClient(name, id, age, selected_game, selected_seats, new_invoice, '')
                new_invoice.print_invoice()
                clients.append(new_client)
                invoices.append(new_invoice)
                print('Pago realizado con exito')
                return clients, invoices
            else:
                return clients, invoices
        else:
            clients, invoices

def generate_invoice(selected_seats, selection_ticket, cost, discount, tax, total):
    new_invoice = Invoice(selected_seats, selection_ticket, cost, discount, tax, total)
    return new_invoice

# Calculo de la factura

def calculate_invoice(selected_seats, id, selection_ticket):
    cost = calculate_cost(selected_seats, selection_ticket)
    discount = calculate_discount(id)
    tax = calculate_tax(cost, discount)
    total = calculate_total(cost, tax)
    return cost, discount, tax, total

def calculate_cost(seats, selection_ticket):
    cost = 0
    if selection_ticket == 'General':
        cost = 15 * len(seats)
    else:
        cost = 45 * len(seats)
    return cost

def calculate_discount(id):
    discount = 0
    vampire_id = False
    if vampire_id:
        discount = 0.5
    return discount

def calculate_tax(cost, discount):
    cost_with_discount = cost - discount
    return cost_with_discount * 0.16

def calculate_total(cost_with_discount, tax):
    return cost_with_discount + tax

# Reinicio de datos de Modulo 2

def restart_data_2(db):
    load_data('Referees_DB.txt', [])
    load_data('Clients.txt', [])
    load_data('Games.txt', [])
    load_data('Invoices.txt', [])
    
    referees = get_referees(db)
    load_data('Referees_DB.txt', referees)