"""
Author: MeetRajput00 (Meet Rajput)

Template for the linked list data structure. Linked Lists works like
array except they follow non-contagious memory allocation.
The benefit of this over a regular array or list is that elements 
can be easily inserted and removed without the need of changing the
index of all other items and the memory used to store the linked list 
does not need to be reorganised because the data does not have to 
be stored contiguously. However, we can’t access items in constant
time (O(1)) as we could in an array as looking up an item in
the list has a linear time complexity (O(n)).

insert(x)
adds element x to the end of the list.

find(x)
returns the position of x.

remove(x)
removes the first occurence of x from the list.

get_count()
returns the number of elements in the list.

is_empty()
checks if the list is empty.

"""
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
    def get_data(self):
        return self.val
    def set_data(self, val):
        self.val = val
 
    def get_next(self):
        return self.next
 
    def set_next(self, next):
        self.next = next

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head
        self.count = 0
    def insert(self, data):
        """
        Create a new node at the Head of the Linked List
        This has a time complexity of O(1) as we are simply changing
        the current head of the Linked List and no indices have to   
        change
        """ 
        #create a new node to hold the data
        new_node = Node(data)
        
        #set the next of the new node to the current head
        new_node.set_next(self.head)
        #set the head of the Linked List to the new head
        self.head = new_node
        #add 1 to the count
        self.count += 1
    def find(self, val):
        """
        Search for item in Linked List with data = val
        
        Time complexity is O(n) as in worst case scenario
        have to iterate over whole Linked List
        """
        #start with the first item in the Linked List
        item = self.head
        #then iterate over the next nodes
        #but if item = None then end search
        while item != None:
           
           #if the data in item matched val
           #then return item
           if item.get_data() == val:
               return item
           
           #otherwise we get the next item in the list
           else:
                item = item.get_next()
        #if while loop breaks with None then nothing found
        #so we return None
        return None
    def remove(self, item):
        """
        Remove Node with value equal to item
        Time complexity is O(n) as in the worst case we have to 
        iterate over the whole linked list
        """
        #set the current node starting with the head
        current = self.head
        #create a previous node to hold the one before
        #the node we want to remove
        previous = None
        #while current is note None then we can search for it
        while current is not None:
            #if current equals to item then we can break
            if current.data == item:
                break
            #otherwise we set previous to current and 
            #current to the next item in list
            previous = current
            current = current.get_next()
        #if the current is None then item, not in the list
        if current is None:
            raise ValueError(f"{item} is not in the list")
        #if previous None then the item is at the head
        if previous is None:
            self.head = current.next
            self.count -= 1
        #otherwise then we remove that node from the list
        else:
             previous.set_next(current.get_next())
             self.count -= 1
    def get_count(self):
        """
        Return the length of the Linked List
        Time complexity O(1) as only returning a single value
        """
        return self.count
    def is_empty(self):
        """
        Returns whether the Linked List is empty or not
        Time complexity O(1) as only returns True or False
        """
        #we only have to check the head if is None or not
        return self.head == None