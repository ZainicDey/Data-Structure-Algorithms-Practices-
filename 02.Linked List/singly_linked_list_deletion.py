#Node that will take two block of data: 1.element, 2.address of next element
class Node:
    def __init__(self,value=None):
        self.value = value
        #by default the address of next node is none for later implementation
        self.next = None

#the structure of a linear list with different functionalities
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insertAtAny(self,value, position):
        #position 0 means insert at head and position last means insert at tail otherwise in the middle 
        if position == 0:
            newNode = Node(value)
            newNode.next = self.head
            self.head = newNode
            #when the list is empty, we have to do the same for the first insertion
            if self.tail is None:
                self.tail = newNode
            return
        
        temp = self.head
        cur = 0

        while(cur < position-1 and temp is not None):
            temp = temp.next
            cur+=1
        
        #seeing whether the poisition to insert the element is valid, if temp moves to the end without reaching it's location then the position is invalid
        if temp is None or  cur < position - 1:
            print('Invalid position')
        else:
            newNode = Node(value)
            if temp.next is None:
                self.tail = newNode
            newNode.next = temp.next
            temp.next = newNode
    def delete_node(self,position):
        if self.head == None:
            print('Nothing to delete')
            return
        if position == 0:
            tempNode = self.head
            self.head = self.head.next
            if self.head == None:
                self.tail = None
        else:
            tempNode = self.head
            count = 1
            while count < position and tempNode.next is not None:
                count+=1
                tempNode = tempNode.next
            if count != position or tempNode.next is None:
                print('Invalid Position')
                return
            tempNode.next = tempNode.next.next
            if tempNode.next == None:
                self.tail = tempNode
    def print(self):
        if self.head is None:
            print('list is empty')
        else:
            temp = self.head
            while(temp is not None):
                if temp.next is None:
                    print(temp.value)
                else:
                    print(f'{temp.value}->', end='')
                temp = temp.next
            print()
#the main fucntion operations             
singly = SinglyLinkedList()
while True:
    print('Choose option:')
    n = int(input('1.Insert element\n2.Delete an element\n3.Print the list\n'))
    if n==1:
        value = int(input('Enter the element:'))
        position = int(input('Enter the postion:'))
        singly.insertAtAny(value,position)
    elif n==2:
        position = int(input('Enter the postion to delete:'))
        singly.delete_node(position)
    elif n==3:
        singly.print()