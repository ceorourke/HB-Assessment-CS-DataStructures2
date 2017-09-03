class Node(object):
    """Node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return '<Node %s>' % self.data


# The Node class is defined above. Below is the stub of the traverse_recursively method, which is inside the Node class.

    def traverse_recursively(self):
        """Traverse a Node's path recursively and print out each node's data."""
        
        if self.next == None:
            print self.data
            return
        print self.data
        self = self.next
        self.traverse_recursively()


data = raw_input().split(' ')
first = node = Node(data[0])
for item in data[1:]:
    node.next = Node(item)
    node = node.next
first.traverse_recursively()