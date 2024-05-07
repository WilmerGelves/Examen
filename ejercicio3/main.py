import os
import corefiles.productos as product
import globales.llave as llave
def abastos():
    os.system('clear')
    title = """
    *********************
    * TIENDA DE VÍVERES *
    *********************
    """
    print(title)
    menu = '1.Ingresar producto\n2.Salir'
    print(menu)
    try: 
        op = int(input('=>'))
        while (op != 1 and op != 2):
            print ('Opción inválida.')
            os.system('pause')
            op = int(input('=>'))
        match op:
            case 1: 
                os.system('clear')
                title ="""
                ************************
                * INGRESO DE PRODUCTOS *
                ************************
                """
                print(title)
                print('Ingrese los datos del producto: ')
                codigo = int(input('Ingrese el código: '))
                nombreP = input('Nombre del producto: ')
                valor = float(input('Valor del producto: '))
                minimo = int(input('Stock mínimo del producto: '))
                maximo = int(input('Stock maxima del producto: '))
                
                elemento = {
                    'codigo': codigo,
                    'nombreP': nombreP,
                    'valor': valor,
                    'minimo': minimo,
                    'maximo': maximo
                }
                product.AddData('producto',codigo,elemento)
                llave.productos.get('producto').update({codigo:elemento})
                print ('1.Para agregar un nuevo producto\n2.Salir ')
                seleccion = int(input('=>'))
                while (seleccion != 1 and seleccion != 2):
                    print ('Opción inválida.')
                    os.system('pause')
                    seleccion = int(input('=>'))
                if seleccion ==1 : 
                    abastos()
                else :
                    exit()
    except ValueError: 
        print('Está ingresando valores incorrectos... Intente nuevamente')
        os.system('pause')
        abastos()

if __name__ == '__main__':
    os.system('clear')
    product.PRODUCTOS = ('data/datos.json')
    product.checkFile(llave.productos)
    abastos()


