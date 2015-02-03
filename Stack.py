class Stack:
  def __init__(self):
      self.stackElms = []
      self.maxLen = 100

  def push(self,num):
      if self.full():
          raise "Error in pop - stack is full\n"
      else:
          self.stackElms = [num] + self.stackElms

  def pop(self):
      if self.empty():
          raise "Error in pop - stack is empty\n"
      else:
          del self.stackElms[0]

  def top(self):
      if self.empty():
          raise "Error in pop - stack is empty\n"
      else:
          return self.stackElms[0]

  def empty(self):
      return len(self.stackElms) == 0

  def full(self):
      return len(self.stackElms) == self.maxLen

  def inspect(self):
      print(self.stackElms)

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push("abc")
s.push("def")
s.pop()
print(s.top())
s.inspect()
print(len(s.stackElms))

