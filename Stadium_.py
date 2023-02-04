class Stadium:
    def __init__(self, name, general_seats, vip_seats):
        self.name = name
        self.general_seats = general_seats
        self.vip_seats = vip_seats
    
    def print_general_seats(self):
        print('             *** Generales ***')
        for i in self.general_seats:
            print(              i)
    
    def print_vip_seats(self):
        print('             *** VIP ***')
        for i in self.vip_seats:
            print(              i)