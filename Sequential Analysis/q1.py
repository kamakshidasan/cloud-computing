file_input = open('pagecounts-20160501-000000','r')
count = 0
for line in file_input:
    count += 1
print count
file_input.close()
