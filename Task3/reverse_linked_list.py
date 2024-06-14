# Exercise: Reversed Linked List
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_link_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def print_link_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

values = input("Enter the values for the linked list (comma-separated integers): ").split(',')
head = ListNode(int(values[0]))
current = head
for value in values[1:]:
    current.next = ListNode(int(value))
    current = current.next

print("Original linked list:")
print_link_list(head)
head = reverse_link_list(head)
print("Reversed linked list:")
print_link_list(head)
