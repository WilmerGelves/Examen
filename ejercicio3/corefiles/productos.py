import json 
import os

PRODUCTOS = 'data/productos.json'  #ruta de la carpeta que almacena los datos.

def NewFile(*param):
    with open(PRODUCTOS,"w") as wf: #bufer de escritura
        json.dump(param[0],wf,indent=4)

def UpdateFile(*param):
    with open(PRODUCTOS,"w") as fw:
        json.dump(param[0],fw,indent=4)


def AddData(*param):
    producto = list(param)
    with open(PRODUCTOS,"r+") as rwf: #buefer de escritura y lectura. 
        data_file=json.load(rwf)
        if (len(param) > 1):
            data_file[producto[0]].update({producto[1]:producto[2]})
        else:
            data_file.update({param[0]})
        # data_file[llavePrincipal].update({codigo:info})
        rwf.seek(0)
        json.dump(data_file,rwf,indent=4)


def ReadFile(): #Si el archivo exites, carga el contenido dentro de ellos.
    with open(PRODUCTOS,"r") as rf:
        return json.load(rf)
    


#Verificando si el archivo existe en nuestra carpeta data. 
def checkFile(*param):
    data = list(param)
    if(os.path.isfile(PRODUCTOS)):
        if(len(param)):
            data[0].update(ReadFile())
    else:
        if(len(param)):
            NewFile(data[0])