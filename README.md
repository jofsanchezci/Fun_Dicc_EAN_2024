# Ejercicios de Funciones

## Programa para calcular la raíz cuarta de un número real
```
import math

def calcular_raiz_cuarta():
    numero = float(input("Ingresa un número real: "))
    raiz_cuarta = math.sqrt(math.sqrt(numero))
    print(f"La raíz cuarta de {numero} es: {raiz_cuarta:.4f}")

calcular_raiz_cuarta()
```

## Programa para calcular el área de un círculo

```
import math

def calcular_area_circulo():
    radio = float(input("Ingresa el radio del círculo: "))
    area = math.pi * (radio ** 2)
    print(f"El área del círculo con radio {radio} es: {area:.4f}")

calcular_area_circulo()
```

## Programa para calcular el precio de venta de un artículo
```
def calcular_precio_venta():
    nombre_producto = input("Ingresa el nombre del producto: ")
    costo_produccion = float(input(f"Ingrese el costo de producción de {nombre_producto}: "))

    utilidad = costo_produccion * 1.20
    impuestos = (costo_produccion + utilidad) * 0.15
    precio_venta = costo_produccion + utilidad + impuestos

    print(f"El precio de venta del producto '{nombre_producto}' es: {precio_venta:.2f}")

calcular_precio_venta()
```
# Ejercicios de Diccionarios

## Función que crea un diccionario con claves desde 1 hasta un número indicado, y valores como los cuadrados de las claves
```
def crear_diccionario_cuadrados():
    numero = int(input("Ingresa un número entero positivo: "))
    diccionario = {i: i ** 2 for i in range(1, numero + 1)}
    print(diccionario)

crear_diccionario_cuadrados()

```

## Función que recibe una cadena y devuelve un diccionario con la cantidad de apariciones de cada carácter

```
def contar_caracteres(cadena):
    diccionario = {}
    for caracter in cadena:
        if caracter in diccionario:
            diccionario[caracter] += 1
        else:
            diccionario[caracter] = 1
    return diccionario

# Ejemplo de uso
cadena = input("Ingresa una cadena: ")
resultado = contar_caracteres(cadena)
print(resultado)

```

## Programa que maneja un diccionario de precios de frutas y calcula el precio final basado en la cantidad vendida
```
def consultar_precio_fruta():
    precios_frutas = {
        'manzana': 2.5,
        'naranja': 1.2,
        'platano': 1.8,
        'pera': 2.1
    }

    while True:
        fruta = input("Ingresa el nombre de la fruta: ").lower()
        if fruta in precios_frutas:
            cantidad = float(input(f"Ingresa la cantidad vendida de {fruta}: "))
            precio_final = precios_frutas[fruta] * cantidad
            print(f"El precio final de {cantidad} {fruta}(s) es: {precio_final:.2f}")
        else:
            print(f"Error: La fruta '{fruta}' no está disponible.")

        otra_consulta = input("¿Deseas realizar otra consulta? (sí/no): ").lower()
        if otra_consulta != 'sí':
            break

consultar_precio_fruta()

```
