# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Initial simple solution
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1_multiplier = 1
        l1_value = 0
        while (l1):
            l1_value += l1.val*l1_multiplier
            l1 = l1.next
            l1_multiplier *= 10
        l2_multiplier = 1
        l2_value = 0
        while (l2):
            l2_value += l2.val*l2_multiplier
            l2 = l2.next
            l2_multiplier *= 10
        sum = l1_value+l2_value
        top = None
        current = ListNode()
        if sum == 0:
            return ListNode()
        while (sum > 0):
            print(sum%10)
            if (top == None):
                top = ListNode(sum%10)
                current = top
            else:  
                l = ListNode(sum%10)
                current.next = l
                current = l
            sum /= 10
        return top
 
 # Second Solution (O(max(m,n)), also in place)

def add_one(l1):
        current = l1
        while current.val == 9:
            current.val = 0
            if (current.next == None):
                current.next = ListNode(1)
                return
            current = current.next
        current.val += 1
            
class Solution(object):
                    
    def addTwoNumbers(self, l1, l2):
        curr1 = l1
        curr2 = l2
        while (curr1 and curr2):
            value = curr1.val + curr2.val
            if value >= 10:
                if curr1.next == None:
                    curr1.next = ListNode(1)
                else:
                    add_one(curr1.next)
            curr1.val = value % 10
            if curr1.next == None and curr2.next != None:
                curr1.next = curr2.next
                return l1
            if curr1.next != None and curr2.next == None:
                return l1
            
            curr1 = curr1.next
            curr2 = curr2.next
        return l1
        
# Another Solution that not in place, but a lot cleaner

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        result_tail = result
        carry = 0
                
        while l1 or l2 or carry:            
            val1  = (l1.val if l1 else 0)
            val2  = (l2.val if l2 else 0)
            carry, out = divmod(val1+val2 + carry, 10)    
                      
            result_tail.next = ListNode(out)
            result_tail = result_tail.next                      
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
               
        return result.next
 
        
        
