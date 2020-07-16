# A BFS approach: 

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        q = collections.deque()
        nodeMap = {}
        q.append((root, 0, 0))
        
        while q:
            if x in nodeMap and y in nodeMap:
                break
            node, level, parent = q.popleft()
            nodeMap[node.val] = [level, parent]
            if node.left:
                q.append((node.left, level+1, node.val))
            if node.right:
                q.append((node.right, level+1, node.val))
            
        return (nodeMap[x][0] == nodeMap[y][0]) and (nodeMap[x][1] != nodeMap[y][1])
        
# A DFS approach:
class Solution(object):
    def isCousins(self, root, x, y):
        g = {}
        def dfs(root, i=0, parentVal=None):
            if root == None:
                return
            g[root.val] = (i, parentVal)
            dfs(root.left, i+1, parentVal=root.val)
            dfs(root.right, i+1, parentVal=root.val)
        dfs(root)
        return g[x][0] == g[y][0] and g[x][1] != g[y][1]
