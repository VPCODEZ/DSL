class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class ExpressionTree:
    def __init__(self):
        self.root = None

    # Build tree from prefix expression
    def build(self, expr):
        stack = []
        for ch in reversed(expr):
            node = Node(ch)
            if ch in "+-*/":
                node.left = stack.pop()
                node.right = stack.pop()
            stack.append(node)
        self.root = stack[-1]

    # Non-recursive postorder traversal
    def postorder(self):
        if not self.root: return
        stack1, stack2 = [self.root], []
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left: stack1.append(node.left)
            if node.right: stack1.append(node.right)
        print("Postorder:", end=" ")
        while stack2:
            print(stack2.pop().val, end=" ")
        print()

    # Delete entire tree
    def delete(self):
        def del_nodes(node):
            if node:
                del_nodes(node.left)
                del_nodes(node.right)
                del node
        del_nodes(self.root)
        self.root = None
        print("🗑️ Expression Tree Deleted")

# --- Main ---
exp = input("Enter Prefix Expression: ")
tree = ExpressionTree()
tree.build(exp)
tree.postorder()
tree.delete()
