class InvoiceRestaurant:
    def __init__(self, id, selected_products, cost, discount, total):
        self.id = id
        self.selected_products = selected_products
        self.cost = cost
        self.discount = discount
        self.total = total
    
    def print_invoice_rest(self):
        print('*******************')
        self.print_cost()
        self.print_discount()
        self.print_total()
        print('*******************')

    
    def print_cost(self):
        print(f'        Subtotal: {self.cost}')

    def print_discount(self):
        print(f'        Descuento: {self.discount}')
    
    def print_total(self):
        print(f'        Total: {self.total}')
