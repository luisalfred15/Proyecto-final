class Invoice:
    def __init__(self, seats, type_ticket, cost, discount, tax, total):
        self.seats = seats
        self.type_ticket = type_ticket
        self.cost = cost
        self.discount = discount
        self.tax = tax
        self.total = total
    
    def print_invoice(self):
        print('         *******************')
        self.print_seats()
        self.print_cost()
        self.print_discount()
        self.print_tax()
        self.print_total()
        print('         *******************')

    
    def print_seats(self):
        x = ''                                      # Se emplea una variable auxiliar para mejor impresion
        for i in range(len(self.seats)):
            if i < len(self.seats) - 1:
                x += f'{self.seats[i]}' + ', '
            else:
                x += f'{self.seats[i]}'
        print(f'        Asiento(s): {x}')
    
    def print_cost(self):
        print(f'        Subtotal: {self.cost}')
    
    def print_discount(self):
        print(f'        Descuento: {self.discount}')
    
    def print_tax(self):
        print(f'        Impuesto: {self.tax}')
    
    def print_total(self):
        print(f'        Total: {self.total}')