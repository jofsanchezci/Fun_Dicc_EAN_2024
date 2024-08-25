def crear_diccionario_cuadrados():
    numero = int(input("Ingresa un número entero positivo: "))
    diccionario = {i: i ** 2 for i in range(1, numero + 1)}
    print(diccionario)

crear_diccionario_cuadrados()


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
