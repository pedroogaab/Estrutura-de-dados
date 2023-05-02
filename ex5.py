################# ESCREVA SEU CÓDIGO AQUI  ###############################
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class pilhaFila:
    def __init__(self):
        
        self.get_top = None
        self.get_tail = None
        
        self.get_front = None
        self.get_rear = None
        
        self.get_size = 0
        
        self.pilha = False
        self.fila = False
        
    def size(self):
        return self.get_size
    
    
    def isEmpty(self):
        return self.get_size == 0


    def push(self, data):
        noh = Node(data)

        if self.get_top is None:
            self.get_top = noh
            self.get_tail = noh
        else:
            noh.next = self.get_top
            self.get_top = noh
            
        self.pilha = True
        self.fila = False
        self.get_size += 1
        
        
    def pop(self):
        if self.get_top is None:
            return self.isEmpty()

        data = self.get_top.data
        self.get_top = self.get_top.next
        self.get_size -= 1

        if self.get_top is None:
            self.get_tail = None

        self.pilha = True
        self.fila = False
        
        self.get_rear = self.get_top if self.get_top is not None else None
        return data


    def enqueue(self, data):
        noh = Node(data)

        if self.get_front is None:
            self.get_front = noh
            self.get_rear = noh
        else:
            self.get_rear.next = noh
            self.get_rear = noh
            
        self.pilha = False
        self.fila = True
        self.get_size += 1

    def dequeue(self):
        if self.get_front is None:
            return self.isEmpty()

        data = self.get_front.data
        self.get_front = self.get_front.next
        self.get_size -= 1

        if self.get_front is None:
            self.get_tail = None

        self.pilha = False
        self.fila = True
        self.get_rear = self.get_tail if self.get_tail is not None else None
        return data
        

    def top(self):
        if self.get_top is None:
            return self.isEmpty()

        return self.get_top.data


    def front(self):
        if self.get_front is None:
            return self.isEmpty()
        
        return self.get_front.data
        
        
    def rear(self):
        if self.get_rear is None:
            return self.isEmpty()
        else:
            return self.get_rear.data

    
    def __str__(self):
        
        _str = ""
        if self.pilha:
            _str += "aaaaaaaaa" + " "
        else: _str += "bbbbbbbbb" + " "
        
        _str = _str.strip()
        return "[" + _str + "]"


    def clear(self):

        while not self.isEmpty():
            data = self.pop()



##########################################################################
       
# testando a PilhaFila
pilhaFila1 = pilhaFila()

pilhaFila1.push(5)
print(pilhaFila1)

pilhaFila1.enqueue(3)
print(pilhaFila1)

pilhaFila1.push(9)
print(pilhaFila1)

print( 'Size: ', pilhaFila1.size() )

valor = pilhaFila1.pop()
print(pilhaFila1)

valor = pilhaFila1.dequeue()
print(pilhaFila1)

print( 'Vazia?: ', pilhaFila1.isEmpty() )

valor = pilhaFila1.pop()
print(pilhaFila1)

print( 'Vazia?: ', pilhaFila1.isEmpty() )

valor = pilhaFila1.pop()
print(pilhaFila1)

pilhaFila1.push(2)
print(pilhaFila1)

pilhaFila1.push(14)
print(pilhaFila1)

print(pilhaFila1.front())
print(pilhaFila1.rear())
print(pilhaFila1.top())

print( 'Vazia?: ', pilhaFila1.isEmpty() )

pilhaFila1.clear()
print( 'Vazia?: ', pilhaFila1.isEmpty() )

print('\n' + 20*'-')
print('Resultado esperado:')
print("\nLista:\n")
print('[ 5 ]')
print('[ 5, 3 ]')
print('[ 5, 3, 9 ]')
print('Size:  3')
print('[ 5, 3 ]')
print('[ 3 ]')
print('Vazia?:  False')
print('[ ]')
print('Vazia?:  True')
print('pilhaFila1 vazia')
print('[ ]')
print('[ 2 ]')
print('[ 2 14 ]')
print('2')
print('14')
print('14')
print('Vazia?:  False')
print('Vazia?:  True)')