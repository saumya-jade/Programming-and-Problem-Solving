class Complex:
	def _init_(self):
		self.real = 0
		self.imag = 0
	def initComplex(self):
		line = input().split()
		if line:
			self.real = int(line[0])
			self.imag = int(line[1])
	def sum(self, c1, c2):
		self.real = c1.real + c2.real
		self.imag = c1.imag + c2.imag
	def display(self):
		if self.imag >= 0:
			print(f"{self.real} + {self.imag}i")
		else:
			print(f"{self.real} - {abs(self.imag)}i")
c1 = Complex() # Create three instances
c2 = Complex()
c3 = Complex()
c1.initComplex() # Initialize two complex numbers
c2.initComplex()
c3.sum(c1, c2) # Compute and display sum
c3.display()
