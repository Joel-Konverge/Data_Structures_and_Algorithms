class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data)
    def preorder(self):
        print(self.data)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
t=Tree(5)
t.left=Tree(9)
t.right=Tree(7)
t.left.left=Tree(3)
t.left.right=Tree(6)
print("Inorder")
t.inorder()
print("Postorder")
t.postorder()
print("Preorder")
t.preorder()