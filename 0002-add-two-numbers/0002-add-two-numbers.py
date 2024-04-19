# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        def print_ListNode(x: ListNode):
            while True:
                print(x.val, end="")
                if x.next is None:
                    break
                x = x.next
            print()

        print_ListNode(l1)
        print_ListNode(l2)

        sum = 0
        carry = 0
        result = result_org = ListNode()

        while True:

            result.val = l1.val + l2.val + carry
            carry = 0
            if result.val > 9:
                result.val -= 10
                carry = 1

            print(result.val, carry)
            if l1.next is None or l2.next is None:
                break
            l1, l2 = l1.next, l2.next
            result.next = ListNode()
            result = result.next

        if l1.next is None and l2.next is None:
            pass
        else:
            result.next = ListNode()
            result = result.next
            if l1.next is None:
                l2 = l2.next
                while True:
                    result.val = l2.val + carry
                    carry = 0
                    if result.val > 9:
                        result.val -= 10
                        carry = 1
                    print(result.val, carry)
                    if l2.next is None:
                        break
                    l2 = l2.next
                    result.next = ListNode()
                    result = result.next
            else:
                l1 = l1.next
                while True:
                    result.val = l1.val + carry
                    carry = 0
                    if result.val > 9:
                        result.val -= 10
                        carry = 1
                    print(result.val, carry)
                    if l1.next is None:
                        break
                    l1 = l1.next
                    result.next = ListNode()
                    result = result.next

        if carry == 1:
            result.next = ListNode(1)

        print_ListNode(result_org)
        return result_org
