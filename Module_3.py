from functions import *
from Drink_ import Drink
from Food_ import Food

# Crea los objetos de cada jugador y los añade a una lista de todos los jugadores de cada equipo

def create_objects_products(db):
    products = []
    for product in db['restaurant']:
        price = round(product.get('price') + product.get('price') * 0.16, 1)
        if product.get('type') == 'c':
            new_product = Food(product.get('name'), product.get('quantity'), price, product.get('packing'))
        else:
            new_product = Drink(product.get('name'), product.get('quantity'), price, product.get('alcoholic'))
        products.append(new_product)
    return products

def show_products(products):
    option_products = comprobar_opcion('''Seleccione como desea buscar los productos del restaurante:
            1. Por nombre del producto
            2. Por tipo de producto
            3. Por rango de precio
            -> ''', 3)
    search(products, option_products)
    
def search(products, option_products):
    if option_products == 1:
        print_by_name(products)
    elif option_products == 2:
        print_by_type(products)
    else:
        print_by_range(products)

# Filtro por nombre del producto

def print_by_name(products):
    product_found = False
    name = comprobar_str('Ingrese el producto que desea buscar: ')
    while True:    
        for product in products:
            if product.name == name:
                product_found = True
                product_to_print = product
        if product_found:
            product_to_print.print_product()
            break
        else:
            name = comprobar_str('Error, no se encontro el producto. Ingrese el producto que desea buscar: ')

# Filtro por tipo de producto

def print_by_type(products):
    type_product = comprobar_str('''Ingrese el tipo de producto que desea buscar: 
    b. Bebida
    c. Comida
    -> ''')
    type_product = type_product.lower()
    counter = 0
    while True:
        for product in products:
            if product.type_product == type_product:
                product.print_product()
                counter += 1
        if counter == 0:
            type_product = comprobar_str('Error, no se encontro el tipo de producto. Ingrese el tipo de producto que desea buscar: ')
        else:
            break

# Filtro por rango de precio

def print_by_range(products):
    low_bound = comprobar_num('Ingrese la cota inferior del rango: ')
    up_bound = comprobar_num('Ingrese la cota superior del rango: ')
    counter = 0
    while True:
        for product in products:
            if low_bound <= product.price <= up_bound:
                product.print_product()
                counter += 1
        if counter == 0:
            print('No se encontro ninguna comida dentro del rango de precio introducido')
            low_bound = comprobar_num('Ingrese la cota inferior del rango: ')
            up_bound = comprobar_num('Ingrese la cota superior del rango: ')
        else:
            break

def restart_data_3(db):
    load_data('Products_DB.txt', [])
    load_data('Invoices.txt', [])
    
    products = create_objects_products(db)
    load_data('Products_DB.txt', products)