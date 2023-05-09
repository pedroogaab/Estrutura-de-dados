class Node:
    
    def __init__(self, data):
        
        self.data = data
        self.right = None
        self.left = None
        
class Tree:
    """
    Arvore binaria de busca - implementacao dinamica
    """

    def __init__(self):
        self.root = None
        
    def insert(self, data, node = None):
        """
        Insere um novo noh. Considera a regra de arvores
        binarias de busca em que a subarvore esquerda de um determinado noh 
        deve ter uma chaves menores que a desse noh, enquanto que a subarvore direita 
        deve ter chaves maiores
        """
        
        # se a arvore ainda nao possui noh raiz
        if self.root == None:
            self.root = Node(data)
            
        else:
            
            if node is None: 
                node = self.root
        
            # se o valor do novo noh for menor que o valor do noh atual, insere na esquerda
            if data < node.data:
                
                if node.left is None:
                    
                    # insere um novo noh com o valor desejado na esquerda
                    node.left = Node(data)
                    
                else:
                    # se ja existe um noh na esquerda, nao podemos inserir o novo noh
                    # diretamente. Precisamos chamar a funcao insert recursivamente no 
                    # noh da esquerda
                    self.insert( data, node.left )
                
                
            # se o valor do novo noh for maior ou igual que o valor do noh atual, insere na direita
            else:
                
                if node.right is None:
                    
                    # insere um novo noh com o valor desejado na direita
                    node.right = Node(data)
                    
                else:
                    # se ja existe um noh na direita, nao podemos inserir o novo noh
                    # diretamente. Precisamos chamar a funcao insert recursivamente no 
                    # noh da direita
                    self.insert( data, node.right )
                    
                    
    def delete(self, searchedData, node = -1):
        """
        Deleta o noh que possui valor igual ao que foi informado na entrada.
        """
        
        if node == -1:
            node = self.root 
            
        previousNode = None
        encontrou = False
        while node is not None and encontrou == False:
            
            # se o dado que sera removido for igual ao dado do noh atual
            if searchedData == node.data:
                
                encontrou = True
                
                # se o previousNode eh None, significa que estamos removendo a raiz.
                # Portanto, devemos setar a raiz adequadamente
                if previousNode == None:
                    
                    # se a esquerda e direita do noh que sera excluido sao none, significa que a arvore ficara vazia
                    if node.left is None and node.right is None:
                        self.root = None
                    
                    # se o filho da esquerda eh None, a raiz recebe a subarvore da direita
                    elif node.left is None:
                        self.root = node.right
                        
                    # se o filho da direta eh None, a raiz recebe a subarvore da esquerda
                    elif node.right is None:
                        self.root = node.left
                        
                    # trata o caso onde o noh a ser removido tem filho na direita e na esquerda
                    # substitui o noh a ser excluido por um sucessor: aquele mais a esquerda da subarvore a direita
                    # outra opcao de sucessor que poderia ter sido usada eh: o noh mais a direita da subárvore esquerda
                    else:

                        # noh pai do no que ira se tornar o sucessor
                        auxPrevSucessor = node
                        
                        # noh que ira se tornar o sucessor
                        auxSucessor = node.right
                        
                        # atualiza o no noh sucessor na arvore: aquele mais a esquerda da 
                        # subarvore da direita do noh que sera removido
                        while auxSucessor.left is not None:
                            auxPrevSucessor = auxSucessor
                            auxSucessor = auxSucessor.left
                           
                        # caso o noh pai do sucessor seja diferente do noh que sera removido
                        # o seu filho a esquerda sera None, porque ele ira se tornar um noh folha
                        if auxPrevSucessor != node:
                            auxPrevSucessor.left = None

                        # caso o noh sucessor nao seja o proprio noh a direita do noh a ser removido,
                        # ele devera assumir o filho da direita do noh a ser removido                       
                        if auxSucessor != node.right:
                            auxSucessor.right = node.right
                           
                        # o noh sucessor deve assumir o filho da esquerda do noh que sera removido
                        auxSucessor.left = node.left
                        
                        self.root = auxSucessor

                # se o valor do noh anterior for > que o noh atual, 
                # segnifica que o noh atual esta do lado esquerdo do seu pai
                elif previousNode.data > node.data:   

                    # se a esquerda e direita do noh que sera excluido sao none, 
                    # significa que o pai dele se tornara uma folha                     
                    if node.left is None and node.right is None:
                        previousNode.left = None
                        
                    # se o filho da esquerda eh None, a pai dele recebe a subarvore da direita 
                    elif node.left is None:
                        previousNode.left = node.right
                        
                    # se o filho da direta eh None, a pai dele recebe a subarvore da esquerda
                    elif node.right is None:
                        previousNode.left = node.left
                        
                    # trata o caso onde o noh a ser removido tem filho na direita e na esquerda
                    # substitui o noh a ser excluido por um sucessor: aquele mais a esquerda da subarvore a direita
                    # outra opcao de sucessor que poderia ter sido usada eh: o noh mais a direita da subárvore esquerda
                    else:
                        
                        # noh pai do no que ira se tornar o sucessor
                        auxPrevSucessor = node
                        
                        # noh que ira se tornar o sucessor
                        auxSucessor = node.right
                        
                        # atualiza o no noh sucessor na arvore: aquele mais a esquerda da 
                        # subarvore da direita do noh que sera removido
                        while auxSucessor.left is not None:
                            auxPrevSucessor = auxSucessor
                            auxSucessor = auxSucessor.left
                           
                        # caso o noh pai do sucessor seja diferente do noh que sera removido
                        # o seu filho a esquerda sera None, porque ele ira se tornar um noh folha
                        if auxPrevSucessor != node:
                            auxPrevSucessor.left = None

                        # caso o noh sucessor nao seja o proprio noh a direita do noh a ser removido,
                        # ele devera assumir o filho da direita do noh a ser removido                       
                        if auxSucessor != node.right:
                            auxSucessor.right = node.right
                           
                        # o noh sucessor deve assumir o filho da esquerda do noh que sera removido
                        auxSucessor.left = node.left
                            
                        # o noh sucessor se tornara o filho da esquerda 
                        # do noh que sera removido
                        previousNode.left = auxSucessor


                # se o valor do noh anterior for < que o noh atual, 
                # significa que o noh atual esta do lado direito do seu pai                        
                elif previousNode.data < node.data:

                    # se a esquerda e direita do noh que sera excluido sao none, 
                    # significa que o pai dele se tornara uma folha                       
                    if node.left is None and node.right is None:
                        previousNode.right = None
                        
                    # se o filho da esquerda eh None, a pai dele recebe a subarvore da direita                         
                    elif node.left is None:
                        previousNode.right = node.right
                        
                    # se o filho da direta eh None, a pai dele recebe a subarvore da esquerda
                    elif node.right is None:
                        previousNode.right = node.left
                        
                    # trata o caso onde o noh a ser removido tem filho na direita e na esquerda
                    # substitui o noh a ser excluido por um sucessor: aquele mais a esquerda da subarvore a direita
                    # outra opcao de sucessor que poderia ter sido usada eh: o noh mais a direita da subárvore esquerda
                    else:
                        
                        # noh pai do no que ira se tornar o sucessor
                        auxPrevSucessor = node
                        
                        # noh que ira se tornar o sucessor
                        auxSucessor = node.right
                        
                        # atualiza o no noh sucessor na arvore: aquele mais a esquerda da 
                        # subarvore da direita do noh que sera removido
                        while auxSucessor.left is not None:
                            auxPrevSucessor = auxSucessor
                            auxSucessor = auxSucessor.left
                           
                        # caso o noh pai do sucessor seja diferente do noh que sera removido
                        # o seu filho a esquerda sera None, porque ele ira se tornar um noh folha
                        if auxPrevSucessor != node:
                            auxPrevSucessor.left = None

                        # caso o noh sucessor nao seja o proprio noh a direita do noh a ser removido,
                        # ele devera assumir o filho da direita do noh a ser removido                       
                        if auxSucessor != node.right:
                            auxSucessor.right = node.right
                           
                        # o noh sucessor deve assumir o filho da esquerda do noh que sera removido
                        auxSucessor.left = node.left

                        # o noh sucessor se tornara o filho da esquerda 
                        # do noh que sera removido                            
                        previousNode.right = auxSucessor

            # se o dado que sera removido for menor que o dado do noh atual                            
            elif searchedData < node.data:
                
                # se o filho da esquerda eh None, significa que o dado que 
                # foi passado como entrada nao existe na arvore
                if node.left is None:
                    node = None
                    print('Valor não encontrado')                    
                
                else:
                    # atualiza o noh atual e o seu pai
                    previousNode = node
                    node = node.left   


            # se o dado que sera removido for maior que o dado do noh atual                 
            else:
                
                # se o filho da direita eh None, significa que o dado que 
                # foi passado como entrada nao existe na arvore
                if node.right is None:
                    node = None
                    print('Valor não encontrado')   
                    
                else:
                    # atualiza o noh atual e o seu pai
                    previousNode = node
                    node = node.right   

            
        # deleta o noh
        del node

             
    def strInorder(self, node = -1, info = ''):
        """
        Retorna uma string com os valores da arvore obtidos apos 
        o percurso "Em Ordem"
        """
        
        if self.root is None:
            return ' '
            
        else:
            
            if node==-1:
                node = tree.root
            
            if node.data is not None:
                
                if node.left is not None: 
                    info += self.strInorder(node.left)
                    
                info += ' ' + str(node.data) #print(data)
                
                if node.right is not None:
                    info += self.strInorder(node.right)
                    
                return info
            else:
                return info
            
            
    def strPreorder(self, node = -1, info = ''):
        """
        Retorna uma string com os valores da arvore obtidos apos 
        o percurso "Pre Ordem"
        """
        
        if self.root is None:
            return ' '
            
        else:
            
            if node==-1:
                node = tree.root
            
            if node.data is not None:
                
                info += ' ' + str(node.data)
                
                info += '('
                
                if node.left is not None: 
                    info += self.strPreorder(node.left)
                
                if node.right is not None:
                    info += self.strPreorder(node.right)
                    
                info += ' )'
                
                return info
            else:
                return info
            
    def strPostorder(self, node = -1, info = ''):
        """
        Retorna uma string com os valores da arvore obtidos apos 
        o percurso "Pre Ordem"
        """
        
        if self.root is None:
            return ' '
            
        else:
            
            if node==-1:
                node = tree.root
            
            if node.data is not None:
                              
                if node.left is not None: 
                    info += self.strPostorder(node.left)
                
                if node.right is not None:
                    info += self.strPostorder(node.right)
                    
                info += ' ' + str(node.data)
                    
                return info
            else:
                return info
            
        
    def buscar(self, searchedData, node = -1):
    
        if node == -1:
            node = self.root
            
        if node.data is not None:
            
            if searchedData == node.data:
                return True
            
            elif searchedData < node.data:
                
                if node.left is not None: 
                    return self.buscar( searchedData, node.left )
                else: 
                    return False
            else:
                if node.right is not None:
                    return self.buscar( searchedData, node.right )
                else:
                    False
        else:
            return False 

if __name__ == "__main__":
    #---------------------    
    # testando a arvore
    
    tree = Tree()
    tree.insert(6)
    tree.insert(2)
    tree.insert(7)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)
    tree.insert(4)
    info = tree.strInorder()
    print('strInorder():', info)
    
    info = tree.strPostorder()
    print('strPostorder():', info)
    
    info = tree.strPreorder()
    print('strPreorder():', info)
            
    res = tree.buscar(18)
    print('buscar(18): ', res)
        
    res = tree.buscar(23)
    print('buscar(23): ', res)  
    
    tree.delete(17)
    print('delete(17):', tree.strPreorder())
    
    tree.delete(48)
    print('delete(48):', tree.strPreorder())
    
    tree.delete(6)
    print('delete(6):', tree.strPreorder())
    
    tree.delete(4)
    print('delete(4):', tree.strPreorder())
    
    tree.delete(14)
    print('delete(14):', tree.strPreorder())
    
    tree.delete(23)
    print('delete(6):', tree.strPreorder())
    
    tree.delete(35)
    print('delete(6):', tree.strPreorder())
    
    tree.insert(17)
    print('insert(17):', tree.strPreorder())  
    
    tree.delete(18)
    print('delete(18):', tree.strPreorder())
