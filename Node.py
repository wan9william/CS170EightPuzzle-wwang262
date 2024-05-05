import math

class Node:
    def __init__(self, state):
        self.state = state
        self.children = []
        self.parent = None
        self.lastAction = -1 
        self.size = int(math.sqrt(len(self.state)))
        self.depth = 0
    def addChild(self,node):
        node.parent = self
        node.depth = self.depth + 1
        self.children.append(node)
    def addChildren(self,nodes):
        for n in nodes:
            n.parent = self
            n.depth = self.depth + 1
            self.children.append(n)
    def getPath(self):
        path = []
        currNode = self
        while currNode.parent != None:
            path.append(currNode.lastAction)
            currNode = currNode.parent
        path.reverse()
        pathstr = str(path).replace("4", "D").replace("3", "U").replace("2", "R").replace("1", "L")
        return pathstr
    def __str__(self):
        value = ""
        for x in range(0, self.size*self.size,self.size):
            value += (str(self.state[x:x+self.size]) + "\n")
        return value
    
    
# n = Node([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
# print(n)


# n2 = Node([[1,2,3,4], [1,2,3,4],[4,5,6,12], [7,8,0,2]])
# n.addChild(n2)
# print(n.children[0].parent)

    