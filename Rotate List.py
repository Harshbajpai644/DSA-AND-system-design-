class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        last_node = head
        length = 1
        while last_node.next:
            last_node = last_node.next
            length += 1
        
        k = k % length
        if k == 0:
            return head
        
        last_node.next = head
        
        new_tail_steps = length - k - 1
        new_tail = head
        for _ in range(new_tail_steps):
            new_tail = new_tail.next
            
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
