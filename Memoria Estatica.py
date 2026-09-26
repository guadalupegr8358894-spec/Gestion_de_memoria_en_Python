# ==========================================
# EJEMPLO: Memoria Estática en Python
# ==========================================

# Se define explícitamente un tamaño fijo de 5 elementos
TAMANO_FIJO = 5

# Reservamos 5 espacios predefinidos en memoria (simulando memoria estática)
calificaciones = [0] * TAMANO_FIJO

print("=== MEMORIA ESTÁTICA ===")
print(f"Espacios reservados en memoria: {len(calificaciones)}")

# Ciclo for exactamente como el del video (de 0 a 4)
for i in range(TAMANO_FIJO):
    # Se solicita la entrada y se convierte a entero
    entrada = input(f"Ingrese la calificación {i + 1}: ")
    calificaciones[i] = int(entrada)

print("\nCalificaciones almacenadas en los espacios fijos:")
print(calificaciones)