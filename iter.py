class myiter(object):
	def __init__(self,n):
		self.i=0
		self.n=n
	def __iter__(self):
		return myiter(self.n)
	def next(self):
		if self.i < self.n:
			i=self.i
			self.i+=1
			return i
		else:
			raise StopIteration()


m=myiter(5)
for i in m:
	print i
