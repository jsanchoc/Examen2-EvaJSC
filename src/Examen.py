def buscarPalabra(objetivo, palabras):
    while True:
        print()
        nombre = str(input("Buscar nombre: "))

        if nombre not in objetivo and nombre != "exit":
            print("el nombre no existe...")
        elif nombre == "exit":
            break
        else:
            for i in objetivo:
                if nombre == i:
                    print(f"{nombre} tiene {palabras[i]} años")
                
    print("\nFIN DEL PROGRAMA")


def imprimirListaInversa(lista):
    return lista[::-1]
        

nombres = ["Mengano", "Fulano", "Zutano", "Perantano"]
edades = {
    "Mengano": 0,
    "Fulano": 25,
    "Zutano": 50,
    "Perantano": 75
}

print(imprimirListaInversa(nombres))
buscarPalabra(nombres, edades)

