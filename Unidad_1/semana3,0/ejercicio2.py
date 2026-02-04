#Pide un numero del 1 al 12 y muestra el nombre del mes 

print("1.Enero,2.Febrero,3.Marzo,4.Abril,5.Mayo,6.Junio,7.Julio,8.Agosto,9.Septiembre,10.Octubre,11.Noviembre,12.Diciembre")
opcion = int(input("Selecciona un numero para determinar que mes es: "))

match opcion:
    case 1: 
        print("Es Enero")
    case 2: 
        print("Es Febrero")
    case 3:
        print("Es Marzo") 
    case 4:
        print("Es Abril")
    case 5:
        print("Es Mayo")
    case 6:
        print("Es Junio")
    case 7:
        print("Es Julio") 
    case 8: 
        print("Es Agosto")
    case 9:
        print("Es Septiembre")
    case 10:
        print("Es Octubre")
    case 11:
        print("Es Noviembre")
    case 12:
        print("Es Diciembre")
    case _:
        print("Mes no encontrado")