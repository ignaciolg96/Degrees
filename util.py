class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)  # Agrego un nodo a la frontera en último lugar

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)   # Chequea si algún nodo contiene el estado argumento

    def empty(self):
        return len(self.frontier) == 0  # Chequear si la frontera está vacía

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]    # Selecciona el último elemento(nodo) de la lista
            self.frontier = self.frontier[:-1]  # Remuevo el último nodo
            return node     # Devuelvo el nodo extraído


class QueueFrontier(StackFrontier):
    # HEREDA de StackFrontier! Es decir que comparte sus método. 
    # OJO: el remove SOBREESCRIBE (creo) el método del padre 
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]     # Selecciono el primer nodo
            self.frontier = self.frontier[1:]   # Remueve el primer nodo
            return node     # Devuelvo el nodo
