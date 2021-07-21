class Node:
    def __init__(self,data):
        self.key = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.index = 0
    
    def insert_1(self,data):
        if not data:
            return
        if not self.root:
            self.root = Node(data)
        curr = self.root
        while True:
            if curr.key> data:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = Node(data)
            elif curr.key< data:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = Node(data)
            else:
                break
    def insert_2(self,data):
        if not self.root:
            self.root = Node(data)
        return self.insert_2_helper(self.root,data)
    
    def insert_2_helper(self,node,data):
        if  node.key > data:
            if not node.left:
                node.left = Node(data)
            else:
                return self.insert_2_helper(node.left,data)
        elif node.key < data:
            if not node.right:
                node.right = Node(data)
            else:
                return self.insert_2_helper(node.right,data)
    
    def delete(self,root,key):
        if not root:
            return
        if self.root.key == key:
            if not root.left and not root.right:
                return 
            elif not root.left and root.right:
                return root.right
            elif root.left and not root.right:
                return root.right
            else:
                pnt = root.right
                while pnt.left:
                    pnt = pnt.left
                root.key = pnt.key
                root.right = self.delete(root.right,key)
            
        elif root.key > key:
            root.left = self.delete(root.left,key)
        elif root.key < key:
            root.right = self.delete(root.right,key)
            
    def search(self,root,key):
        if not root:
            return False
        if root.data == key:
            return True
        left = self.search(root.left,key)
        if left:
            return True
        right = self.search(root.right,key)
        if right:
            return True
    # Construct BST from given preorder traversal | Set 1   
    def bst_from_preorder(self,arr,n):  ##### O(n),O(n)
        if not arr:
            return 
        root = Node(arr[0])
        s = []
        s.append(root)
        for i in range(1,n):
            if arr[i] < s[-1].key:
                s[-1].left = Node(arr[i])
                s.append(s[-1].left)
            else:
                while s and arr[i] > s[-1].key:
                    popped = s.pop()
                popped.right = Node(arr[i])
                s.append(popped.right)
        return root
    # Construct BST from given preorder traversal | Set 2
    def bst_from_pre(self,pre):
        size = len(pre)
        min = float('-inf')
        max = float('inf')
        return self.tree_from_pre(pre,size,pre[0],min,max)
    
    def tree_from_pre(self,pre,size,key,min,max):
        if self.index > size:
            return None
        root = None
        if key > min and key<max:
            root = Node(key)
            self.index+=1
            if self.index < size:
                root.left = self.tree_from_pre(pre,size,pre[self.index],min,key)
                root.right = self.tree_from_pre(pre,size,pre[self.index],key,max)
        return root
    
    def preorder(self,node):
        if not node:
            return
        print (node.key,end=" ")
        self.preorder(node.left)
        self.preorder(node.right)
    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.key,end=" ")
            self.inorder(root.right)
    # Sorted Array to Balanced BST
    def sorted_array_to_balanced_bst(self,arr):
        if not arr:
            return None
        mid = len(arr)//2
        root = Node(arr[mid])
        root.left = self.sorted_array_to_balanced_bst(arr[:mid])
        root.right = self.sorted_array_to_balanced_bst(arr[mid+1:])
        return root
    # Transform a BST to greater sum tree
    def greater_sum_bst(self,root): # O(n)
        def search(root,sum):
            if not root:
                return sum
            sum = search(root.right,sum)
            sum+= root.key
            root.key = sum-root.key
            sum = search(root.left,sum)
            return sum
        search(root,0)
        return root
    
    # Construct all possible BSTs for keys 1 to N
    
    # Construct BST from its given level order traversal
    def constructBSTfromLevelOrder(self,arr,n):
        if not arr:
            return
        root = None
        for i in range(0,n):
            root = self.level_order(root,arr[i])
        return root
    
    def level_order(self,root,data):
        if not root:
            root = Node(data)
            return root
        if data < root.key:
            root.left = self.level_order(root.left,data)
        if data > root.key:
            root.right = self.level_order(root.right,data)
        return root
        
    #Merge two BSTs with limited extra space
    
    
    
    #Check if the given array can represent Level Order Traversal of Binary Search Tree
    # def check_level_order(self,arr,n):
    #     if not arr:
    #         return True
    #     min = float('-inf')
    #     max = float('inf')
    #     q = []
    #     i = 0
    #     root = Node(arr[0])
    #     q.append(root)
    #     i += 1
    #     while i<n and len(q)!=0:
    #         temp = q.pop(0)
    #         if i < n and temp.key < arr[i] and  arr[i] > min:
    #             new_node = Node(arr[i])
    
    def check_two_bst(self,arr1,arr2):
        if len(arr1) != len(arr2):
            return False
        for i in range(1,len(arr1)-1,3):
            if arr1[i-1] != arr2[i-1] or arr1[i+1] != arr2[i+1] != arr1[i] == arr2[i]:
                return False
        return True
            
        
        
        
        
if __name__ == "__main__":
    b = BST()
    a = [8, 3, 6, 1, 4, 7, 10, 14, 13]
    c = [8, 10, 14, 3, 6, 4, 1, 7, 13]
    print(b.check_two_bst(a,c))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
            
            
            
            
            
            
