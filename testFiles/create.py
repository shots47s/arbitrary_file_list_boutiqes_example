for i in range(1,10):
	with open("file_{0}.txt".format(i),"w") as f:
		f.write("This has number {0}\n".format(i))
