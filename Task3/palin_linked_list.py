List = [1, 2, 3, 4, 3, 2]
if not List:
    head = None
else:
    head = {'value': List[0], 'next': None}
    current = head
    for value in List[1:]:
        current['next'] = {'value': value, 'next': None}
        current = current['next']

current = head
print("Linked list:")
while current:
    print(current['value'], end=" -> " if current['next'] else "\n")
    current = current['next']

slow = head
fast = head
while fast and fast['next']:
    slow = slow['next']
    fast = fast['next']['next']

prev = None
while slow:
    temp = slow['next']
    slow['next'] = prev
    prev = slow
    slow = temp

left = head
right = prev
is_palindrome = True
while right:
    if left['value'] != right['value']:
        is_palindrome = False
        break
    left = left['next']
    right = right['next']

if is_palindrome:
    print("The linked list is a palindrome.")
else:
    print("The linked list is not a palindrome.")
