 #inicio (bienvenida)   
print('-----------------------------')
print('Hola bienvenido a calculadora')
print('-----------------------------')

# datos del usuario requeridos 
print('digita tu primer numero')
numero1 = float(input())
print('digita tu segundo numero')
numero2 = float(input())
input() 
#resultado
print ('elige tu ecuacion: + - * / %')
operacion = input()
if operacion == '+':
 print('el resultado de la suma es') 
 print (numero1 + numero2) 
elif operacion == '-':
 print('el resultado de la resta es')
 print (numero1 - numero2)
elif operacion == "*":
 print ('el resultado de la multiplicacion es')
 print (numero1 * numero2)
elif operacion == '/':
    if numero2 == 0:
        print('no se puede dividir por cero')
    else:
        
      print ('el resultado de la division es')
      print (numero1 / numero2)
elif operacion == '%':
    print ('el resultado del porcentaje es')
    print (numero1 % numero2)
else:
     print('opeacion no valida') 
     print(input) 