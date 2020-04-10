"""
    Reverse a string in-place
"""
def reverse_string_inplace(s):
    if len(s) == 0 or len(s) == 1:
        pass
    else:
        #s.reverse() # simple  python implementation
        left = 0
        right = len(s) -1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left = left + 1
            right = right - 1
    print s

"""
    Given a linked list, swap every two adjacent nodes and return its head.
    e.g.  for a list 1-> 2 -> 3 -> 4, one should return the head of list as 2 -> 1 -> 4 -> 3.

    1. First, we swap the first two nodes in the list, i.e. head and head.next;
    2. Then, we call the function self as swap(head.next.next) to swap the rest of the list following the first two nodes.
    3. Finally, we attach the returned head of the sub-list in step (2) with the two nodes swapped in step (1) to form a new linked list.
"""
def swap_pairs(self, head):
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
    """
    :type head: ListNode
    :rtype: ListNode
    """
    def swap(head):
        tmp = head.next
        head.next = head.next.next
        tmp.next = head
        head = tmp
        #print "After swap head:", head
        #print "After swap next:", head.next
        return head

    if head is None or head.next is None: # Base case of 0, 1 nodes
        return head
    first_head = swap(head) # 1,2 becomes 2, 1
    curr_head = first_head # curr_head is 2
    while True:
        next_head = curr_head.next.next # 3
        if next_head is not None and next_head.next is not None: # 3, 4
            #print "Next head:", next_head # 3
            curr_head.next.next = swap(next_head) # swap 3,4 to 4,3 return at 2,1
            curr_head = curr_head.next.next
            #print "Curr head:", curr_head
        else:
            break
    return first_head

"""
    Reverse a singly linked list.
    Example:
    Input: 1->2->3->4->5->NULL
    Output: 5->4->3->2->1->NULL
"""
def reverse_linked_list(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head == None:
        return
    # Iterative approach
    curr = head # 1
    prev = None # beginning of list is None
    next = curr.next # 2
    while next is not None:
        curr.next = prev # 1 points to null
        prev = curr # null becomes 1
        curr = next # 2 becomes curr
        next = next.next
    curr.next = prev # for last node, have to assign manually
    return curr
