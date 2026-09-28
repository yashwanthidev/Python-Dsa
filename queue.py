class Queue:
  def __init__(self,cap=5):
      self._a=[None for _ in range(cap)]
      self._front=0
      self._rear=-1
      self._c=0
  def peek(self):
      if self.isempty():
        return "No Elements"
      return self._a[self._front]
  def enqueue(self,data):
      if self.isfull():
          return "OVERFLOW!"
      self._a[self._c]=data
      self._c+=1
      return f"{data} is enqueued"
  def rear(self):
    if self.isempty():
      return "No Elements"
    return self._a[self._c-1]
  def dequeue(self):
    if self._c == 0:
      return "UNDERFLOW!"
    data = self._a[self._front]
    for i in range(1,self._c):
      self._a[i-1]=self._a[i]
    self._a[self._c-1] = None
    self._c -= 1
    return f"{data} is removed"
  def isempty(self):
    return self._c==0
  def isfull(self):
    return self._c==len(self._a)

queue=Queue()
print(queue.enqueue(10))
print(queue.enqueue(20))
print(queue.enqueue(30))
print(queue.enqueue(40))
print(queue.enqueue(50))
print(f" front element of queue: {queue.peek()}")
print(f"  rear element of queue: {queue.rear()}")
print(queue.enqueue(60))
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(f" front element of queue: {queue.peek()}")
print(f"  rear element of queue: {queue.rear()}")