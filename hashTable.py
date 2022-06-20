
class LinkedList:
    def __init__(self,newNodeData):
        newNode = ListNode(newNodeData) #creating new node with passed data
        self.start = newNode
        self.end = newNode
    
    def push(self,newNodeData): #add new node to end
        newNode = ListNode(newNodeData)
        self.end.next = newNode #set current end node to point right to new end
        newNode.prev = self.end #set new node to point left to old end
        self.end = newNode #set end to new end
    
    def getNodes(self):
        nodes = []
        curNode = self.start
        while True:
            nodes.append(curNode.data)
            if curNode.next == None:
                break
            else:
                curNode = curNode.next
        return nodes

class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

class HashTable:
    def __init__(self,length):
        self.table = [None] * length
        self.length = length
    
    def hash(self,data):
        total = 0
        for char in data:
            total += ord(char)
        return total % self.length
    
    def insert(self,data):
        index = self.hash(data)
        if self.table[index] == None:
            self.table[index] = LinkedList(data)
        else: #deal with collisions using chaining
            self.table[index].push(data) #add new data to linked list

    def getAtIndex(self,index):
        data = self.table[index]
        if data != None:
            return data.getNodes()
        else:
            return None
            
    def printTable(self):
        for i,data in enumerate(self.table):
            if data != None:
                print(i,data.getNodes())
            else:
                print(i,'Empty')


