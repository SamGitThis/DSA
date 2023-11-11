class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self, data):
        node = Node(data, None)
        if self.head == None:
            self.head = node
            return
        
        itr = self.head 
    
        while(itr.next):
            itr = itr.next 
            
        itr.next = node 
        
    def insert(self, llist):
        for i in llist:
            self.insert_at_end(i)
            
    def get_length(self):
        itr= self.head 
        count = 0
        
        while(itr):
            count = count + 1
            itr = itr.next 
            
        return count
            
    def insert_at(self, index, data):
        length = self.get_length()
        
        if(index > length or index < 0):
            print("Index out of range.")
        
        elif(index == 0):
            self.insert_at_begining(data)
            
        elif(index == length):
            self.insert_at_end(data)
            
        else:
            itr = self.head 
            count = 0
            while(itr):
                if index - 1 == count:
                    node = Node(data, itr.next)
                    itr.next = node
                    break
                else:
                    itr = itr.next 
                    count = count + 1
        
    def remove_at(self, index):
        count = 0
        length = self.get_length
        itr = self.head 
        
        while(itr):
            if index == 0:
                self.head = itr.next 
                break
            elif count == index - 1:
                itr.next = itr.next.next 
                break
            else:
                count = count + 1
                itr = itr.next 
    
    def get_element(self, index):
        length = self.get_length()
        
        if(index > length or index < 0):
            print("Index out of range.")
        
        else:
            itr = self.head 
            count = 0
            while(itr):
                if count == index:
                    value = itr.data 
                    break 
                else:
                    itr = itr.next 
                    count = count + 1
            return value
        
    def get_position(self, value):
        itr = self.head 
        count = 0
        while(itr.next):
            if itr.data == value:
                print(count)
                return
            else:
                count = count + 1
                itr = itr.next 
    
    def printll(self):
        itr = self.head
        llstr = ""
        
        while(itr):
            llstr = llstr + str(itr.data) + "- > "
            itr = itr.next
        
        print(llstr)
        

if __name__ == "__main__":
    ll = LinkedList()
    #ll.insert_at_begining(2)
    """ll.insert_at_end(3)
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(2)"""
    ll.insert([0,1,2,3,4,5,6])
    ll.insert_at(1, 10000)
    ll.printll()
    ll.remove_at(1)
    ll.printll()
    print(ll.get_element(1))
    ll.get_position(4)