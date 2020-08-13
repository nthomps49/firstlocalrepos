Lines=['This is line A\n','This is line B\n','This is line C\n']
with open(r"C:\Users\natha\Documents\GitHub\firstlocalrepos\PythonLearning\WriteExample1.txt","w") as File1:
	for line in Lines:
		File1.write(line)
