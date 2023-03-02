# You are free to follow the instructions laid under "Implement Your Own LinkedList" 
# as long as you fully understand and can talk through the code that you write:

# there are two classes, one for the node and one for the linked list. 
# the node class sets up the functionality for the node to be able to hold the data, 
# the linked list class sets up the functionality to hold the nodes within the list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        # data refers to whatever the node is holding, next refers to the next node within the list
    def __repr__(self): 
        # from my understanding, repr is to show what is in the node/linked list, hence the return statement
        # in this case, repr shows the data being stored in each Node
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None
        # head refers to the beginning of the list

    def __repr__(self):
        node = self.head
        # the head node = the first node in the list
        nodes = []
        # the creation of the linked list that will store all the nodes
        while node is not None:
            nodes.append(node.data)
            # while loop = if the node contains data, 
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


# I put the Linked List assignments off for so long because, as you may have seen from some of the things
# I've turned in, OOP was hard for me to wrap my head around, and at the time of me doing this assignment,
# it still in many ways is. I know that more was probably expected in this assignment, however I wanted to 
# make sure I didn't put it off for two reasons: one: while we're in flask week I want to make sure I fully
# understand OOP and as much of Python in general as I can, and two: I hate how far behind I am and want to
# make sure I catch up ASAP, in terms of assignments and understanding. In some ways I feel I've fallen behind
# from the rest of the class in understanding, and I'm going to do everything I can to catch up.