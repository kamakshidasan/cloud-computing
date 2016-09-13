file_output = open('output','r')
count = 0
for line in file_output:
	array = line.split()
	name = array[0].lower()
	if 'cloud' in name and 'computing' in name:
		count += 1
print count
file_output.close()
