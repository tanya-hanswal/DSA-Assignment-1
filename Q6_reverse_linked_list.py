class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    previous = None
    current = head

    while current:
        nextNode = current.next
        current.next = previous
        previous = current
        current = nextNode

    return previous


# Create a linked list: 1 -> 2 -> 3 -> None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

# Reverse the linked list
result = reverseList(head)

# Print the reversed linked list
while result:
    print(result.val, end=" -> ")
    result = result.next

print("None")
print("program finished")