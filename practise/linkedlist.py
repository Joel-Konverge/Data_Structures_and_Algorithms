class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
    
class Linkedlist():
    def __init__(self):
        self.head=None
    def append(self,data):
        if self.head is None:
            self.head=Node(data)
        cur_val=self.head
        while cur_val.next:
            cur_val=cur_val.next
        cur_val.next=Node(data)
    def remove(self,data):
        if self.head is None:
            print("Empty Linkedlist")
            return
        elif self.head.data==data:
            self.head=self.head.next
            return
        val=self.head
        while val:
            if val.next is None:
                print("Not found")
                break
            if val.next.data==data:
                val.next=val.next.next
                break
            val=val.next
    def length(self):
        if self.head is None:
            print("Empty Linkedlist")
            return
        count=0
        cur_val=self.head
        while cur_val:
            count+=1
            cur_val=cur_val.next
        return count
            
    def get_val(self,pos):
        if self.head is None:
            print("Empty Linkedlist")
            return 
        count=1
        val=self.head
        if pos>self.length() or pos<=0:
            return "position not found"
        while val:
            
            if count==pos:
                return val
            count+=1
            val=val.next


    def reverse(self):
        cur_val=self.head
        pre_val=None
        while cur_val:
            next_val=cur_val.next
            cur_val.next=pre_val
            pre_val=cur_val
            cur_val=next_val
        self.head=pre_val
    def disp(self):
        if self.head is None:
            return 0
        cur_val=self.head
        while cur_val:
            print(cur_val.data , end=",")
            cur_val=cur_val.next

l=Linkedlist()
l.head=Node(5)
l.head.next=Node(6)
l.append(8)
l.append(9)
l.append(13)
print("appended linkedlist")
l.disp()
print()
l.remove(13)
print("13 removed from linkedlist:",)
l.disp()
print()
print("length:",l.length())
print("Value at position 3:",l.get_val(3).data)
l.reverse()
print("reverse linkedlist:")
l.disp()
print()

