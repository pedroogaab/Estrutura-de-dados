class Node:
    
    def __init__(self, data, next=None):
        
        self.data = data
        self.next = next
        
class Deque:
    """
    Deque (fila dupla) dinâmico
    """
    
    def __init__(self):
        
        self.front = None
        self.rear = None
        self.size = 0
            
    def isEmpty(self):
        
        if self.size == 0:
            return True
        else:
            return False
        
    def enqueueRear(self,valor):
        """
        Insere um elemento no final da fila
        """
        
        noh = Node( valor )
        
        if self.size==0:
            self.front = noh
            self.rear = noh
        
        else:
            self.rear.next = noh
            self.rear = noh
         
        # aumenta a qtd. de elementos da fila
        self.size += 1 
        
    def enqueueFront(self,valor):
        """
        Insere um elemento no inicio da fila
        """
        
        # cria um novo nó
        noh = Node(valor)
        
        if self.isEmpty():
            self.front = noh
            self.rear = noh
            
        else:
            
            noh.next = self.front
            
            self.front = noh

        # aumenta a qtd. de elementos da fila            
        self.size += 1
            
        
    def dequeueFront(self):
        """
        Elimina o primeiro elemento
        """
        
        if self.isEmpty():
            print('Erro. Underflow')
            return None
        else:
            
            nohAExcluir = self.front
            
            # retorna o valor
            valor = nohAExcluir.data
            
            # atualiza quem está na frente
            self.front = nohAExcluir.next
            
            # diminui o numero de elementos
            self.size -= 1
            
            # deleta o noh da memoria
            del nohAExcluir
            
            return valor
        
    def dequeueRear(self):
        """
        Elimina o ultimo elemento
        """
        
        if self.isEmpty():
            print('\nErro. Underflow')
            return None
            
        nohAExcluir = self.rear
        
        # retorna o valor
        valor = nohAExcluir.data
        
        # se o deque tiver tamanho 1, ao excluir o noh, ele ficara vazio
        if self.size==1:
            self.front = None
            self.rear = None
        else:
            # atualiza quem esta atras. Precisa tambem atualizar o next do no que sera o novo rear.
            # o unico jeito de achar o noh que sera o novo rear, eh percorrendo toda a fila
            nohAux = self.front
            novoRear = None 
            
            # Percorre a fila ate achar o elemento anterior ao rear. 
            # O laco para quando achar o rear, isto eh, um next igual ao None.
            while nohAux.next is not None:
                novoRear = nohAux
                nohAux = nohAux.next
                
            # troca o rear
            self.rear = novoRear
            
        # diminui o numero de elementos
        self.size -= 1
    
        # deleta o noh da memoria            
        del nohAExcluir
        
        return valor

    def getFront(self):
        """
        Retorna o primeiro elemento da lista sem remover
        """
        
        if self.front is None:
            print("Pilha vazia")
            return None

        # iremos retornar apenas o dado do noh, mas
        # dependendo da necessidade, poderia ser
        # retornado o noh inteiro
        return self.front.data

    def getRear(self):
        """
        Retorna o ultimo elemento da lista sem remover
        """
        
        if self.rear is None:
            print("Pilha vazia")
            return None

        # iremos retornar apenas o dado do noh, mas
        # dependendo da necessidade, poderia ser
        # retornado o noh inteiro
        return self.rear.data
        
    def getSize(self):
        """
        Retorna o tamanho da lista
        """
        
        return self.size
    
    def clear(self):
        """
        Apaga o deque
        """

        while not self.isEmpty():
            self.dequeueFront()
            
    
    def __str__(self):
          
        # fila auxiliar para imprimir a fila original
        dequeAux = Deque()
        
        # string que ira guardar os valores
        info = '[ '
        
        while not self.isEmpty():
            
            valor = self.dequeueFront()
            
            # insere na fila auxiliar
            dequeAux.enqueueRear( valor )
            
            info = info + ' ' + str(valor)
        
        info = info + ' ]'
        
        # laço para recuperar a fila 
        while not dequeAux.isEmpty():
            
            valor = dequeAux.dequeueFront()
            self.enqueueRear(valor)
            
        return info
        
if __name__ == "__main__":
       
    # testa o deque
    deque1 = Deque()
    
    deque1.enqueueFront( 5 )
    print('enqueueFront( 5 ): ', deque1) 
    
    deque1.enqueueFront( 3 )
    print('enqueueFront( 3 ): ', deque1)
    
    deque1.enqueueFront( 9 )
    print('enqueueFront( 9 ): ', deque1)
    
    deque1.enqueueRear( 15 )
    print('enqueueRear( 15 ): ', deque1)      
    
    res = deque1.getSize( )
    print('size( ): ', res, ' -- ', deque1)   
    
    res = deque1.getFront( )
    print('front( ): ', res, ' -- ', deque1)   
    
    res = deque1.getRear( )
    print('rear( ): ', res, ' -- ', deque1)   
    
    res = deque1.dequeueFront( )
    print('dequeueFront( ): ', res, ' -- ', deque1)  
    
    res = deque1.dequeueRear( )
    print('dequeueRear( ): ', res, ' -- ', deque1)  
    
    res = deque1.isEmpty( )
    print('isEmpty( ): ', res, ' -- ', deque1)  
    
    res = deque1.dequeueFront( )
    print('dequeueFront( ): ', res, ' -- ', deque1)  
    
    res = deque1.dequeueRear( )
    print('dequeueRear( ): ', res, ' -- ', deque1) 
    
    res = deque1.dequeueRear( )
    print('dequeueRear( ): ', res, ' -- ', deque1)  
    
    res = deque1.isEmpty( )
    print('isEmpty( ): ', res, ' -- ', deque1) 
    
    deque1.enqueueFront( 40 )
    print('enqueueFront( 40 ): ', deque1) 
    
    deque1.enqueueRear( 44 )
    print('enqueueRear( 44 ): ', deque1) 
    
    deque1.clear( )
    print('clear( ): ', deque1) 
    
    res = deque1.isEmpty( )
    print('isEmpty( ): ', res, ' -- ', deque1)  
    
