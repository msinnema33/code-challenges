# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

# Note: Do not modify the linked list.

# https://leetcode.com/problems/linked-list-cycle-ii/ # 142

def detectCycle(self, head: ListNode) -> ListNode:
    visited = set()
    current = head
    while current is not None:
        if hasattr(current, 'visited'):
            return current
        
        current.visited = True
        current = current.next
        
    return None
