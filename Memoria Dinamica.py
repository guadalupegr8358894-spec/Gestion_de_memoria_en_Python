# ==========================================
# EJEMPLO: Memoria Dinámica en Python
# ==========================================

print("=== MEMORIA DINÁMICA ===")

# Se crea la lista dinámica sin especificar un tamaño inicial
frutas = []

# 1. Agregar elementos iniciales mediante el método append() (equivalente a add() en Java)
frutas.append("Mango")
frutas.append("Manzana")
frutas.append("Granada")
frutas.append("Durazno")

# Imprimir el contenido de la lista dinámica
print("Estado inicial de la lista de frutas:")
print(frutas)

# 2. Eliminar elementos por índice (equivalente a remove(índice) en Java)
# Eliminamos el elemento en el índice 0 ("Mango")
del frutas[0] 

# Eliminamos el nuevo elemento en el índice 1 (que ahora es "Granada", pues "Manzana" pasó al índice 0)
del frutas[1]

# 3. Agregar un nuevo elemento en tiempo de ejecución
frutas.append("Sandía")

# Imprimir el estado final de la lista
print("\nEstado final de la lista tras eliminar e insertar elementos:")
print(frutas)