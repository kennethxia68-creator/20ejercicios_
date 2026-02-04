#Pide el numero de un mes y di que estacion pertenece

print("1.Enero,2.Febrero,3.Marzo,4.Abril,5.Mayo,6.Junio,7.Julio,8.Agosto,9.Septiembre,10.Octubre,11.Noviembre,12.Diciembre")
opcion = int(input("Selecciona un numero para determinar que mes es y en que estacion del año se encuentra: "))

match opcion:
    case 1: 
        print("El mes es Enero y la estacion es: Invierno")
    case 2: 
        print("El mes es Febrero y la estacion es: Invierno")
    case 3:
        print("El mes es Marzo y la estacion es: Primavera") 
    case 4:
        print("El mes es Abril y la estacion es: Primevera")
    case 5:
        print("El mes es Mayo y la estacion es: Primavera")
    case 6:
        print("El mes es Junio y la estacion es: Verano")
    case 7:
        print("El mes es Julio y la estacion es: Verano") 
    case 8: 
        print("El mes es Agosto y la estacion es: Verano")
    case 9:
        print("El mes es Septiembre y la estacion es: Otoño")
    case 10:
        print("El mes es Octubre y la estacion es: Otoño")
    case 11:
        print("El mes es Noviembre y la estacion es: Otoño")
    case 12:
        print("El mes es Diciembre y la estacion es: invierno")