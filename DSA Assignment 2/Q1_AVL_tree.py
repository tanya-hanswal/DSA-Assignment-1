class Node:
    def _init_(self, key):
        self.key = key
        self.left = None
        self.right = None


def check_avl(root, low=float('-inf'),
              high=float('inf')):
    if root is None:
        return 0

    if not low < root.key < high:
        return -1

    l = check_avl(root.left, low, root.key)
    r = check_avl(root.right, root.key, high)

    if l == -1 or r == -1 or abs(l-r) > 1:
        return -1

    return 1 + max(l, r)


root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(15)

if check_avl(root) != -1:
    print("AVL Tree")
else:
    print("Not an AVL Tree")