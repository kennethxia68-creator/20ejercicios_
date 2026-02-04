 #SOLICITAR AL USUARIO CUANDO DESEA INICIAR SU SALDO 
 #TOME EN CUENTA QUE DEBE ASIGNAR UN PRODUCTO CON VALOR DE 100
 #CALCULE SI AL USUARIO LE ALCANZA PARA COMPRAR EL PRODUCTO Y
 #MOSTRAR UN MENSAJE: COMPRA EXITOSA SU VUELTO ES: (MOSTRAR SU VUELTO)

# Solicitar al usuario con cuánto desea iniciar su saldo
saldo = int(input("Ingrese el monto con el que desea iniciar su saldo: "))

# Asignar el valor del producto
precio_producto = 100

# Verificar si el usuario puede comprar el producto
if saldo >= precio_producto:
    vuelto = saldo - precio_producto
    print("Compra exitosa.")
    print("Su vuelto es:", vuelto)
else:
    print("Saldo insuficiente para comprar el producto.")
