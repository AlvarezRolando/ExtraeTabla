#Script que extrae cadenas de caracteres de archivos de texto y las 
#exporta en formato de tabla, el objetivo es facilitar la extracciíon de
#datos estadísticos de los archivos .inv 

#ESTE ES UN COMENTARIO
import pandas as pd

"""# TODO EL TEXTO SE GUARDA EN UN ÚNICO ARREGLO
archivo= open('TRE01.INV','r',encoding="utf-8")
contenido = archivo.read()
#print(contenido)
archivo.close()

#El archivo es de tipo 
#print(type(contenido))

linRes=contenido.find('INVERSION RESULTS')
print(linRes)
print(contenido[linRes:linRes+100])
"""

#Lectura de archivo línea por línea con for
archivo = open('TRE01.INV','r',encoding="utf-8")
numlin,inicRes,inicResumen,inicTabla,finRes,finResumen,finTabla=0,0,0,0,0,0,0
texto=[]

#Campo a buscar
t1='INITIAL RMS ERROR'
t2='Model inversion constraint'
t3='Error Distribution'
t4='Iteration  Time for this iteration  Total Time   Abs. Error'
t5='RES2DINV ver. 3.55.32 - ID. No. : K3-C8FAC8FA-C8FA'
t6='ITERATION 1'


for linea in archivo:
	linea=linea.strip('\n') 
	texo=texto.append(linea)

#Busqueda con condicional "if"	para hallar la información de interés
	if (linea == t1):
		lineat1=numlin

	if (linea == t2):
		lineat2=numlin+1
	#BUSCANDO ERROR MEDIO
	if (linea == t3):
		lineat3= numlin - 3 #SE EXTRAE EL RENGLÓN CON LA INFORMACIÓN DE ERROR MEDIO

	#if (linea == t4):
	#	lineat3=numlin+1

	#if (linea == t5):
	#	lineat4=numlin-1
	if (linea == t6):
		lineat6=numlin +3

	numlin=numlin+1
	
	

print('TERMINA LECTURA DEL ARCHIVO')

#Resultados encontrados
resultadosInv=texto[lineat1:lineat1+6] 
errorMedio=texto[lineat3]

numNiveles=texto[lineat6]
numNiveles=numNiveles.split(",") #Separa la cadena dado un delimitador. -> resulta en un arreglo de cadenas

print("RESULTAOS DE INVERSIÓN")
#print(resultadosInv)
#print(type(resultadosInv))

#SE CREA EL DATAFRAME QUE CONTIENE PARTE DE LA INFORMACIÓN DE "DATOS DE SALIDA INVERSIÓN" 
dInverResults=pd.DataFrame(resultadosInv) # Comvertimos la lista en un DataFrame

#dfResultados = pd.DataFrame(resultadosInv) # Comvertimos la lista en un DataFrame

#Resumen de parámetros de inversión
#resumen=texto[inicResumen:finResumen]

#Resumen de iteraciones
#tablaIteraciones=texto[inicTabla-1:finTabla]

print(dInverResults)
print (numNiveles)
print(type(numNiveles))
