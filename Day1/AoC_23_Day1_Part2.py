'''Creating a custom object type to hold values and their location in the string'''
class digitCoordinates:
    def __init__(self, index, value):
        self.index = index
        self.value = value

    def __repr__(self):
        return f"index:{self.index},value:{self.value}"
'''Creating an array to hold the digit values from each line of the input file'''
numberList = []
finalSum = 0
'''Open input file and create a list variable using each line'''
with open('input.txt', 'r') as inputFile:
	myinputList = inputFile.read().splitlines()
'''Step trhough each line of that list'''	
for line in myinputList:
	'''An array to hold the custom objects, a blank string to hold the number contruct, and lists of text digits and numerals to use in find loops'''
	indexAndValue = []
	testDigits = ['one','two', 'three','four','five','six','seven','eight','nine']
	testNumerals = ['1','2','3','4','5','6','7','8','9']
	'''Check through each of the arrays to find matches and append them to our array'''
	for digit in testDigits: 
		if line.find(digit) != -1:
			thisIndex = line.find(digit)
			thisValue = str(testDigits.index(digit) + 1)
			myCoordinate = digitCoordinates(thisIndex,thisValue)
			indexAndValue.append(myCoordinate)	
	for number in testNumerals:
	 	if line.find(number) != -1:
	 		thisIndex = line.find(number)
	 		thisValue = number
	 		myCoordinate = digitCoordinates(thisIndex,thisValue)
	 		indexAndValue.append(myCoordinate)
	print(indexAndValue)
	sortedValues = sorted(indexAndValue, key=lambda x: x.index)
	print(sortedValues)
	if len(sortedValues)==1:
		myNum = str((sortedValues[0]).value)+str((sortedValues[0]).value)
	else:
		myNum = str((sortedValues[0]).value) + str((sortedValues[-1]).value)
	numberList.append(int(myNum))
print('The sum total via sum is ' + str(sum(numberList)))
for total in numberList:
		finalSum += total	
print('The final total is ', finalSum)

