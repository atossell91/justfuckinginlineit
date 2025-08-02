class ListNode:
    def __init__(self, next_node=None, item=None):
        self.next_node = next_node
        self.item = item

class LinkedList:
    def __init__(self):
        self.first_node = None
        self.last_node = None

    def append_item(self, item):
        new_node = ListNode(item=item)

        if self.first_node is None:
            self.first_node = new_node
            self.last_node = new_node
        else:
            self.last_node.next_node = new_node
            self.last_node = new_node

    def find_item(self, predicate):
        list_item = self.first_node
        while list_item is not None:
            if predicate(list.item):
                return list_item
            
            list_item = list_item.next_node

    def find_parent(self, predicate):
        parent = None
        list_item = self.first_node
        while list_item is not None:
            if predicate(list_item.item):
                return parent
            
            parent = list_item
            list_item = list_item.next_node

    def insert_after(self, loc_node, new_item):
        new_node = ListNode(item=new_item)
        new_node.next_node = loc_node.next_node
        loc_node.next_node = new_node

    def scan_list(self):
        node_item = self.first_node
        while node_item is not None:
            yield node_item
            node_item = node_item.next_node
