# Gestión de memoria en Python

## ¿En qué consiste el programa?

Este trabajo muestra dos ejemplos de gestión de memoria en Python: memoria estática y memoria dinámica.

El programa de memoria estática utiliza una cantidad fija de 5 espacios para guardar calificaciones. En cambio, el programa de memoria dinámica utiliza una lista de frutas que puede aumentar o disminuir durante la ejecución.

## Memoria estática

En este programa se define un tamaño fijo de 5 elementos. Se reservan 5 espacios para almacenar las calificaciones y después se solicita al usuario que ingrese cada una.

Al finalizar, el programa muestra las calificaciones almacenadas en los espacios fijos.

## Memoria dinámica

En este programa se crea una lista vacía llamada `frutas`, por lo que no se especifica un tamaño inicial.

Después se agregan diferentes frutas utilizando el método `append()`:

- Mango
- Manzana
- Granada
- Durazno

Posteriormente se eliminan algunos elementos mediante su índice y finalmente se agrega una nueva fruta, `Sandía`.

Al final se muestra el estado de la lista.

## Diferencia entre ambos ejemplos

La memoria estática trabaja con una cantidad de espacios definida previamente, mientras que la memoria dinámica permite agregar o eliminar elementos durante la ejecución del programa.

## Lenguaje utilizado

- Python
