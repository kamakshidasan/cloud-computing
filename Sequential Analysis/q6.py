import re
file_output = open('output','r')
count = 0
for line in file_output:
	array = line.split()
	numeroalpha = re.match('^[0-9][a-zA-Z]', array[0])
	if numeroalpha != None:
		count += int(array[1])
print count
file_output.close()


