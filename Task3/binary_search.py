# Exercise: Binary Search Tree
def create_node(value):
    return {'value': value, 'left': None, 'right': None}

def insert_node(root, value):
    if root is None:
        return create_node(value)
    
    if value < root['value']:
        root['left'] = insert_node(root['left'], value)
    else:
        root['right'] = insert_node(root['right'], value)
    return root

def search_node(root, value):
    if root is None or root['value'] == value:
        return root
    
    if value < root['value']:
        return search_node(root['left'], value)
    else:
        return search_node(root['right'], value)

def min_node(node):
    current = node
    while current['left'] is not None:
        current = current['left']
    return current

def delete_node(root, value):
    if root is None:
        return root
    
    if value < root['value']:
        root['left'] = delete_node(root['left'], value)
    elif value > root['value']:
        root['right'] = delete_node(root['right'], value)
    else:
        if root['left'] is None:
            return root['right']
        elif root['right'] is None:
            return root['left']
        
        temp = min_node(root['right'])
        root['value'] = temp['value']
        root['right'] = delete_node(root['right'], temp['value'])
    return root

# Inorder traversal of the BST
def inorder_traversal(root, elements):
    if root is not None:
        inorder_traversal(root['left'], elements)
        elements.append(root['value'])
        inorder_traversal(root['right'], elements)
bst_root = None
values_to_insert = [1, 3, 5, 7, 4, 6, 9]
for value in values_to_insert:
    bst_root = insert_node(bst_root, value)

inorder_elements = []
inorder_traversal(bst_root, inorder_elements)
print("Inorder Traversal After Insertion:", inorder_elements)

# Search for values in the BST
print("Search for 5:", search_node(bst_root, 5) is not None)
print("Search for 2:", search_node(bst_root, 2) is not None)

# Delete values from the BST
bst_root = delete_node(bst_root, 3)
inorder_elements = []
inorder_traversal(bst_root, inorder_elements)
print("Inorder Traversal After Deleting 3:", inorder_elements)

bst_root = delete_node(bst_root, 5)
inorder_elements = []
inorder_traversal(bst_root, inorder_elements)
print("Inorder traversal after deleting 5:", inorder_elements)
