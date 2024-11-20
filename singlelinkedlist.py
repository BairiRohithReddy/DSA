class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length +=1
            currentNode = currentNode.next
        return length
        
    def insertHead(self, newNode):
        currentHead = self.head
        self.head = newNode
        self.head.next = currentHead
    
    def insertAt(self, newNode, position):
        if position == 0:
            self.insertHead(newNode)
            return
        if position < 0 or position > self.listLength():
            print("Invalid Position")
            return
        currentNode = self.head
        currentPosition = 0
        
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition +=1
                
    def insertend(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            # john --> Ben --> None || John --> Ben --> Matthew
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode
            
    def deleteHead(self):
        currentNode = self.head
        self.head = currentNode.next
        
            
    def deleteEnd(self):
        currentNode = self.head
        while currentNode.next is not None:
            prevNode = currentNode
            currentNode = currentNode.next
        prevNode.next = None
        
    def deleteAt(self, position):
        if position ==0:
            self.deleteHead()
            return
        if position < 0 or position > self.listLength():
            print("Invalid Position")
            return
        currentNode = self.head
        currentPosition = 0 
        while True:
            if currentPosition == position:
                prevNode.next = currentNode.next
                break
            prevNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1
            
    def mergeLists(self, list1, list2):
        l3 = LinkedList()
        l1Current = list1.head
        l2Current = list2.head
        while l1Current is not None and l2Current is not None:
            if l1Current.data < l2Current.data:
                l3.insertend(Node(l1Current.data))
                l1Current = l1Current.next
            else:
                l3.insertend(Node(l2Current.data))
                l2Current = l2Current.next
        #appending the remaining elements of list1 if any
        while l1Current is not None:
            l3.insertend(Node(l1Current.head))
            l1Current = l1Current.next
            
        #appending the remaining elements of list2 if any
        while l2Current is not None:
            l3.insertend(Node(l2Current.data))
            l2Current = l2Current.next
        
        return l3
                        
    def printList(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next
                

# firstNode = Node("John")
# linkedlist1 = LinkedList()
# linkedlist1.insertend(firstNode)
# # John --> None

# secondNode = Node("Ben")
# linkedlist1.insertend(secondNode)
# # John --> Ben --> None

# thirdNode = Node("matthew")
# linkedlist1.insertend(thirdNode)

# fourthNode = Node("kim")
# #linkedlist.insertHead(fourthNode)

# fifthNode = Node("Rohith")
# #linkedlist.insertAt(fifthNode, 4)

# #linkedlist.deleteEnd()

# #linkedlist.deleteHead()

# #linkedlist1.deleteAt(2)

print("-----------------------Linked List 1--------------------------")
linkedlist1 = LinkedList()
a = Node(1)
b = Node(3)
c = Node(4)
d = Node(6)

linkedlist1.insertend(a)
linkedlist1.insertend(b)
linkedlist1.insertend(c)
linkedlist1.insertend(d)
linkedlist1.printList()

print("-----------------------Linked List 2--------------------------")
linkedlist2 = LinkedList()
a1 = Node(2)
a2 = Node(5)
a3 = Node(8)
a4 = Node(9)

linkedlist2.insertend(a1)
linkedlist2.insertend(a2)
linkedlist2.insertend(a3)
linkedlist2.insertend(a4)
linkedlist2.printList()

linkedlist = LinkedList()
linkedlist = linkedlist.mergeLists(linkedlist1, linkedlist2)
print("-----------------------Merged List--------------------------")
linkedlist.printList()