class Node:
    def __init__(self, val) -> None:
        self.prev = None
        self.next = None
        self.value = val 

class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, val):
        node = Node(val=val)  
        if self.tail is None:
            self.tail = node
            self.head = node
            self.size += 1
        
        else:
            self.tail.next = node
            node.prev = self.head
            self.tail = node
            self.size += 1

    def __str__(self):
        list_values = []
        node = self.head

        while node is not None:
            list_values.append(node.value)
            node = node.next

        return str(list_values)


my_list = DoubleLinkedList()
my_list.add(5)
my_list.add(65)
my_list.add(555)

print(my_list)