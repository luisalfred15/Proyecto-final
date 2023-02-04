from Client_ import Client

class GeneralClient(Client):
    def __init__(self, name, id, age, selected_game, seats, invoice):
        super().__init__(name, id, age, selected_game, seats)
        self.type_ticket = 'General'
        self.seats = seats
        self.invoice = invoice
    
    
