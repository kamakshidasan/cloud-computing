file_input = open('pagecounts-20160501-000000','r')
count = 0
for line in file_input:
	array = line.split()
	if len(array) == 4:
		count += int(array[2])
	elif len(array) == 3:
		count += int(array[1])
print count
file_input.close()
