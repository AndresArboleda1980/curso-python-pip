class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def eliminar(self, valor):
        if not self.cabeza:
            return

        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente
            if not self.cabeza:
                self.cola = None
            return

        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.valor == valor:
                actual.siguiente = actual.siguiente.siguiente
                if not actual.siguiente:
                    self.cola = actual
                return
            actual = actual.siguiente

    def mostrar(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(actual.valor)
            actual = actual.siguiente
        return elementos

    def __iter__(self):
        self.actual = self.cabeza
        return self

    def __next__(self):
        if self.actual is None:
            raise StopIteration
        valor = self.actual.valor
        self.actual = self.actual.siguiente
        return valor

# Crear una lista enlazada con 4 valores aleatorios
lista = ListaEnlazada()
valores_aleatorios = [42, 17, 8, 99]

for valor in valores_aleatorios:
    lista.agregar(valor)

# Utilizar el iterador para recorrer y mostrar la lista enlazada
print("Recorriendo la lista enlazada con el iterador:")
for elemento in lista:
    print(elemento)
