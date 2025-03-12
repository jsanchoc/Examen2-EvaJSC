# Examen2-EvaJSC

1. [Función buscarPalabra](#P1)
2. [Función imprimirListaInvertida](#P2)
3. [Llamada de funciones](#P3)

En este examen de **Entornos de Desarrollo**, teníamos que, en *python*, hacer dos funciones, ***buscarPalabra()*** e ***imprimirListaInversa()***.

<div id="P1">

###  1. buscarPalabra()
```py
def buscarPalabra(objetivo, palabras):
```
> Cuenta con dos parámetros

Dentro de está función tenemos lo siguiente:
```py
while True:
        print()
        nombre = str(input("Buscar nombre: "))

        if nombre not in objetivo and nombre != "exit":
            print("el nombre no existe...")
        elif nombre == "exit":
            break
```
La función contiene un while, el cual pregunta al usuario que introduzca un nombre, el cual más adelante comprueba con el parámetro objetivo, para que en caso de que no esté en la lista, y no sea exit, imprima por pantalla *"El nombre no existe"*, y en caso de que sea exit, termine el bucle.


```py
else:
            for i in objetivo:
                if nombre == i:
                    print(f"{nombre} tiene {palabras[i]} años")
                
    print("\nFIN DEL PROGRAMA")
```
Aquí, coje el caso de que si este en el parámetro objeto, y lo recorre entero para ver si está y en que posición está para poder asignarle la edad.
Por último hace un *print()* finalizando el programa.

<br>
<div id="P2">

### 2. imprimirListaInvertida

```py
def imprimirListaInversa(lista):
```
>Esta función toma solo un parámetro

```py
    return lista[::-1]
```
Esta función es sencilla porque la he hecho de forma ***cochina***

<br>

Por último llama a las variables, y les asigna los parámetros.
```py
print(imprimirListaInversa(nombres))
buscarPalabra(nombres, edades)
```
