import re
import time
start_time = time.time()
file_input = open('pagecounts-20160501-000000','r')
file_output = open('sorted','w')

duplicate = {}
for line in file_input:
	array = line.split()
	name = array[1]
	if len(array) == 4:
		if array[0] == 'en' or array[0] == 'en.m':
			namespace = re.match('^(Media|Special|Talk|User|User_talk|Wikipedia|Wikipedia_talk|File|File_talk|MediaWiki|MediaWiki_talk|Template|Template_talk|Help|Help_talk|Category|Category_talk|Portal|Portal_talk|Book|Book_talk|Draft|Draft_talk|Education_Program|Education_Program_talk|TimedText|TimedText_talk|Module|Module_talk|Gadget|Gadget_talk|Gadget_definition|Gadget_definition_talk|Topic)(:|%3a|%3A)',name,re.IGNORECASE)
			if not namespace:
				upper_present = True
				if name[0].isalpha():
					if name[0].isupper():
						upper_present = True
					else:
						upper_present = False
				if upper_present == True:
					extension = re.search('\.(png|gif|jpg|jpeg|tiff|tif|xcf|mid|ogg|ogv|svg|djvu|oga|flac|opus|wav|webm|ico|txt)$',name,re.IGNORECASE)
					if not extension:
						boilerplate = re.match('^(404_error/|Main_Page|Hypertext_Transfer_Protocol|Search)$',name)
						if not boilerplate:
							if name in duplicate:
								duplicate[name] += int(array[2])
							else:
								duplicate[name] = int(array[2])
for item in duplicate.items():
	file_output.write(str(item[0])+'\t'+str(item[1])+'\n')
	del item
file_input.close()
file_output.close()
print("--- %s seconds ---" % (time.time() - start_time))
