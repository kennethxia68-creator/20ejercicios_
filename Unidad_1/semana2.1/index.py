# Calculadora de Descuento
#Pide el precio de un producto. Si el precio es mayor a $100, aplica un descuento del 15%. 
#Muestra el precio final.

#Colocar el precio del preducto 

Producto = int(input("Escriba el precio del producto que desea comprar"))

#vereficar si el producto es mayor a 100 
Mayor = 100 

#Aplicar el descuento del 15% al producto 

if Producto >= Mayor: 
    descuento = Producto * 0.15
    Preciofinal = Producto - Mayor * 0.85 
    print(f"El precio final es:{Preciofinal}")
else: 
    print(f"El precio sin el descuento seria: {Producto}")

 