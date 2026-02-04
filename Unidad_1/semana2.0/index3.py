#SOLICITAR AL USUARIO CON CUANDO DESEA INICIAR SU SALDO
#TOME EN CUENTA QUE DEBE ASIGNAR UN PRODUCTO CON VALOR DE 200 QUETZALES
#PREGUNTARLE AL USUARIO SI DESEA REALIZAR LA COMPRA CON UNA "si", Si
#ACEPTA REALIZAR LA COMPRA ENTONCES: 
#CALCULE SI AL USUARIO LE ALCANZA PARAR COMPRAR EL PRODUCTO Y SI LE ALCANZA
#MOSTRA UN MENSAJE: COMPRA EXITOSA, SU VUELTO ES: (MOSTRAR VUELTO)


# Solicitar al usuario con cuánto desea iniciar su saldo
saldo = int(input("Ingrese el monto con el que desea iniciar su saldo: "))

# Asignar el valor del producto
precio_producto = 200

# Verificar primero si le alcanza el dinero
if saldo >= precio_producto:
    respuesta = input("¿Desea realizar la compra? (si / no): ")

    if respuesta.lower() == "s":
        vuelto = saldo - precio_producto
        print("Compra exitosa, su vuelto es:", vuelto)
    else:
        print("Compra cancelada.")
else:
    print("No tienes saldo suficiente para comprar el producto.")


