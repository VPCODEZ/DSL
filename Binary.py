class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

class BST:
    def __init__(self):
        self.root = None

    # Insert
    def insert(self, root, key):
        if root is None: return Node(key)
        if key < root.key: root.left = self.insert(root.left, key)
        elif key > root.key: root.right = self.insert(root.right, key)
        return root

    # Search
    def search(self, root, key):
        if root is None: return False
        if root.key == key: return True
        return self.search(root.left, key) if key < root.key else self.search(root.right, key)

    # Find min value
    def minValueNode(self, node):
        curr = node
        while curr.left: curr = curr.left
        return curr

    # Delete
    def delete(self, root, key):
        if root is None: return root
        if key < root.key: root.left = self.delete(root.left, key)
        elif key > root.key: root.right = self.delete(root.right, key)
        else:
            if not root.left: return root.right
            elif not root.right: return root.left
            temp = self.minValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        return root

    # Inorder Display
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

# --- Main Menu ---
bst = BST()
while True:
    print("\n1.Insert 2.Delete 3.Search 4.Display 5.Exit")
    ch = input("Choose: ")
    if ch == '1':
        k = int(input("Enter key: "))
        bst.root = bst.insert(bst.root, k)
        print("✅ Inserted")
    elif ch == '2':
        k = int(input("Enter key to delete: "))
        bst.root = bst.delete(bst.root, k)
        print("🗑️ Deleted (if existed)")
    elif ch == '3':
        k = int(input("Enter key to search: "))
        print("🔍 Found" if bst.search(bst.root, k) else "⚠️ Not found")
    elif ch == '4':
        print("🌳 BST (Inorder): ", end="")
        bst.inorder(bst.root)
        print()
    elif ch == '5':
        break
    else:
        print("⚠️ Invalid choice")
