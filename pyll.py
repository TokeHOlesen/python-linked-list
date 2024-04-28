class LinkedList:
    """Implements a linked list of objects of the Node class."""
    
    class Node:
        """Implements a node in a linked list."""
        def __init__(self, value) -> None:
            self.next_node: self.Node = None
            self.value = value
    
    def __init__(self) -> None:
        self.dummy_head = self.Node(None)
        self.tail = self.dummy_head
    
    def __iter__(self):
        current_node = self.dummy_head.next_node
        while current_node is not None:
            yield current_node.value
            current_node = current_node.next_node
        
    def insert_node(self, value) -> None:
        """Inserts a node at the beginning of the list."""
        new_node = self.Node(value)
        new_node.next_node = self.dummy_head.next_node
        self.dummy_head.next_node = new_node
        
    def append_node(self, value) -> None:
        """Inserts node(s) at the end of the list."""
        last_node = self.tail
        last_node.next_node = self.Node(value)
        self.tail = last_node.next_node
    
    def insert_ordered(self, value) -> None:
        """Inserts a new node before a node with a higher value. Use to keep list ordered."""
        current_node = self.dummy_head
        new_node = self.Node(value)
        while current_node.next_node is not None and new_node.value >= current_node.next_node.value:
            current_node = current_node.next_node
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node
        if new_node.next_node is None:
            self.tail = new_node
    
    def sort(self):
        """Sorts the list using the bubble sort algorithm."""
        if self.dummy_head.next_node is None or self.dummy_head.next_node.next_node is None:
            return
        
        has_swapped = True
        while has_swapped:
            has_swapped = False
            current_node = self.dummy_head
            while current_node.next_node and current_node.next_node.next_node:
                first_node = current_node.next_node
                second_node = current_node.next_node.next_node
                if first_node.value > second_node.value:
                    first_node.next_node = second_node.next_node
                    second_node.next_node = first_node
                    current_node.next_node = second_node
                    
                    if current_node.next_node.next_node is None:
                        self.tail = current_node.next_node

                    has_swapped = True
                current_node = current_node.next_node
    
    def remove_first(self, value) -> None:
        """Removes the first occurrence of a node with the specified value."""
        current_node = self.dummy_head
        while current_node.next_node is not None:
            if current_node.next_node.value == value:
                current_node.next_node = current_node.next_node.next_node
                if current_node.next_node is None:
                    self.tail = current_node
                return
            else:
                current_node = current_node.next_node
    
    def remove_all(self, value) -> None:
        """Removes all nodes with the specified value from the list."""
        current_node = self.dummy_head
        while current_node.next_node is not None:
            if current_node.next_node.value == value:
                current_node.next_node = current_node.next_node.next_node
                if current_node.next_node is None:
                    self.tail = current_node
                    return
            else:
                current_node = current_node.next_node
    
    def reverse(self) -> None:
        """Reverses the list."""
        reversed_list = LinkedList()
        current_node = self.dummy_head.next_node
        while current_node is not None:
            reversed_list.insert_node(current_node.value)
            current_node = current_node.next_node
        self.dummy_head.next_node = reversed_list.dummy_head.next_node
    
    def node_count(self) -> int:
        """Returns the number of nodes in the linked list."""
        count = 0
        current_node = self.dummy_head.next_node
        while current_node is not None:
            count += 1
            current_node = current_node.next_node
        return count

    def includes(self, value) -> bool:
        """Returns True if the linked list contains a node with the given value."""
        current_node = self.dummy_head.next_node
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next_node
        return False
    
    def is_sorted(self) -> bool:
        """Returns True is the list is sorted."""
        if not self.dummy_head.next_node is None:
            current_node = self.dummy_head.next_node
            while current_node.next_node is not None:
                if current_node.value > current_node.next_node.value:
                    return False
                current_node = current_node.next_node
        return True
