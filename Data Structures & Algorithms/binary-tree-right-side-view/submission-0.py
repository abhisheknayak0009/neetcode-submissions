# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        res = []
        if not root:
            return res
        else:
            q.append(root)
        
        while q:
            val = []
            qLen = len(q)
            c = 1
            for i in range(qLen):
                node = q.popleft()
                if c == qLen:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                c += 1
        return res