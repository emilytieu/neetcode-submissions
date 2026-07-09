# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        encode = ""
        
        def dfs(node):
            nonlocal encode
            if not node:
                encode += "N,"
                return
            
            encode += str(node.val) + ","
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return encode

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        index = 0

        def dfs():
            nonlocal index
            if vals[index] == "N":
                index += 1
                return None

            node = TreeNode(int(vals[index]))
            index += 1
            
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()

