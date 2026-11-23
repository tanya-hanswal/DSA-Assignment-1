class Node:
    def _init_(self, key):
        self.key = key
        self.red = True
        self.left = None
        self.right = None


class RedBlackTree:
    def _init_(self):
        self.root = None

    def is_red(self, node):
        return node is not None and node.red

    def rotate_left(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.red = h.red
        h.red = True
        return x

    def rotate_right(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.red = h.red
        h.red = True
        return x

    def flip(self, h):
        h.red = not h.red
        h.left.red = not h.left.red
        h.right.red = not h.right.red

    def balance(self, h):
        if self.is_red(h.right):
            h = self.rotate_left(h)
        if self.is_red(h.left) and self.is_red(h.left.left):
            h = self.rotate_right(h)
        if self.is_red(h.left) and self.is_red(h.right):
            self.flip(h)
        return h

    def insert(self, key):
        def add(h, key):
            if h is None:
                return Node(key)
            if key < h.key:
                h.left = add(h.left, key)
            elif key > h.key:
                h.right = add(h.right, key)
            else:
                return h
            return self.balance(h)

        self.root = add(self.root, key)
        self.root.red = False

    def search(self, key):
        h = self.root
        while h:
            if key == h.key:
                return True
            h = h.left if key < h.key else h.right
        return False

    def move_left(self, h):
        self.flip(h)
        if self.is_red(h.right.left):
            h.right = self.rotate_right(h.right)
            h = self.rotate_left(h)
            self.flip(h)
        return h

    def move_right(self, h):
        self.flip(h)
        if self.is_red(h.left.left):
            h = self.rotate_right(h)
            self.flip(h)
        return h

    def minimum(self, h):
        while h.left:
            h = h.left
        return h

    def delete_min(self, h):
        if h.left is None:
            return None
        if not self.is_red(h.left) and not self.is_red(h.left.left):
            h = self.move_left(h)
        h.left = self.delete_min(h.left)
        return self.balance(h)

    def delete(self, key):
        def remove(h, key):
            if key < h.key:
                if h.left and not self.is_red(h.left) and not self.is_red(h.left.left):
                    h = self.move_left(h)
                h.left = remove(h.left, key)
            else:
                if self.is_red(h.left):
                    h = self.rotate_right(h)
                if key == h.key and h.right is None:
                    return None
                if h.right and not self.is_red(h.right) and not self.is_red(h.right.left):
                    h = self.move_right(h)
                if key == h.key:
                    x = self.minimum(h.right)
                    h.key = x.key
                    h.right = self.delete_min(h.right)
                else:
                    h.right = remove(h.right, key)
            return self.balance(h)

        if not self.search(key):
            print("Key not found")
            return

        if not self.is_red(self.root.left) and not self.is_red(self.root.right):
            self.root.red = True

        self.root = remove(self.root, key)

        if self.root:
            self.root.red = False

    def inorder(self, h=None):
        if h is None:
            h = self.root
        if h:
            self.inorder(h.left)
            print(h.key, end=" ")
            self.inorder(h.right)

    def printTree(self):
        from collections import deque
        if not self.root:
            print("Tree is empty")
            return
        q = deque([self.root])
        while q:
            h = q.popleft()
            color = "RED" if h.red else "BLACK"
            print(f"{h.key}({color})", end=" ")
            if h.left:
                q.append(h.left)
            if h.right:
                q.append(h.right)
        print()


tree = RedBlackTree()

for x in [10, 20, 30, 15, 25]:
    tree.insert(x)

print("Inorder:")
tree.inorder()

print("\nSearch 20:", tree.search(20))

tree.delete(20)

print("After deletion:")
tree.inorder()

print("\nTree:")
tree.printTree()