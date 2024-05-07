import json 
import os

CARGOS = 'data/cargos.json'  #ruta de la carpeta que almacena los datos.

def NewFile(*param):
    with open(CARGOS,"w") as wf: #bufer de escritura
        json.dump(param[0],wf,indent=4)

def UpdateFile(*param):
    with open(CARGOS,"w") as fw:
        json.dump(param[0],fw,indent=4)


def AddData(*param):
    cargo = list(param)
    with open(CARGOS,"r+") as rwf: #buefer de escritura y lectura. 
        data_file=json.load(rwf)
        if (len(param) > 1):
            data_file[cargo[0]].update({cargo[1]:cargo[2]})
        else:
            data_file.update({param[0]})
        # data_file[llavePrincipal].update({codigo:info})
        rwf.seek(0)
        json.dump(data_file,rwf,indent=4)


def ReadFile(): #Si el archivo exites, carga el contenido dentro de ellos.
    with open(CARGOS,"r") as rf:
        return json.load(rf)
    


#Verificando si el archivo existe en nuestra carpeta data. 
def checkFile(*param):
    data = list(param)
    if(os.path.isfile(CARGOS)):
        if(len(param)):
            data[0].update(ReadFile())
    else:
        if(len(param)):
            NewFile(data[0])