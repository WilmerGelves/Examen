import os
import interfaces.registroCargos as cargos 
def menuP(op):
    os.system('clear')
    title = """
    *******************
    * MENU PRINCIPAL  *
    *******************
    """
    menu = '1.Registrar cargos\n2.Ingresar empleado\n3. Generar desprendible de pago\n4.Salir'
    if (op != 4):
        print(title)
        print(menu)
        value = int(input('=>'))
        while(value <1 and value > 4):
            os.system('clear')
            print('Opción inválida')
            value = int(input('=>'))
        match (op):
            case 1:
                cargos.registroCargo()
            case 2:
                pass
            case 3:
                pass
            case 4:
                print('Hasta pronto..')
                os.system('pause')
                exit()
            case _: 
                print('Opción inválida...Intenta nuevamente')
                os.system('pause')
                menuP(0)



            
            
