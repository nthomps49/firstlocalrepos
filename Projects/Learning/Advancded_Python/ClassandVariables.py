class Dog:
	def __init__(self,name,breed):
	
		self.name = name
		self.breed = breed
  
	def print_details(self):
		
		print("My name is %s and I am a %s" % (self.name, self.breed))

d1 = Dog('Rex', 'Chiwawa')
print(d1.print_details())