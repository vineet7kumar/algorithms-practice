import linkedlist as ll

lst = ll.SinglyLinkedList(0)
lst.append(0)
for i in range(10):
    lst.prepend(i)

lst.pretty_print()
