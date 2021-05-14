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
        
    
    def print(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next


if __name__ == "__main__":
    llist = LinkedList()
    llist.push("Ram")
    llist.push("Mohan")
    llist.push("Vikash")
    llist.append("Sam")
    llist.append("Paul")
    llist.insertAfter(llist.head.next, "Samuel")
    llist.print()
    llist.middleNode()
