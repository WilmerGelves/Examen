import interfaces.menuPrincipal as menu
import corefiles.cargos as cargos
import globales.globales as globals
if __name__ == "__main__":
    cargos.CARGOS = 'data/cargos.json'
    cargos.checkFile(globals.cargos)
    menu.menuP(0)
