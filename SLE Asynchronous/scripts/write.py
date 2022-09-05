import os
FILETYPE = 'csv'

def WriteFile_SL(dict_SortedNames, game, category):
	path = os.getcwd()
	filename = '%s_%s' % (game, category)
	
	file = ('%s\\exports\\%s.' + FILETYPE) % (path, filename)
	
	print()
	
	with open(file, 'w', encoding='utf-8') as f:
		for i, var in dict_SortedNames.items():
			print('%s' % str(var))
			f.write('%s\n' % str(var))
	print('\nExport Complete!\n')
	
def WriteFile_UL(userdata, user):
	path = os.getcwd()
	filename = '%s_export' % (user)
	
	file = '%s\\exports\\%s.txt' % (path, filename)
	
	with open(file, 'w', encoding='utf-8') as f:
		for i, var in userdata.items():
			print(str(var))
			f.write(str(var))
	print('Export Complete!')