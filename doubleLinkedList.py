class Node:
    def __init__(self, value) -> None:
        self.previous = None
        self.next = None
        self.value = value
    

class DoubleLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None
        self.size = 0

    def add(self, node_val):
        node = Node(value=node_val) 
        if self.tail_node is None:  # tail none means the list is empty 
            self.head_node = node
            self.tail_node = node
            self.size += 1

        else:
            self.tail_node.next = node
            node.previous = self.head_node
            self.tail_node = node            
            self.size += 1

    


    def __str__(self):
        list_values = []
        node = self.head_node

        while node is not None:
            list_values.append(node.value)
            node = node.next

        return str(list_values)

my_list = DoubleLinkedList()
my_list.add(5)
my_list.add(6)
my_list.add(99)
print(my_list)