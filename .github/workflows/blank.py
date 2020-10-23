import numpy as np
import matplotlib.pyplot as plt
import os

if os.path.isdir('archivoEntrada/'): #If para definir si existe o no la carpeta archivoEntrada.
    
    data=np.loadtxt('archivoEntrada/T5_datos(1).csv',delimiter=',',skiprows=1) #Se importan los datos. 
 
    x=data[:,0] #Se crea un arreglo con los valores de tiempo.
    y=data[:,1] #Se crea un arreglo con los valores de resistencia.

    plt.title("Resistencia VS Tiempo.") #Se da titulo del gráfico.
    plt.plot(x,y,color='green')         #Se le da color a la gráfica.
    plt.xlabel("Tiempo [días].")        #Se da titulo al eje x.
    plt.ylabel("Resistencia [MPa].")    #Se da titulo al eje y.

    if os.path.isdir('archivoSalida/'):                                         #If para definir si existe o no la carpeta archivoSalida.
        plt.savefig('archivoSalida/Entrega1.png', dpi=300, bbox_inches='tight') #Se exporta la imagen en formato png.;
        print('La grafica fue guardada con exito.');                            #Se le informa al usuario del procedimiento llevado a cabo.
    
    else:
        print('La carpeta archivoSalida no existe.');                                      #En caso tal se indica que no existe la carpeta.
        os.mkdir('archivoSalida')                                                          #Se crea la carpeta archivoSalida.
        plt.savefig('archivoSalida/Entrega1.png', dpi=300, bbox_inches='tight')            #Se exporta la imagen en formato png.
        print('La carpeta archivoSalida fue creada y la gráfica fue guardada con exito.'); #Se le informa al usuario del procedimiento seguido.
    
    #En ambos casos se imprime la gráfica al final.

else:
    print('La carpeta archivoEntrada no existe.');  #En caso tal se indica que no existe la carpeta.
