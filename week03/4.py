class node:
    def __init__(self,data):
        self.data=data 
        self.next=None
class links:
    head=None
    def add(self,data):
        new_node=node(data)
        if self.head==None:
            self.head=new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
    def delete(self,target):
        if self.head==None:
            return
        if self.head.data==target:
            self.head=self.head.next
            return
        current=self.head
        while(current.next!=None):
            if current.next.data==target:
                current.next=current.next.next
                return
            current=current.next
    def find(self,target):
        current=self.head
        while(current!=None):
            if current.data==target:
                print("yes")
                return
            current=current.next
        print("no")
        return 
    def switch(self,old,new):
        current=self.head
        while(current!=None):
            if current.data==old:
                current.data=new
            current=current.next
        return 
    def pr(self):
        current=self.head
        while(current!=None):
            print(current.data,end=" => ")
            current=current.next
        print()
        return 
l1=links()
l1.pr()
l1.add(1)
l1.pr()
l1.add(2)
l1.pr()
l1.add(3)
l1.pr()
l1.add(4)
l1.pr()
l1.delete(3)
l1.pr()
l1.switch(2,8)
l1.pr()
