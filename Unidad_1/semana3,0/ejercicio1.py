#Pide un numero del 1 al 7 y muestra el nombre del dia 

print("1.Lunes,2.Martes,3.Miercoles,4.Jueves,5.Viernes,6.Sabado,7.Domingo")
opcion =int(input("Selecciona un numero para determinar que dias es: "))

match opcion:
    case 1: 
        print("Hoy es Lunes")
    case 2: 
        print("Hoy es Martes")
    case 3:
        print("Hoy es Miercoles") 
    case 4:
        print("Hoy es Jueves")
    case 5:
        print("Hoy es Viernes")
    case 6:
        print("Hoy es Sabado")
    case 7:
        print("Hoy es domingo") 
    case _: 
        print("Dia no encontrado")