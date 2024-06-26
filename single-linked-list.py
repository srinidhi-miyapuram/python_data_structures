 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # creating single linked list
    def __init__(self):
        self.head = None

    def add_num(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    # function to list the linked list
    def list_num(self):
        new_list = []
        old_head = self.head
        while self.head.next != None:
            new_list.append(self.head.data)
            self.head = self.head.next
        new_list.append(self.head.data)
        self.head = old_head
        return new_list
    
    # function to delete a particular value 
    def delete_num(self,data):
        old_head = self.head
        node_data = self.head
        while self.head.data != data:
            node_data = self.head
            self.head = self.head.next
        if self.head.data == data:
            node_data.next = self.head.next
            self.head = old_head
    
    # function returns the length of the linked list
    def len_linked_list(self):
        old_head = self.head
        count = 1
        while self.head.next != None:
            count += 1
            self.head = self.head.next
        self.head = old_head
        return count

        


if __name__ == "__main__":
    num = int(input("Enter the size :- "))
    my_list = [int(input()) for i in range(num)]
    res = LinkedList()
    for i in my_list:
        result = res.add_num(i)

    # before deletion the linked list
    res_list = res.list_num()
    print(res_list)
    # deleting a particular value
    del_num = res.delete_num(3)

    # post deletion the linked list
    res_list = res.list_num()
    print(res_list)

    list_length = res.len_linked_list()
    print(list_length)
