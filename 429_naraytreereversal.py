# A super clean one:
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        q, ret = [root], []
        while any(q):
            ret.append([node.val for node in q])
            q = [child for node in q for child in node.children if child]
        return ret

# A more standard one:
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue, ret = [root], []
        while queue:
            temp = []
            newqueue = []
            for i in queue:
                temp.append(i.val)
                for j in i.children:
                    if j:   
                        newqueue.append(j)
            ret.append(temp)
            queue = newqueue
        return ret
            
