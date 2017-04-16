# class implementing linked list data structure


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList(object):
    def __init__(self, head=None):
        if head is not None:
            self._head = Node(head)
        else:
            self._head = Node(None)

    def append(self, value):
        temp = self._head
        while temp.next is not None:
            temp = temp.next
        temp.next = Node(value)

    def prepend(self, value):
        node = Node(value)
        node.next = self._head.next
        self._head.next = node

    def pretty_print(self):
        temp = self._head.next
        while temp is not None:
            print(str(temp.value) + "->")
            print("\b")
            temp = temp.next

    def delete(self, node):
        temp = self._head.next
        while temp.next != node:
            temp = temp.next
        temp.next = node.next
        del node
