class Node:
    def __init__(self,data,indx):
        self.data = data
        self.index = indx
        self.right = None
        self.left = None
        
class BinaryS:
    def __init__(self):
        self.node = None

    def insertHead(self,item,index):
        n = Node(item,index)
        if self.node==None:
            self.node = n
            self.node.left = BinaryS()
            self.node.right = BinaryS()
        else:
            return

    def insertLeft(self,item,index):
        n = Node(item,index)

        if self.node==None:
            self.node = n
            self.node.left = BinaryS()

        else:
            self.node.left.insertLeft(item,index)


    def insertRight(self,item,index):
        n = Node(item,index)

        if self.node==None:
            self.node=n
            self.node.right = BinaryS()

        else:
            self.node.right.insertRight(item,index)

    def preOrder(self):
        
        print(self.node.index)
        self.preOrder(self.node.left.node)
        self.preOrder(self.node.right.node)
