class calc():
	def add(self, a, b):
		self.a = a
		self.b = b
		return self.a + self.b

	def minus(self, a, b):
		self.a = a
		self.b = b
		return self.a - self.b

	def multi(self, a, b):
		self.a = a
		self.b = b
		return self.a * self.b

	def div(self, a, b):
		self.a = a
		self.b = b
		return self.a / self.b

x = 6
y = 3
s = calc()
print(s.add(x,y))
print(s.minus(x,y))
print(s.multi(x,y))
print(s.div(x,y))

