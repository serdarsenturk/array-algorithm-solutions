class Node:
    def __init(self, value):
        self.value = value
        self.nextNode = None

    
class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.data)
            currentNode = currentNode.next

    def append(self, data):
        newNode = Node(data)

        if self.head == None:
            self.head = newNode
            return
    
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = newNode

llist = LinkedList()
llist.append("A")
llist.append("B")
print(llist.printList())