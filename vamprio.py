def es_vampiro(numero):
    esVampiro = False
    son_colmillos = False
    long_par = False

    long_vamp = len(numero)

    if long_vamp % 2 == 0:
        long_par = True
        son_colmillos = hallar_colmillos(numero)
    
    if son_colmillos and long_par:
        esVampiro = True
    
    return esVampiro
    
def hallar_colmillos(numero):
    son_colmillos = False
    
    lista_aux = list(itertools.permutations(list(numero)))
    perms_numero = [''.join(permutacion) for permutacion in lista_aux]

    for perm in perms_numero:
        mitad1 = perm[:int(len(numero)/2)]
        mitad2 = perm[int(-len(numero)/2):]
        
        lista_aux1 = list(itertools.permutations(list(mitad1)))
        perms_mitad1 = [''.join(permutacion) for permutacion in lista_aux1]
        lista_aux2 = list(itertools.permutations(list(mitad2)))
        perms_mitad2 = [''.join(permutacion) for permutacion in lista_aux2]

        for perm1 in perms_mitad1:
            for perm2 in perms_mitad2:
                if (perm1[-1] == '0' or perm2[-1] != '0') or (perm2[-1] == '0' or perm1[-1] != '0'):
                    colmillo1 = int(perm1)
                    colmillo2 = int(perm2)
                    if colmillo1 * colmillo2 == int(numero):
                        son_colmillos = True
                        return son_colmillos

def hallar_permutaciones(numero):
    for 

def main():
    while True:
        numero = input('Ingrese un numero: ')
        esVampiro = es_vampiro(numero)

        if esVampiro:
            print('El numero es vampiro')
        else:
            print('El numero NO es vampiro')

    # lista_vampiro = []
    # for i in range(1, 150001):
    #     esVampiro = es_vampiro(str(i))
    #     if esVampiro:
    #         lista_vampiro.append(i)
    # print(lista_vampiro)

main()

