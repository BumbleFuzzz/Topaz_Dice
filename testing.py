def checkInt(value):
	
	flag = True
	
	try:
		int(value)
	except ValueError:
		flag = False
		
	return flag
	
def checkIndex(list, index):
		
	flag = True

	try:
		list[index]
	
	except IndexError:
		flag = False
	
	return flag