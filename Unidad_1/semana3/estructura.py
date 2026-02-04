#sENTENCIA SWITCH 

print("1.Azul,2.Amarillo,3.Rojo")
opcion = int(input("ingrese un numero para determinar tu color: "))

match opcion:
    case 1: 
        print("Has eligido el azul")
    case 2: 
        print("Has eligido el amarillo")
    case 3:
        print("Has eligido el rojo") 
    case _:
        print("Opcion invalida") 
#Conforme a la estructura del switch case, realizar un menu de las
#4 operaciones basicas utilizando dos numeros (solicitar)

print("1.Suma,2.Resta,3.Multiplicacion,4.Division")
operaciones = int(input("ingrese el numero para elegir la operacion"))

match operaciones: 
    case 1: 
        print("Has seleccionado Suma")
    case 2: 
        print("Has seleccionado resta")