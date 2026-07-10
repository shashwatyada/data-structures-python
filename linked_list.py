# Create a blueprint for a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# STEP 2: CREATE THE LINKED LIST MANAGER
class LinkedList:
    def __init__(self):
        # The list starts completely empty, so head points to None
        self.head = None  

    def insert_at_beginning(self, data):
        # Create a brand new independent node block
        new_node = Node(data)
        # Link the new node to the current head (which could be None if the list is empty)
        new_node.next = self.head
        # Update the head to point to this new node 
        self.head = new_node 
            
    # Method to add a node at the very end of our chain
    def insert_at_end(self, data):
        # Create a brand new independent node block
        new_node = Node(data)  
        
        # Condition A: If the list is empty, make this new node the first item (head)
        if self.head is None:
            self.head = new_node
            return
        
        # Condition B: If the list already has nodes, traverse to the end
        current = self.head
        while current.next is not None:
            current = current.next  # Shift our pointer forward one by one
            
        # Once we reach the last node, connect its 'next' to our new node
        current.next = new_node

    def delete_node(self, key):
        current = self.head

        # Case 1: If the list is empty
        if current is None:
            print("The list is empty. Cannot delete.")
            return
        
        # Case 2: If the node to be deleted is the head
        if current.data == key:
            self.head = current.next # shift head to the next node
            current = None # Optional: clear the current node
            return
        # Case 3: Search for the value while keeping track of the previous node
        prev = None
        while current is not None and current.data != key:
            prev = current
            current = current.next

        # If the value wasn't found in the entire list
        if current is None:
            print(f"Value {key} not found in the list.")
            return

        # Unlink the target node from the linked list
        prev.next = current.next
        current = None

    # Method to travel through the list and print every item
    def display(self):
        if self.head is None:
            print("The list is currently empty.")
            return
        
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next  # Move pointer to the next block
        print("None")  # This shows the end of the chain

    # Method to reverse the linked list in place
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next # Store the next node
            current.next = prev     # Reverse the link
            prev = current         # Move prev and current one step forward
            current = next_node

        self.head = prev # Update head to the new first node


# ==========================================
# STEP 3: RUN AND TEST OUR CODE
# ==========================================
if __name__ == "__main__":
    # Create an empty instance of our Linked List
    my_list = LinkedList()

    # Insert items sequentially
    my_list.insert_at_end(10)
    my_list.insert_at_end(20)
    my_list.insert_at_end(30)

    # Print the final list structure
    print("Printing my first Singly Linked List:")
    my_list.display()

    # Insert an item at the beginning
    my_list.insert_at_beginning(5)
    print("After inserting 5 at the beginning:")
    my_list.display()

    # Delete a node from the middle
    my_list.delete_node(20)

    print("\nList after deleting 20:")
    my_list.display()

    my_list.reverse()
    print("\nList after reversing:")
    my_list.display()