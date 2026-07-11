# 1 Node Class
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

# 2 Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None 

    # Helper method to insert elements at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
    
    # Helper method to display the linked list structure
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None") 

    # Detect Cycle 
    def has_cycle(self):
        slow = self.head
        fast = self.head 
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


# 3 Run and Test Our Code
if __name__ == "__main__":
    my_list = LinkedList()

    # insert item 
    my_list.insert_at_end(10)
    my_list.insert_at_end(20)
    my_list.insert_at_end(30)
    my_list.insert_at_end(40)
    my_list.insert_at_end(50)

    print("Original List : ")
    my_list.display()

    # Test Cycle Detection (By default, no cycle)
    print("\n--- Testing Cycle Detection ---")
    print(f"Does the list have a cycle? {my_list.has_cycle()}")

    # # Let's forcefully create a cycle for testing: 50 -> 30    
    # # Connect last node (50) to third node (30)
    # node1 = my_list.head
    # node3 = my_list.head.next.next
    # node5 = my_list.head.next.next.next.next
    # node5.next = node3  # Creating a loop manually

    # print("After manually creating a loop/cycle:")
    # print(f"Does the list have a cycle now? {my_list.has_cycle()}")
