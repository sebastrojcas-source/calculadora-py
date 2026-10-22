print ('Hola')
lista_tareas = []
print ('ingresa tu tarea')
lista_tareas.append(input()) 
print ('necesitas agregar otra tarea?')
otra = input()
while otra == 'si':
  print('ingresa tu tarea')
  lista_tareas.append(input())
  print('necesitas agregar otra tarea? (si/no)')
  otra = input()

print('quieres ver tus tareas? (si/no)')
ver_tareas = input()

if ver_tareas == 'si':
  print(lista_tareas)
elif ver_tareas == 'no':
  print('gracias por usar el programa')
  print ('adios')