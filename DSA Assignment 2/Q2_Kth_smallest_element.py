class Node:
    def _init_(self, key):
        self.key = key
        self.left = None
        self.right = None


def kth_smallest(root, k):
    stack = []
    current = root
    count = 0

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        count += 1

        if count == k:
            return current.key

        current = current.right

    return None


root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(15)

print("Kth smallest:", kth_smallest(root, 3))