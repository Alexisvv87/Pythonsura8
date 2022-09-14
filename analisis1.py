import pandas as pd     

#cargar los datos

dataFrame=pd.read_csv('./empleados.csv')
#print(dataFrame)

#Cargar todos los datos
#print(dataFrame.to_string)

#cargar los primeros N registros de un banco de datos

#print(dataFrame.head())

#cargar los ultimos N registros de un banco de datos

#print(dataFrame.tail())

#obtener informacion de los datos cargados
#print(dataFrame.info())
#print(dataFrame.describe())
#acceder a datos o registros especificos
#primeros 5 nombres 
#print(dataFrame["nombres"] .head())
#Ultimos 20 salarios
#print(dataFrame["salarios"] .tail(20))
#Aceder a Registros por su indice ahi esta por rango del 20 al 30 
#print(dataFrame.iloc[20:30])
#Aceder a Registros por su indice ahi esta por rango y que muestre por separado el 20, 30 y 40 
#print(dataFrame.loc[[20,30,40]])
#Aceder a Registros por su indice ahi esta por rango y que muestre por separado el 20, 30 y 40 
# pero solo que me traiga nombres y salarios  
#print(dataFrame.loc[[20,30,40],['nombres','salarios']])
#almacenar los datos en ves de imprimir en otra variable
'''
tabla=(dataFrame.loc[[20,30,40],['nombres','salarios']])
html=tabla.to_html()
tex_file=open('index.html','w')
tex_file.write(html)
tex_file.close()
'''

#filtros con condiciones logicas 

print(dataFrame[dataFrame["salario"]>5500000].head(10))
print(dataFrame[(dataFrame["salario"]>5500000) & (dataFrame["cargo"]=="analista2")])









