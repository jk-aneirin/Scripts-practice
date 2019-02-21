#!/usr/bin/python3
class BitNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def has_value(self,value):
        if self.data == value:
            return True
        else:
            return False

class BitTree:
    def __init__(self):
        self.root = None
        self.bitList = []

    def add_item(self,item):
        if not isinstance(item,BitNode):
            item = BitNode(item)

        if self.root is None:
            self.root = item
            self.bitList.append(item)
        else:
            rootNode = self.bitList[0]
            while True:
                if item.data < rootNode.data:
                    if rootNode.left == None:
                        rootNode.left = item
                        self.bitList.append(item)
                        break
                    else:
                        rootNode = rootNode.left
                elif item.data > rootNode.data:
                    if rootNode.right is None:
                        rootNode.right = item
                        self.bitList.append(item)
                        break
                    else:
                        rootNode = rootNode.right
    def front_traverse(self,root):
        if root == None:
            return
        print(root.data)
        self.front_traverse(root.left)
        self.front_traverse(root.right)

    def last_traverse(self,root):
        if root == None:
            return
        self.last_traverse(root.left)
        self.last_traverse(root.right)
        print(root.data)



if __name__ == "__main__":
    node1 = BitNode(15)
    node2 = BitNode(9)
    node3 = BitNode(8)
    node4 = BitNode(16)
    node5 = BitNode(2)
    node6 = BitNode(23)
    node7 = BitNode(1)
    node8 = BitNode(14)
    bitree = BitTree()
    for i in [node1,node2,node3,node4,node5,node6,node7,node8]:
        bitree.add_item(i)
    bitree.front_traverse(bitree.root)
