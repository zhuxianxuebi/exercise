"""
链表
"""

class node:
	def __init__(self,val):
		self.val = val
		self.next = None

class Nodelist:
	def __init__(self):
		self.head = None

	def is_empty(self):
		if self.head == None:
			return True
		else:
			return False

	def get_len(self):
		count = 0
		Node = self.head
		while True:
			if Node == None:
				break
			count += 1
			Node = Node.next
		return count

	def add(self,val):
		Node = node(val)
		if self.is_empty():
			self.head = Node
		else:
			Node.next = self.head
			self.head = Node

	def append(self, val):
		Node = node(val)
		if self.is_empty():
			self.head = Node
		else:
			cur = self.head
			while cur.next != None:
				cur = cur.next
			cur.next = Node

	def travel(self):
		if self.is_empty():
			print("链表为空！")
		else:
			cur = self.head
			while True:
				print(cur.val, end = "")
				if cur.next == None:
					break
				cur = cur.next

	def insert(self, i, val):
		if i <= 1:
			self.add(val)
		elif i > self.get_len():
			self.append(val)
		else:
			cur = self.head
			for j in range(i-2):
				cur = cur.next
			Node = node(val)
			Node.next = cur.next
			cur.next = Node


	def search(self, i):
		if i < 1 or i > self.get_len():
			print("所找元素不存在！")
		else:
			cur = self.head
			for j in range(i-1):
				cur = cur.next
			print(cur.val)

if __name__ == '__main__':
	n = Nodelist()
	for i in range(7):
		n.append(i)
	n.travel()
	n.search(5)



		