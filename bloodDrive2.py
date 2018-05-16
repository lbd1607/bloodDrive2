#Laura Davis
#30 April 2016
#This program will collect and process data from a blood drive. 
#Instead of requiring user input to collect this data every time
#as in the previous version, this version will either save data 
#to a file or import data from a file.

#CGP145 Ch 10 Lab-3 Blood Drive

#the main function
def main():
	endProgram = 'no'
	print
	while endProgram == 'no':
		option = 0
		print
		print 'Enter 1 to enter in new data and store to file'
		print 'Enter 2 to display data from the file'
		option = input('Enter now -> ')
		print

		# declare variables
		pints = [0] * 7

		if option == 1:
			# function calls
			pints = getPints(pints)
			totalPints = getTotal(pints)
			averagePints = getAverage(totalPints)
			writeToFile(averagePints, pints)	

		else:
			averagePints = readFromFile(pints)		
			endProgram = raw_input('Do you want to end program? (Enter no or yes): ')
			while not (endProgram == 'yes' or endProgram == 'no'):
				print 'Please enter a yes or no'
				endProgram = raw_input('Do you want to end program? (Enter no or yes): ')

			
#the getPints function
def getPints(pints):
	counter = 0
	while counter < 7:
		pints[counter] = input('Enter pints collected: ')
		counter = counter + 1
	return pints

#the getTotal function
def getTotal(pints):
	totalPints = 0
	counter = 0
	while counter < 7:
		totalPints = totalPints + pints[counter]
		counter = counter + 1
	return totalPints

#the getAverage function
def getAverage(totalPints):
	averagePints = float(totalPints) / 7
	return averagePints

#the writeToFile function
def writeToFile(averagePints, pints):
	outFile = open('blood.txt', 'a')
	print >> outFile, 'Pints Each Hour'
	counter = 0
	while counter < 7:
		outFile.write(str(pints[counter]) + '\n')
		counter = counter + 1
	print >> outFile, 'Average Pints'
	outFile.write(str(averagePints) + '\n\n')
	outFile.close()

#the readFromFile function
def readFromFile(pints):
	inFile = open('blood.txt', 'r')
	str1 = inFile.read()
	print str1
	pints = inFile.read()
	print pints
	print #adds a blank line
	str2 = inFile.read()
	print str2
	averagePints = inFile.read()
	print averagePints
	inFile.close()

# calls main
main()
