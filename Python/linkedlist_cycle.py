def hasCycle(self, head):
## Solution #2
    # visited = set()
    # if head.next is None:
    #     return False
    # while head.next is not None:
    #     visited.add(head)
    #     if head.next in visited:
    #         return True
    #     self.hasCycle(head.next)
## solution #1
    fast = head
    slow = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

        if fast is slow:
            return True

    return False

## solution #3
#         current = head 
        
#         while current is not None:
#             # check if the current node has the `visited` property
#             if hasattr(current, 'visited'):
#                 return True
            
#             current.visited = True
#             current = current.next 
#             # if we ever encounter a node with the 'visited', then
#             # we've been there before 
#             # or alternatively, set the `value` to None 
        
#         # we reached the end of the linked list 
#         return False
