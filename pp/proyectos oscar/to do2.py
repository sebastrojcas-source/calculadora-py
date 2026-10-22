print('Hola')
print('se muestran sus opciones')
lista_tareas = []
while True:
    print('1. agregar tarea')
    print('2. ver tareas')
    print('3. eliminar tareas')
    print('4. completar tareas')
    print('5. ver tareas pendientes') 
    print('6. ver tareas completadas')
    print('7. salir')
    print ('ingresa el numero de la opcion que deseas realizar')
    opcion = input()
    if opcion == '1':
      print('ingresa tu tarea')
      lista_tareas.append(input())
    elif opcion == '2':
      print(lista_tareas)
    elif opcion == '3':
      print('ingresa la tarea que deseas eliminar')
      tarea_eliminar = input()
      if tarea_eliminar in lista_tareas:
        lista_tareas.remove(tarea_eliminar)
        print('tarea eliminada')
      else:
        print('tarea no encontrada')    
    elif opcion == '4':
      print('ingresa la tarea que deseas completar')
      tarea_completar = input()
      if tarea_completar in lista_tareas:
        lista_tareas.remove(tarea_completar)
        print('tarea completada')
      else:
        print('tarea no encontrada')
    elif opcion == '5':
      print('tareas pendientes:')
      for tarea in lista_tareas:
        print(f"- {tarea}")
    elif opcion == '6':
       print('tareas completadas:')
       if not lista_tareas:
         print('No hay tareas completadas aún.')
      
    elif opcion == '7':
      print('gracias por usar el programa')
      break