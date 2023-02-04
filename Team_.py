class Team:
    def __init__(self, name, lineup, stadium):
        self.name = name
        self.lineup = lineup
        self.stadium = stadium
    
    def print_team(self):
        self.print_name()
        self.print_stadium()
        self.print_lineup()
    
    def print_name(self):
        print(f'''              ***** {self.name} *****''')
    
    def print_stadium(self):
        print(f'                Estadio: {self.stadium.name}')
    
    def print_lineup(self):
        for player in self.lineup:
            print('         ***********************')
            print(f'''           Nombre: {player.name}
            Posicion: {player.position}
            Numero: {player.number}''')
