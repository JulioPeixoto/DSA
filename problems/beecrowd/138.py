from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        old_new = {}
        cur = head
        while cur:
            old_new[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            if cur.next:
                old_new[cur].next = old_new[cur.next]
            if cur.random:
                old_new[cur].random = old_new[cur.random]
            cur = cur.next
        return old_new[head]




# ============= TESTES =============

# Teste 1: [[7,null],[13,0],[11,4],[10,2],[1,0]]
n1 = Node(7)
n2 = Node(13)
n3 = Node(11)
n4 = Node(10)
n5 = Node(1)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n1.random = None
n2.random = n1
n3.random = n5
n4.random = n3
n5.random = n1

result = Solution().copyRandomList(n1)
