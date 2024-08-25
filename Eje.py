import math

#Raiz cuadrada
def calcular_raiz_cuarta():
    numero = float(input("Ingresa un número real: "))
    raiz_cuarta = math.sqrt(math.sqrt(numero))
    print(f"La raíz cuarta de {numero} es: {raiz_cuarta:.4f}")

calcular_raiz_cuarta()


# Area de un circulo
def calcular_area_circulo():
    radio = float(input("Ingresa el radio del círculo: "))
    area = math.pi * (radio ** 2)
    print(f"El área del círculo con radio {radio} es: {area:.4f}")

calcular_area_circulo()


#Precio de venta
def calcular_precio_venta():
    nombre_producto = input("Ingresa el nombre del producto: ")
    costo_produccion = float(input(f"Ingrese el costo de producción de {nombre_producto}: "))

    utilidad = costo_produccion * 1.20
    impuestos = (costo_produccion + utilidad) * 0.15
    precio_venta = costo_produccion + utilidad + impuestos

    print(f"El precio de venta del producto '{nombre_producto}' es: {precio_venta:.2f}")

calcular_precio_venta()

