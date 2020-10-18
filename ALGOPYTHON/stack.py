class _Node(object):  # helper linked list class
    """Node object. Nodes are stored in a Stack."""

    def __init__(self, item, _Node):
        self.Item = item  # Type String Item
        self.Next = _Node  # Type Node<Item>


if __name__ == "__main__":
    node = _Node()
