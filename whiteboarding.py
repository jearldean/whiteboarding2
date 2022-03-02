class Node():
    def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

class LinkedList():
    def __init__(self):
      self.head = None
      self.tail = None

    def print_node(self):
      current = self.head

      while current:
        print(current.data)
        current = current.next

      return None
        
    def print_odd_nodes(self):
        current = self.head

        counter = 0
        
        while current:
            if counter % 2 != 0:
                # print(counter)
                print(current.data)
            current = current.next
            counter += 1
                
        return None

    def append(self, node):
        if self.head is None:
          self.head = node
          self.tail = node
        else:
          self.tail.next = node
          self.tail = node

    def remove(self, node):

        if node == self.head:
            self.head = node.next
            after_neighbor = node.next
            after_neighbor.prev = None

        elif node != self.tail:
            before_neighbor = node.prev # a
            after_neighbor = node.next # c

            before_neighbor.next = after_neighbor
            after_neighbor.prev = before_neighbor

        else:  # Node is tail.
            self.tail = node.prev
            before_neighbor = node.prev
            before_neighbor.next = None

"""
   def add_node(self, data):
        "Add node with data to end of list."

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node
"""

#Solution
# def remove(self, node):
#     if node.prev is None:
#         # If node.prev is None, it means this node is the head of
#         # the list. To remove it, just reassign self.head to the next
#         # node
#         self.head = node.next
#     else:
#         node.prev.next = node.next

#     if node.next is None:
#         # If node.next is None, it means this node is the tail of
#         # the list. To remove it, reassign self.tail to the previous
#         # node
#         self.tail = node.prev
#     else:
#         node.next.prev = node.prev
#Testing linked list
llist = LinkedList()
a = Node('apple')
b = Node('berry')
c = Node('cherry')
d = Node('durian')
llist.head = a
a.next = b
b.prev = a
b.next = c
c.prev = b
c.next = d
d.prev = c
llist.tail = d

print('original list')
llist.print_node()
# llist.remove(b)
# print('after removal of b')
# llist.print_node()
# llist.remove(d)
# print('after removal of d')
# llist.print_node()
print('after removal of a')
llist.remove(a)
llist.print_node()
