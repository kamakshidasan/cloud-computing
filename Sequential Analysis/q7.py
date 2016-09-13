import re
file_output = open('output','r')

tv_dict = {}
film_dict = {}

for line in file_output:
 	array = line.split()
	value = array[0]
	tv_match = re.search('_\([0-9][0-9][0-9][0-9]_TV_series\)$|_\(TV_series\)$', value)
	film_match = re.search('_\([0-9][0-9][0-9][0-9]_film\)$|_\(film\)$', value)
	if tv_match != None:
		tv_title = value[0:tv_match.start(0)]
		tv_dict[tv_title] = 1
	elif film_match != None:
		film_title = value[0:film_match.start(0)]
		if film_title in film_dict:
			film_dict[film_title] += 1 
		else:
			film_dict[film_title] = 1

count = 0
for item in film_dict.items():
	film = item[0]
	if film in tv_dict:
		count += film_dict[film]
print count
file_output.close()
