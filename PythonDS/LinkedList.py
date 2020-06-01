class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.start_node = None

    def traversing_list(self):
        if self.start_node is None:
            print("List is empty")
        n = self.start_node
        while n is not None:
            print(n.item, " ")
            n = n.ref

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node

    def inser_at_end(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        new_node = Node(data)
        n.ref = new_node

    def inser_after_item(self, x, data):
        n = self.start_node
        while n is not None:
            if n.item == x:
                break
            n = n.ref
        if n is None:
            print("x not in list")

        new_node = Node(data)
        new_node.ref = n.ref
        n.ref = new_node

    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
        if x == self.start_node.item:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
            return
        n = self.start_node
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
            return
        i = 1
        n = self.start_node
        while i < index - 1 and n is not None:
            n = n.ref
            i += 1
        if n is None:
            print("index out of bound")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def count(self):
        if self.start_node is None:
            return 0
        n = self.start_node
        count = 0
        while n is not None:
            count += 1
            n = n.ref

        return count

    def search_with_index(self, x):
        if x == self.start_node.item:
            print("item at index 1")
            return
        n = self.start_node
        count = 0
        while n is not None:
            count += 1
            if n.item == x:
                print(x, "is at ", count)
                return
            n = n.ref
        if n is None:
            print("item not found")
            return

    def delete_from_begning(self):
        if self.start_node is None:
            print("The list is empty")
            return
        self.start_node = self.start_node.ref

    def delete_from_end(self):
        if self.start_node is None:
            print("list has no item to delete")
            return
        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None

    def delete_by_value(self, x):
        if self.start_node is None:
            print("List is empty")
            return
        if heself.start_node.ref.item == x:
            self.start_node.ref = None
            return
        n = self.start_node
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("item not in list")
        else:
            n.ref = n.ref.ref

    def delete_by_index(self, index):
        if index == 1:
            self.start_node = self.start_node.ref
            return
        i = 1
        n = self.start_node
        while i < index - 1 and n is not None:
            n = n.ref
            i = i + 1
        if n is None:
            print("index out of bound")
        else:
            n.ref = n.ref.ref

    def reverse_linkedlist(self):
        prev = None
        n = self.start_node
        while n is not None:
            next = n.ref
            n.ref = prev
            prev = n
            n = next
        prev = self.start_node

    def bubble_sort_exchanging_data(self):
        end = None
        while end != self.start_node:
            p = self.start_node
            while p.ref != end:
                q = p.ref
                if p.item > q.item:
                    p.item, q.item = q.item, p.item
                p = p.ref
            end = p
