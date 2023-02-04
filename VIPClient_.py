from Client_ import *

class VIPClient(Client):
    def __init__(self, name, id, age, selected_game, seats, invoice_game, invoice_rest):
        super().__init__(name, id, age, selected_game, seats)
        self.type_ticket = 'VIP'
        self.seats = seats
        self.invoice_game = invoice_game
        self.invoice_rest = invoice_rest