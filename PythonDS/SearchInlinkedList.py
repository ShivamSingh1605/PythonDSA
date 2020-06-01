class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.start_node = None

    def traverse_list(self):
        if self.start_node is None:
            print("List is empty")
            return
        n = self.start_node
        while n is not None:
            print(n.item, " ")
            n = n.ref

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node

    def insert_after_item(self, x, data):
        n = self.start_node
        while n is not None:
            if n.item == x:
                break
            n = n.ref
        if n is None:
            print("item not in list")
        new_node = Node(data)
        new_node.ref = n.ref
        n.ref = new_node

    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return

        if self.start_node.item == x:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
            return

        n = self.start_node
        print(n.ref)
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("x not in list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_at_index(self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
        i = 1
        n = self.start_node
        while i < index - 1 and n is not None:
            n = n.ref
            i = i + 1
        if n is None:
            print("Index out of range")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def get_count(self):
        if self.start_node is None:
            return 0
        count = 0
        n = self.start_node
        while n is not None:
            count += 1
            n = n.ref
        return count

    def get_count_rec(self, n=self.start_node):
        n = self.start_node
        if n is None:
            return 0
        else:
            return (1 + get_count_rec(self, n.ref))

    def search_element(self, x):
        if self.start_node is None:
            return ("list is empty")
        n = self.start_node
        count = 0
        while n is not None:
            count += 1
            if n.item == x:
                return count

            n = n.ref

        if n is None:
            return ("item not in LinkedList")


new_LinkedList = LinkedList()
new_LinkedList.insert_at_end(6)
new_LinkedList.insert_at_end(9)
new_LinkedList.insert_at_end(20)

new_LinkedList.insert_at_start(35)
new_LinkedList.insert_at_index(5, 67)

new_LinkedList.insert_before_item(9, 56)
y = new_LinkedList.get_count_rec()
print(y)
new_LinkedList.traverse_list()
