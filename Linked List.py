class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node
        
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        
    def insertAfter(self, prev_node, new_value):
        new_node = Node(new_value)
        if prev_node is None:
            return "Enter Prev Node"
        temp = prev_node.next
        prev_node.next = new_node
        new_node.next = temp
        
    def swap_Nodes(self,key_1,key_2): # swap using nodes
        
        if key_1 == key_2:
            return
        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next
        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next
        if not curr_1 or not curr_2:
            return
        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2
        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1
        curr_1.next,curr_2.next = curr_2.next,curr_1.next
        
    def swap_nodes_alt(self, key_1, key_2): # swap using data values
        if key_1 == key_2:
            return
        curr  = self.head
        x , y = None , None # Assign None to avoid reference error
        while curr :
            if curr.data == key_1:
                x = curr # key_1 found
            if curr.data == key_2:
                y =curr # key_2 found
            curr = curr.next
        
        if x and y: # Check if both key's exist
            x.data , y.data = y.data , x.data
        else : 
            return
    
    def middleNode(self):
        count = self.countNode()
        curr = self.head
        for i in range((count-1)//2):
            curr = curr.next
        if count % 2 == 0:
            print("\nMiddle Nodes are => ",curr.data, "and ",curr.next.data)
        else:
            print("\nMiddle Node is => ",curr.data)
            
      
    def countNode(self):
        curr = self.head
        length = 0
        while curr is not None:
            length += 1
            curr = curr.next
        return length
        
    def delete_Node(self, key):
        curr_node = self.head
        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return
        prev = None
        while curr_node and curr_node.data !=key:
            prev = curr_node
            curr_node = curr_node.next
        
        if curr_node.next is None:
            return "No key Present"
        prev.next = curr_node.next
        curr_node = None
        
    def delete_node_at_pos(self, pos):
    
        cur_node = self.head

        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        count = 0
        while cur_node and count != pos:
            prev = cur_node 
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return 

        prev.next = cur_node.next
        cur_node = None
        
    def deleteTotalList(self):
        curr_node = self.head
        while curr_node:
            prev = curr_node.next
            del curr_node.data
            curr_node = prev
            
    def reverseList(self):
        prev = None
        curr_node = self.head
        while curr_node:
            nxt = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = nxt 
        self.head = prev
        
    def reverse_recursive(self):
        
        def reverse_recursive_helper(curr,prev):
            if not curr:
                return prev
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            return reverse_recursive_helper(curr,prev)
        self.head = reverse_recursive_helper(curr = self.head , prev = None)
    
    def print(self):
        curr = self.head
        if curr is None:
            return
        else:
            while curr is not None:
               print(curr.data, end=" ")
               curr = curr.next
        print("\n")
        
    def count_occurence(self,key):
        curr = self.head
        count = 0
        while curr:
            if curr.data == key:
                count += 1
            curr = curr.next
        print("Occurence of ",key,"in Linked list is => ",count)
    
    def count_occurence_recursive(self,node,key):
        if not node:
            return 0
        else:
            if node.data == key:
                return 1 + self.count_occurence_recursive(node.next,key)
            else:
                return self.count_occurence_recursive(node.next,key)
            
    def  remove_duplicates(self):
        curr = self.head
        prev = None
        dup_values  = dict()
        while curr:
            if curr.data in dup_values:
                prev.next = curr.next
                curr = None
            else:
                dup_values[curr.data] = 1
                prev = curr
            curr = prev.next
            
    def nth_from_start(self,key):
        curr = self.head
        index = 1
        while curr:
            if index == key:
                return curr.data
            else:
                index += 1
                curr = curr.next
    
    def nth_from_last(self,key):
        length = self.countNode()
        curr = self.head
        while curr:
            if length == key:
                return curr.data
            else:
                length -= 1
                curr = curr.next
    
    def merge_sorted_list(self,llist):
        p = self.head
        q = llist.head
        s = None
        new_head = None
        if not p:
            return q
        if not q:
            return p
        if p and q:
            if p.data >= q.data:
                s = q
                q = s.next
            else:
                s = p
                p = s.next
            new_head = s
        while p and q:
            if p.data >= q.data:
                s.next = q
                s = q
                q = s.next
            else:
                s.next = p
                s = p
                p = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        return new_head

    def add_two_lists(self,llist_2):
        curr_node_1 = self.head
        curr_node_2 = llist_2.head
        sum = 0
        while curr_node_1:
            sum = sum + curr_node_1.data
            curr_node_1 = curr_node_1.next
        while curr_node_2:
            sum = sum + curr_node_2.data
            curr_node_2 = curr_node_2.next
        print("Total Sum => ",sum)

    def check_palindrome(self):
        # Method 1
        curr = self.head
        s = []
        while curr:
            s.append(curr.data)
            curr = curr.next
        print(s)
        curr = self.head
        while curr:
            item = s.pop()
            if curr.data != item:
                print("Not Palindrome")
                break
            else:
                print("Palindrome")
                break
            curr = curr.next
    def check_palindrome_2(self): # only if nodes data are string
        curr = self.head
        s = ""
        while curr:
            s+= curr.data
            curr = curr.next
        print(s)

    def rotate_around_node(self,node):
        p = self.head
        q = self.head
        prev = None
        count = 0
        while p and count < node:
            prev = p
            p = p.next
            q = q.next
            count += 1
        p = prev
        
        while q:
            prev = q
            q = q.next
        q = prev
        
        q.next = self.head
        self.head = p.next
        p.next = None
        
    def move_tail_to_head(self):
        curr = self.head
        prev = None
        while curr.next:
            prev = curr
            curr = curr.next
        curr.next = self.head
        prev.next = None
        self.head = curr


if __name__ == "__main__":
    llist_1 = LinkedList()
    llist_2 = LinkedList()
    llist_1.append(1)
    llist_1.append(2)
    llist_1.append(3)
    llist_1.append(4)
    llist_1.print()
    llist_2.append(2)
    llist_2.append(5)
    llist_2.append(10)
    #llist_2.print()
    #llist_1.add_two_lists(llist_2)
    #llist_1.check_palindrome()
    #llist_1.rotate_around_node(3)
    #llist_1.print()
    llist_1.move_tail_to_head()
    llist_1.print()
