class El:
    # Element -> .contents for data and .next for next element
    def __init__(self, contents):
        self.contents = contents
        self.next = None


class LinkedList:
    # FirstEl -> First element of the linked list
    def __init__(self):
        self.first_el = None

    # Reverse function
    def reverse(self):
        pre_el = None
        cur_el = self.first_el
        while cur_el is not None:
            next_el = cur_el.next
            cur_el.next = pre_el
            pre_el = cur_el
            cur_el = next_el
        self.first_el = pre_el

    # Push elements to the LinkedList
    def push_el(self, new_contents):
        new_node = El(new_contents)
        new_node.next = self.first_el
        self.first_el = new_node

    # Print the LinkedList
    def print_list(self):
        temp = self.first_el
        while temp:
            print(temp.contents)
            temp = temp.next


# Test
linked_list = LinkedList()
linked_list.push_el(112)
linked_list.push_el(98)
linked_list.push_el(66)

linked_list.print_list()
linked_list.reverse()
print("--------")
linked_list.print_list()
