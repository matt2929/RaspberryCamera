class batch_write:
	
	def __init__(self, filename, batch_size):
		self.filename = filename
		self.batch_size = 100
		self.output = ""
		self.in_count = 0

	def create_output(self):
		file = open(self.filename,"w")
		file.close()

        def write_data(self):
                file = open(self.filename,"w")
                file.write(self.output)
                self.output=""
                self.in_count=0
                file.close()

	def add_line(self, line):
		self.in_count+=1
		self.output += line + "\n"
 		if self.in_count == self.batch_size:
			self.write_data()
			self.in_count=0

x = batch_write("test.txt", 100)
x.create_output()
for i in range(1000):
	x.add_line(str(i))
