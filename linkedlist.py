class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
  def insert(self,data):#this works for insert at end
    new_node = Node(data)
    temp=self
    while temp.next!=None:
      temp=temp.next
    temp.next=new_node
  def insertAtBeginning(self,data):
    new_node = Node(data)
    new_node.next=self
    #self=new_node(thisiswrongselfalocalparameterchangethelocalvariableselfwouldntchangeactualheadvariable)
    return new_node
  def insertAtLocation(self,data,pos):
    new_node = Node(data)
    temp=self
    for i in range(pos-1):
      temp=temp.next
    new_node.next=temp.next
    temp.next=new_node
  def deleteFromBeginning(self):
    if self is None:
      return None
    return self.next
  def delete_end(self):
    if self.next is None:
      return None
    temp=self
    while temp.next.next is not None:
      temp=temp.next
    temp.next=None
    return self
  def Display(self):
    temp=self
    while temp!=None:
      print(temp.data,end=" ")
      temp=temp.next
  def search(self,value):
    temp=self
    i=0
    while temp is not None:
      if temp.data==value:
        print()
        print(f"{value} found at {i}")
        return
      temp=temp.next
      i += 1
    print()
    print("{value} is  not found")
head=Node(2)
head.next=Node(3)
head.insert(4)
head.insert(5)
head=head.insertAtBeginning(1)
head.insertAtLocation(0,1)
head=head.deleteFromBeginning()
head=head.delete_end()
head.Display()
head.search(2)
# head = Node(2)
# head.next = Node(3)
# head.next.next = Node(4)
# temp=head
# head.Display()