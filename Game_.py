from functions import *

class Game:
    def __init__(self, team1, team2, points1, points2, general_seats, vip_seats, stadium, referee):
        self.team1 = team1
        self.team2 = team2
        self.points1 = points1
        self.points2 = points2
        self.stadium = stadium
        self.general_seats = general_seats
        self.vip_seats = vip_seats
        self.referee = referee
        self.status = False
        self.result = ''
        self.audience = []
    
    def print_game(self):
        self.print_team_names()
        self.print_stadium()
        self.print_referee()
    
    def print_final_game(self):
        self.print_team_names()
        self.print_stadium()
        self.print_referee()
        self.print_result()
    
    def print_team_names(self):
        print(f'''      ******* {self.team1.name} vs. {self.team2.name} ********''')
    
    def print_stadium(self):
        print(f'                Estadio: {self.stadium.name}')
    
    def print_referee(self):
        print(f'                Arbitro: {self.referee}')
    
    def print_result(self):
        print(      self.result)
    
    def print_general_seats(self):
        print('     *** Generales ***')
        for i in self.general_seats:
            print(      i)
    
    def print_vip_seats(self):
        print('     *** VIP ***')
        for i in self.vip_seats:
            print(      i)
    
    def select_general_seats(self, seats_to_buy, dict_seats, client_seats):
        if seats_to_buy > 0:
            self.print_general_seats()
            selected_seat = input('Ingrese el asiento que desea comprar: ')
            for i in range(len(self.general_seats)):
                for j in range(len(self.general_seats[i])):
                    if self.general_seats[i][j] == selected_seat:
                        if self.general_seats[i][j] != 'X':
                            print(f'Asiento {selected_seat} seleccionado')
                            self.general_seats[i][j] = 'X'
                            dict_seats[selected_seat] = [i, j]
                            client_seats.append(selected_seat)
                            return self.select_general_seats(seats_to_buy - 1, dict_seats, client_seats)
                        else:
                            print('Por favor, seleccione un asiento que este disponible')
                            return self.select_general_seats(seats_to_buy, dict_seats, client_seats)
            print('El asiento que ha seleccionado no existe')
            return self.select_general_seats(seats_to_buy, dict_seats, client_seats)
        else:
            proceed = comprobar_opcion('''Desea cambiar algun puesto?
            1. Si
            2. No
            -> ''', 2)
            if proceed == 1:
                client_seats = self.deselect_general_seats(dict_seats, client_seats)
                return client_seats
            else:
                return client_seats
    
    def deselect_general_seats(self, dict_seats, client_seats):
        for seat in client_seats:
            print(f'{client_seats.index(seat) + 1}. {seat}')
        seat = comprobar_opcion('Seleccione el asiento que desea eliminar: ', len(client_seats))
        seat = client_seats[seat - 1]
        delete_seat = dict_seats.get(seat)
        self.stadium.general_seats[delete_seat[0]][delete_seat[1]] = seat
        dict_seats.pop(seat)
        client_seats.pop(client_seats.index(seat))
        return client_seats
    
    def select_vip_seats(self, seats_to_buy, dict_seats, client_seats):
        if seats_to_buy > 0:
            self.print_vip_seats()
            selected_seat = input('Ingrese el asiento que desea comprar: ')
            for i in range(len(self.stadium.vip_seats)):
                for j in range(len(self.vip_seats[i])):
                    if self.vip_seats[i][j] == selected_seat:
                        if self.vip_seats[i][j] != 'X':
                            print(f'Asiento {selected_seat} seleccionado')
                            self.vip_seats[i][j] = 'X'
                            dict_seats[selected_seat] = [i, j]
                            client_seats.append(selected_seat)
                            return self.select_vip_seats(seats_to_buy - 1, dict_seats, client_seats)
                        else:
                            print('Por favor, seleccione un asiento que este disponible')
                            return self.select_vip_seats(seats_to_buy, dict_seats, client_seats)
            print('El asiento que ha seleccionado no existe')
            return self.select_vip_seats(seats_to_buy, dict_seats, client_seats)
        else:
            proceed = comprobar_opcion('''Desea cambiar algun puesto?
            1. Si
            2. No
            -> ''', 2)
            if proceed == 1:
                client_seats = self.deselect_vip_seats(dict_seats, client_seats)
                return client_seats
            else:
                return client_seats
    
    def deselect_vip_seats(self, dict_seats, client_seats):
        for seat in client_seats:
            print(f'{client_seats.index(seat) + 1}. {seat}')
        seat = comprobar_opcion('Seleccione el asiento que desea eliminar: ', len(client_seats))
        seat = client_seats[seat - 1]
        delete_seat = dict_seats.get(seat)
        self.stadium.general_seats[delete_seat[0]][delete_seat[1]] = seat
        dict_seats.pop(seat)
        client_seats.pop(client_seats.index(seat))
        return client_seats