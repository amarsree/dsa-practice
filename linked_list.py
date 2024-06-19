class Node:
    def __init__(self, data) -> None:
        self.next = None
        self.val = data



class LinkedList():
    def __init__(self) -> None:
        self.head=None

    
    def insertAtBeginning(self, data) -> None:
        new_node = Node(data)
        new_node.val = data
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head= new_node
        print(data +' inserted at beginning')

    def insertAtEnd(self, data):
        new_node =  Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            # while(True):
            #     if current.next is None:
            #         current.next = new_node
            #         print(data + " inserted")
            #         break
            #     else:
            #         current = current.next
            while(current.next):
                current=current.next

            print(data + " inserted at end")
            current.next=new_node

        
            
    def printAll(self):
        res=''
        if self.head is None :
            res='list is empty'
        else:
            current = self.head
            while(current):
               # print(current.val)
                res= res+ current.val +  ('' if (current.next is None) else '->')
                current=current.next
        print(res)

    def insertAtIndex(self, data, index):
        new_node = Node(data)
        if(index==0):
            self.insertAtBeginning(data)
            return 
        else:
            pos= 1
            current=self.head
            while(current.next):
                if(index == pos):
                    new_node.next=current.next
                    current.next=new_node
                    break
                else:
                    current=current.next
                pos=pos+1

    def updateAtIndex(self,value,index):
        current = self.head
        pos=0
        while(current):
            if(index==pos):
                current.val=value
                
            else:
                current=current.next
            pos=pos+1

    def linkedListLength(self):
        current=self.head
        lng=0
        while(current):
            lng=lng+1
            current=current.next
        
        print('size is '+ str(lng))

                    


    def _isEmptyList(self):
        if self.head is None:
            return True
        else:
            return False



list = LinkedList()

list.linkedListLength()
# list.insertAtBeginning('a')
list.insertAtBeginning("b")
list.linkedListLength()
list.insertAtEnd("c")
list.insertAtEnd("d")

list.printAll()

list.insertAtBeginning('f')
list.insertAtBeginning('f')
list.insertAtBeginning('f')
list.insertAtBeginning('f')
list.insertAtIndex('x',6)
list.updateAtIndex('y',1)
list.linkedListLength()

list.printAll()