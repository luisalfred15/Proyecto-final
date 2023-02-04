from Product_ import Product

class Food(Product):
    def __init__(self, name, quantity, price, is_packaged):
        super().__init__(name, quantity, price)
        self.is_packaged = is_packaged
        self.type_product = 'c'

    def print_product(self):
        self.print_name()
        self.print_quantity()
        self.print_price()
        if self.type_product == 'c':
            self.print_is_packaged()
        else:
            self.print_is_alcoholic()
    
    def print_name(self):
        print(f'        ******* Nombre: {self.name} *******')
    
    def print_quantity(self):
        print(f'        Cantidad: {self.quantity}')
    
    def print_price(self):
        print(f'        Precio: {self.price}')
    
    def print_is_packaged(self):
        if self.is_packaged == True:
            x = 'Si'
        else:
            x = 'No'
        print(f'        Empaque: {x}')
