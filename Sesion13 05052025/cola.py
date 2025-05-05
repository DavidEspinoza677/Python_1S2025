from collections import deque

class Cola:
    def __init__(self):
        self.cola = deque()

    def encolar(self, elemento):
        self.cola.append(elemento)

    def desencolar(self):
        if not self.esta_vacia():
            return self.cola.popleft()
        return None
    
    def esta_vacia(self):
        return len(self.cola) == 0