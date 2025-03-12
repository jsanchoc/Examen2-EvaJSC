def buscarPalabra(objetivo, palabras):
    while True:
        nombre = str(input("Buscar nombre: "))

        for i in objetivo:
            if nombre == i:
                print(f"{nombre} tiene {palabras[i]} años")
            elif nombre == exit:
                print("FIN DEL PROGRAMA")
                break
            else:
                print("El nombre no existe...")



def imprimirListaInversa(lista):
    print()

nombres = ["Mengano", "Fulano", "Zutano", "Perantano"]
edades = {
    "Mengano": 0,
    "Fulano": 25,
    "Zutano": 50,
    "Perantano": 75
}

buscarPalabra(nombres, edades)

