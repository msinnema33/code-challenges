# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def remove_kth_from_end(head, k):
    if k == 0:
        return head
    length, counter, dummy = 1, 1, head
    while dummy.next:
        length, dummy = length + 1, dummy.next
    dummy = head
    
    if k > length: # finds when k is greater than the length of the list
        return head
        
    if length == k: 
        return head.next
        
    while counter < length - k: # steps through the list to check next values
            counter, dummy = counter + 1, dummy.next
    dummy.next = dummy.next.next
    return head
        
   
# delete a node from the linked list
# find the kth node from end
# if k is longer than the lenght of the LL (do not modify LL)

# This is the two pass solution to find the length of the LL
# This problem can be simply reduced to another one : Remove the (L - n + 1)(L−n+1) th node from the beginning in the list , where LL is the list length. This problem is easy to solve once we found list length LL. Can't do a len(LL)

# First we will add an second "dummy" node, which points to the list head. The "dummy" node is used to simplify some corner cases such as a list with only one node, or removing the head of the list. On the first pass, we find the list length LL. Then we set a pointer to the dummy node and start to move it through the list till it comes to the (L - n)(L−n) th node. We relink next pointer of the (L - n)(L−n) th node to the (L - n + 2)(L−n+2) th node and we are done.

#Complexity Analysis

# Time complexity : O(L)O(L).

# The algorithm makes two traversal of the list, first to calculate list length LL and second to find the (L - n)(L−n) th node. There are 2L-n2L−n operations and time complexity is O(L)O(L).

# Space complexity : O(1)O(1).

# We only used constant extra space.

# One pass solution:  The above algorithm could be optimized to one pass. Instead of one pointer, we could use two pointers. The first pointer advances the list by n+1n+1 steps from the beginning, while the second pointer starts from the beginning of the list. Now, both pointers are exactly separated by nn nodes apart. We maintain this constant gap by advancing both pointers together until the first pointer arrives past the last node. The second pointer will be pointing at the nnth node counting from the last. We relink the next pointer of the node referenced by the second pointer to point to the node's next next node. 

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def removeNthFromEnd(self, head, n):
#         """
#         :type head: ListNode
#         :type n: int
#         :rtype: ListNode
#         """
#         list_ = []
#         while head != None:
#             list_ +=[head.val]
#             head = head.next 
#         del list_[-n]
#         return list_
## A different one pass solution:

# class Solution(object):
#     def removeNthFromEnd(self, head, n):
#         """
#         :type head: ListNode
#         :type n: int
#         :rtype: ListNode
#         """
#         header = head
#         buffer = (n + 1) * [0]
#         i = 0
#         while head:
#             buffer[i] = head
#             head = head.next
#             i += 1
#             i = i%(n + 1)
#         if buffer[i] == 0 :
#             return buffer[0].next
#         else:
#             buffer[i].next = buffer[i].next.next
#             return header