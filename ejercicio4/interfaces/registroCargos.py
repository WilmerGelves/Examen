import corefiles.cargos as cargos
import globales as globals
def registroCargo():
    title = """
    ******************
    * GESTION CARGOS *
    ******************
    """
    print(title)
    cod = int('Ingrese código del cargo: ')
    nombre = input('Nombre del cargo: ')

    cargo = {
        'codigo': cod,
        'nombre': nombre
    }
    cargos.AddData('cargo',cod,cargo)
    globals.cargos.get('cargo').update({cod:cargo})
