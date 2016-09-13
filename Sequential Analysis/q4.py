file_output = open('output','r')
for line in file_output:
 	array = line.split()
 	if 'film' in array[0]:
 		print array[1]
 		break
file_output.close()
