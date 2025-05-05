from cola import Cola

class Banco:
    def __init__(self):
        self.cola = Cola()

    def llegar_cliente(self, cliente):
        self.cola.encolar(cliente)
    
    def atender_cliente(self):
        self.ultimo_cliente = self.cola._clientes.desencolar()
        return self.ultimo_cliente
    
    def obtener_clientes_en_espera(self):
        return self.cola_clienes._clientes()
    
    def obtener_ultimo_cliente(self):
        return self.ultimo_cliente