import re
file_output = open('output','r')
count = 0
for line in file_output:
	array = line.split()
	extension = re.search('[^a-zA-Z]cloud[^a-zA-Z]|^cloud[^a-zA-Z]|[^a-zA-Z]cloud$|^cloud$', array[0], re.IGNORECASE)
	if extension != None:
		count += 1
print count
file_output.close()
