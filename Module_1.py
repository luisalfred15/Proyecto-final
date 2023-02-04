from functions import *
from Team_ import Team
from Player_ import Player
from Stadium_ import Stadium

# Crea los objetos de cada jugador y los añade a una lista de todos los jugadores de cada equipo

def create_objects_players(db):
    players = []
    for team in db['teams']:
        for key, value in team.items():
            if key == 'lineup':
                for player in value:
                    new_player = Player(player.get('name'), team.get('name'), player.get('number'), player.get('position'), 0)
                    players.append(new_player)
    return players

# Genera el mapa de asientos general

def generate_seatmap_general(db):
	m = db[0]
	n = db[1]
	abcdf = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	matriz = ['A'] * m
	for i in range (m):
		matriz[i] = [f'{abcdf[i]}'] * n
	for j in range(m):
		a = matriz[j]
		for i in range(n):
			a[i] = a[i]+str(i)
	return matriz

# Genera el mapa de asientos VIP

def generate_seatmap_vip(db):
	m = db[0]
	n = db[1]
	abcdf = ['AV', 'BV', 'CV', 'DV', 'EV', 'FV', 'GV', 'HV', 'IV', 'JV', 'KV', 'LV', 'MV', 'NV', 'OV', 'PV', 'QV', 'RV', 'SV', 'TV', 'UV', 'VV', 'WV', 'XV', 'YV', 'ZV']
	matrix = ['V'] * m
	for i in range (m):
		matrix[i] = [f'{abcdf[i]}'] * n
	for j in range(m):
		a = matrix[j]
		for i in range(n):
			a[i] = a[i]+str(i)
	return matrix

# Crea los objetos de cada estadio y los añade a una lista

def create_objects_stadiums(db):
    stadiums = []
    for team in db['teams']:
        for key, value in team.items():
            if key == 'stadium':
                new_stadium = Stadium(value.get('name'), generate_seatmap_general(value['map']['general']), generate_seatmap_vip(value['map']['vip']))
                stadiums.append(new_stadium)
    return stadiums

# Crea los objetos de cada equipo

def create_objects_teams(db, players, stadiums):
    teams = []
    for team in db['teams']:
        players_selected = []
        for player in players:                          # En este ciclo, se crea la lista de jugadores que se asociara con el objeto del equipo, ya que
            if team.get('name') == player.team:         # la otra lista contiene a todos los jugadores de la base de datos
                players_selected.append(player)
        for stadium in stadiums:                        # En este ciclo, se asigna el estadio del equipo
            if team['stadium']['name'] == stadium.name:
                stadium_selected = stadium
        new_team = Team(team.get('name'), players_selected, stadium_selected)
        teams.append(new_team)
    return teams

def show_teams(list_teams):
    option_teams = comprobar_opcion('''Seleccione como desea buscar a los equipos:
            1. Por nombre de equipo
            2. Por nombre de jugador
            3. Por nombre de estadio
            -> ''', 3)
    search(list_teams, option_teams)
    
def search(list_teams, option_teams):
    if option_teams == 1:
        print_by_team(list_teams)
    elif option_teams == 2:
        print_by_player(list_teams)
    else:
        print_by_stadium(list_teams)

# Filtro de nombre con ciclo

def print_by_team(list_teams):
    team_found = False
    name = comprobar_str('Ingrese el equipo que desea buscar: ')
    while True:    
        for team in list_teams:
            if team.name == name:
                team_found = True
                team_to_print = team
        if team_found:
            team_to_print.print_team()
            break
        else:
            name = comprobar_str('Error, no se encontro el equipo. Ingrese el equipo que desea buscar: ')

# Filtro de nombre de jugador con ciclo

def print_by_player(list_teams):
    player_found = False
    name = comprobar_str('Ingrese el nombre del jugador que desea buscar: ')
    while True:
        for team in list_teams:
            for player in team.lineup:
                if player.name == name:
                    player_found = True
                    team_to_print = team
        if player_found:
            team_to_print.print_team()
            break
        else:
            name = comprobar_str('Error, no se encontro el jugador. Ingrese el jugador que desea buscar: ')

# Filtro de nombre de estadio con ciclo

def print_by_stadium(list_teams):
    stadium_found = False
    name = comprobar_str('Ingrese el estadio que desea buscar: ')
    while True:
        for team in list_teams:
            if team.stadium.name == name:
                stadium_found = True
                team_to_print = team
        if stadium_found:
            team_to_print.print_team()
            break
        else:
            name = comprobar_str('Error, no se encontro el estadio. Ingrese el estadio que desea buscar: ')

# Reinicia los datos de este modulo

def restart_data_1(db):

    load_data('Players_DB.txt', [])
    load_data('Stadiums_DB.txt', [])
    load_data('Teams_DB.txt', [])
    
    players = create_objects_players(db)
    load_data('Players_DB.txt', players)
    stadiums = create_objects_stadiums(db)
    load_data('Stadiums_DB.txt', stadiums)
    teams = create_objects_teams(db, players, stadiums)
    load_data('Teams_DB.txt', teams)