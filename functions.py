import pickle
import os
import requests

# Para obtener los datos del JSON

def get_json():
    r = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion-2122-3/saman_fifa_api/main/api.json')
    if r.status_code == 200:
        db = r.json()
    return db

# Para cargar los datos a archivos de texto

def load_data(txt_name, data):
    write = open(txt_name, 'wb')
    pickle.dump(data, write)
    write.close()

# Para leer los datos de los archivos de texto

def download_data(txt_name, data):

    read = open(txt_name, "rb")   
    if os.stat(txt_name).st_size != 0:
        data = pickle.load(read)    
    read.close()

    return data

def create_txt(txt):
    file = open(txt, 'rb')
    try:
        data = pickle.load(file)
    except EOFError:
        data = []
    file.close()
    return data

def restart_everything():
    games = []
    invoices = []
    load_data('Games.txt', games)
    load_data('Invoices.txt', invoices)

# Comprobaciones

def comprobar_str(msg):
    string = input(msg)
    if string.replace(' ', '').replace('.', '').isalpha():
        return string
    else:    
        return comprobar_str('Error, ingrese palabras validas: ')

def comprobar_opcion(msg, cantidad_opciones):
    opcion = input(msg)
    if opcion.isnumeric() and int(opcion) in range(1, cantidad_opciones + 1):
        return int(opcion)
    else:
        return comprobar_opcion('Error, seleccione una opcion que este dentro del rango: ', cantidad_opciones)

def comprobar_num(msg):
    num = input(msg)
    if num.isnumeric() and 0 < int(num):
        return int(num)
    else:
        return comprobar_num('Error, ingrese un numero valido: ')