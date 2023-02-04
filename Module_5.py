from functions import *

def average_expense_vip(clients):
    expense_client = 0
    number_clients = 0
    for client in clients:
        if client.type_ticket == 'VIP':
            expense_client += client.invoice_game.total + client.invoice_rest.total
            number_clients += 1

def total_recieved_points(games):
    recieved_saman = calculate_recieved_points(games, 'Saman F.C.')
    recieved_alcan = calculate_recieved_points(games, 'Las Alcantarillas C.F.')
    recieved_paranin = calculate_recieved_points(games, 'Paraninfo Club.')
    return recieved_alcan, recieved_paranin, recieved_saman

def calculate_recieved_points(games, team_name):
    points_recieved = 0
    for game in games:
        if game.team1.name == team_name:
            points_recieved += game.points2
    return points_recieved

def total_points_made(games):
    dict_made = {}
    made_saman, dict_made = calculate_points_made(games, 'Saman F.C.', dict_made)
    made_alcan, dict_made = calculate_points_made(games, 'Las Alcantarillas C.F.', dict_made)
    made_paranin, dict_made = calculate_points_made(games, 'Paraninfo Club.', dict_made)
    return made_alcan, made_paranin, made_saman, dict_made

def calculate_points_made(games, team_name, dict_made):
    points_made = 0
    for game in games:
        if game.team1.name == team_name:
            points_made += game.points1
    dict_made[team_name] = points_made
    return points_made, dict_made

def total_games_played(games):
    played_saman = calculate_games_played(games, 'Saman F.C.')
    played_alcan = calculate_games_played(games, 'Las Alcantarillas C.F.')
    played_paranin = calculate_games_played(games, 'Paraninfo Club.')
    return played_paranin, played_alcan, played_saman

def calculate_games_played(games, team_name):
    games_played = 0
    for game in games:
        if game.team1.name == team_name or game.team2.name == team_name:
            games_played += 1
    return games_played