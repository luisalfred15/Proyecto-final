from Product_ import Product

class Drink(Product):
    def __init__(self, name, quantity, price, is_alcoholic):
        super().__init__(name, quantity, price)
        self.is_alcoholic = is_alcoholic
        self.type_product = 'b'
    
    def print_product(self):
        self.print_name()
        self.print_quantity()
        self.print_price()
        if self.type_product == 'c':
            self.print_is_packaged()
        else:
            self.print_is_alcoholic()
    
    def print_name(self):
        print(f'        ********* Nombre: {self.name} *********')
    
    def print_quantity(self):
        print(f'        Cantidad: {self.quantity}')
    
    def print_price(self):
        print(f'        Precio: {self.price}')
    
    def print_is_alcoholic(self):
        if self.is_alcoholic == True:
            x = 'Si'
        else:
            x = 'No'
        print(f'        Alcoholica: {x}')