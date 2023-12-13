'''Creating an array to hold the digit values from each line of the input file'''
numberList = []
'''Open input file and create a list variable using each line'''
with open('input.txt', 'r') as inputFile:
	myinputList = inputFile.read().splitlines()
'''Step trhough each line of that list'''	
for line in myinputList:
	'''MySum variable to hold digit types from each line'''
	myDigits = ''
	myNum = ''
	for char in line:
		'''Step through the line and pull out numbers and add then to the string MySum'''
		if char.isdigit(): 
				myDigits += char
	'''Get the first and last numbers from each line or if only one combine into a single value'''
	if(len(myDigits) == 1):
		myNum = str(myDigits) + str(myDigits)
	else:
		myNum = str(myDigits[0]) + str(myDigits[-1])	 			 			
	print("The number for line",{myinputList.index(line)}," is ",{myNum})
	numberList.append(int(myNum))
'''Print out the final total using the Sum function'''
print('The final total is',sum(numberList))
