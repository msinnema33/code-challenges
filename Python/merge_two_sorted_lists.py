# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # input has two head nodes to two linked lists, expected output is the head node of the new merged list
    def mergeTwoLists(self, l1: ListNode, l2: ListNode): # -> ListNode:
        # head_ptr will be the head node of the output list
        # temp_ptr will be used to insert nodes into the output list
        head_ptr = temp_ptr = ListNode()

        # loop through until both lists have reached the end
        while l1 or l2:
            # while l1 has still not reached its end and l2 has either reached its end
            # or l1.val is less than or equal to l2.val
            # then add l1 to the output list as a ListNode
            # increment l1 node to its next
            if l1 and (not l2 or l1.val <= l2.val):
                temp_ptr.next = ListNode(l1.val)
                l1 = l1.next
            # otherwise, add l2 to the ouput list as a ListNode and increment l2 node to its next
            else:
                temp_ptr.next = ListNode(l2.val)
                l2 = l2.next
            # increment the temp_ptr pointer to its next
            temp_ptr = temp_ptr.next

        # return the output list
        return head_ptr.next

## clsss solution:
        # # init a new linked list 
        # new_list = ListNode(None)
        # # variable to keep track of where we are in the new list 
        # current_new = new_list
        # # keep track of the two current nodes, l1 and l2

        # # traverse along both linked lists 
        # while l1 is not None and l2 is not None:
        #     # compare the two values that l1 and l2 are referring to 
        #     # if l1.val == l2.val:
        #         # add both to our new list and increment both pointers 
        #     if l1.val <= l2.val:
        #         # take the smaller one and add it on to the end of a new linked list
        #         current_new.next = ListNode(l1.val)
        #         # update the new_list reference 
        #         l1 = l1.next
        #     else:
        #         current_new.next = ListNode(l2.val)
        #         l2 = l2.next
        #     current_new = current_new.next
                
        # # once all of the nodes from one of the linked lists is added,
        # # add all of the remaining nodes from the other list to the end of
        # # the new linked list 
        # # check l1 to see if it still has nodes 
        # if l1 is not None:
        #     # add the rest of l1 to the end of our new list 
        #     current_new.next = l1
        # # check l2 to see if it still has nodes 
        # if l2 is not None:
        #     current_new.next = l2
            
        # # return our new list - our initial dummy node 
        # return new_list.next