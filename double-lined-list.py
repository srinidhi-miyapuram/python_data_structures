
# Need to check the code and complete

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_item(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def list_items(self):
        old_head = self.head
        new_list = []
        while self.head.next != None:
            new_list.append(self.head.data)
            self.head = self.head.next
        new_list.append(self.head.data)
        self.head = old_head
        return new_list
    
    def del_item(self, data):
        old_head = self.head
        new_head = self.head
        res = False
        if self.head.data == data:
            
            new_head.next = self.head.next
            self.head = self.head.next
            self.head.prev = new_head
        while self.head.data != data:
            new_head = self.head
            self.head = self.head.next
            res = True
            print(self.head.data, " head")
        # if self.head.data == data:
            
        #     new_head.next = self.head.next
        #     self.head = self.head.next
        #     self.head.prev = new_head
        
        if res == False:
            data_head = self.head
            self.head = self.head.next
            self.head.prev = None
            self.head = self.head.pre
            
        self.head = old_head
    

if __name__ == "__main__":
    num = int(input("Enter the size :- "))
    my_list = [int(input()) for i in range(num)]
    res = LinkedList()
    for i in my_list:
        result = res.add_item(i)
    
    # before deletion the linked list
    res_list = res.list_items()
    print(res_list)

    # deleting a particular value
    del_num = res.del_item(3)

    # post deletion the linked list
    res_list = res.list_items()
    print(res_list)
            