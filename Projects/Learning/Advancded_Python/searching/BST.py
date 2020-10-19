class Node:
    
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
#implement getter for left child
    def get_left_child(self):
        return self.left
#implement setter for left child
    def set_left_child(self, left):
        self.left = left
#implement getter for right child
    def get_right_child(self):
        return self.right
#implement setter for right child
    def set_right_child(self, right):
        self.right = right
#implement getter for data
    def get_value(self):
        return self.data
#implement setter for data
    def set_value(self):
        self.data = Value
#print tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
            
        print(self.data)
        
        if self.right:
            self.right.print_tree()
            
def insert(head, node):
    
    if head == None:
        return node
    
    if node.get_value() <= head.get_value():
        head.set_left_child(insert(head.get_left_child(), node))
    else:
        head.set_right_child(insert(head.get_right_child(), node))
        
    return head

def lookup(head, data):

    if head == None:
        return print("Value not found!")
    
    if head.get_value() == data:
        return head
    
    if data <= head.get_value():
        return lookup(head.get_left_child(), data)
    else:
        return lookup(head.get_right_child(), data)
    
def print_node(node):
    if (node == None):
        print("not found!")
        
    print(node.get_value())
    
def min_value(head):
    current = head
    
    while(current.left != None):
        current = current.left
        
    return current.data

def max_value(head):
    current = head
    
    while(current.right != None):
        current = current.right
        
    return current.data

A = Node(45)
B = Node(2)
C = Node(33)
D = Node(54)
E = Node(25)
F = Node(68)
G = Node(72)
H = Node(81)
I = Node(23)

head = insert(None, E)

print(head.print_tree())

insert(head, I)
insert(head, A)
insert(head, B)
insert(head, C)
insert(head, D)
insert(head, G)
insert(head, F)
insert(head, H)


print(head.print_tree())

print_node(lookup(head,68))

print(min_value(head))

insert(head, Node(1))

print(min_value(head))

print(max_value(head))
