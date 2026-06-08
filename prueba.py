from collections import deque
# Creamos una cola vacía
cola = deque()
# Encolamos elementos
cola.append("Ana")
cola.append("Luis")
cola.append("Marta")
print("Cola actual:", cola)
# Consultamos el primer elemento
print("Primera persona:", cola[0])
# Desencolamos con popleft()
persona = cola.popleft()
print("Persona atendida:", persona)
print("Cola después de atender:", cola)