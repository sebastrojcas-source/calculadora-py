#listas (son modificables)
lista = ['sebastian rojas','soy chino',True,1.60]
print(lista[3])

#tupla (son una variable inmodificable)
tupla = ['sebastian rojas','soy chino',True,1.60]
tupla = ([3])
#esto es vaido
lista[3] = 'maquinola'

#esto no 
#tupla[3] = 'maquinola'

#creando un conjunto set (no se accede a los elementos por su indice,no almacena datos duplicados)
conjunto = {'sebastian rojas','soy chino',True,1.60}

#conjunto 3 (no se  puede acceder al elemento)
print(conjunto)

#creando un diccionario (dict) (la estructura es key : value y separamos con comas)
diccionario = {
    'nombre' : 'sebastian rojas castro',
    'canal' : 'chino gpt',
    'esta_emocionado' : True,
    'altura' : '1.60',
    'dato_duplicado' : 'chino gpt'
}
print(diccionario['esta_emocionado'])