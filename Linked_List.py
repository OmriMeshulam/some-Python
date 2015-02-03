class LinkedListNode:

    def __init__(self, in_head, in_tail):
        """Construct a new Linked List Node"""
        self.head = in_head
        self.tail = in_tail

class LinkedList:

    def __init__(self):
        """Construct a new LinkedList. The first node and last node are the same. Size is 0"""
        self.firstNode = LinkedListNode(None, None)
        self.lastNode = self.firstNode
        self.size = 0

    def add(self, data):
        """Add a node to the list"""
        node = LinkedListNode(data, None)

        if self.firstNode.head == None:
            self.firstNode = node
            self.lastNode = node
        else:
            self.lastNode.tail = node
            self.lastNode = node


        self.size += 1

    def add_many(self, list_of_data):
        """Add a list of nodes to the linked list"""
        for x in list_of_data:
            self.add(x)

    def remove(self, data):
        """Remove a node from the list"""
        currentNode = self.firstNode
        wasDeleted = False

        if self.size == 0:
            pass

        # The first node is being removed
        if data == currentNode.data:
            # This is the case where we have only one node in the list
            if currentNode.tail == None:
                self.firstNode = LinkedListNode(None, None)
                self.lastNode = self.firstNode
                self.size = self.size - 1
                return

            # Here there are more than one nodes in the list
            currentNode = currentNode.next
            self.firstNode = currentNode
            self.size = self.size - 1
            return;

        while True:

            if currentNode == None:
                wasDeleted = False
                break

            # Check if the data of the next is what we're looking for
            nextNode = currentNode.next
            if nextNode != None:
                if data == nextNode.head:
                    # Found the right one, loop around the node
                    nextNextNode = nextNode.tail
                    currentNode.tail = nextNextNode

                    nextNode = None
                    wasDeleted = True
                    break

            currentNode = currentNode.next

        if wasDeleted:
            self.size = self.size - 1;

    def remove_many(self, list_of_data):
        """Remove a list of nodes from the linked list"""
        for x in list_of_data:
            self.remove(x)

    def get_list_str(self):
        """Get a string representation of the list"""
        result = ""
        currentNode = self.firstNode
        i = 0
        result += "{"

        while currentNode != None:
            if i > 0:
                result = result + ","

            dataObj = currentNode.head

            if dataObj != None:
                result = result + str(dataObj)

            currentNode = currentNode.tail

            i = i + 1

        result = result + "}"
        return result
        
    def contains(self, data):
        """Check whether a node is in the list or not"""
        currentNode = self.firstNode

        while currentNode != None:
            if currentNode.head == head:
                return True
            else:
                currentNode = currentNode.tail

        return False

    def index_of(self, data):
        """Find the position of a node in the list"""
        currentNode = self.firstNode
        pos = 0

        while currentNode != None:
            if (currentNode.head == head):
                return pos
            else:
                currentNode = currentNode.tail
                pos = pos + 1

        return -1    

    def get_size(self):
        """Get the size of the list"""
        return self.size

    def print_list(self):
        print (myList.get_list_str())
        
#    def recursiveCounter(self):
#        if (self.firstNode.tail == None):
#            return 1
#       return 1 + self.recursiveCounter(firstNode.tail)
		
myList = LinkedList()
myList.add(1)
myList.add(2)
myList.add(3)
print (myList.get_list_str())

myList.add_many([4,3,7,6,4,5,6,5])
myList.print_list()
#recursiveNumber = myList.recursiveCounter()
print ("The number of items in the list is", myList.get_size())
     
