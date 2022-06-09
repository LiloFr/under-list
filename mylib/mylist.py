from mylib.item import Item


class MyList:
    def __init__(self):
        self.head = None
    
    def insert(self, value, index):
        i = 0
        node = self.head
        previous_node = self.head

        while i < index:
            previous_node = node
            node = Item.next_node
            i += 1

        previous_node.Item.next_node 