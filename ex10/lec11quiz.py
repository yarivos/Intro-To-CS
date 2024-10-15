class TreeNode: 
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right 

def tree_to_what(tree_root):
    result = str()
    if tree_root.left:
        result += tree_to_what(tree_root.right) + " " \
            + tree_to_what(tree_root.left) + " "
    result += tree_root.data
    return result

expr = TreeNode("*", 
                TreeNode("+", TreeNode("4"), TreeNode("6"))
                , TreeNode("2"))

# print(tree_to_what(expr))

records = [("Al", 23), ('Tabitha', 22), ('Bob', 19), ('Alice', 27)]
print(max(records, key = lambda x: x[0][-1]))

