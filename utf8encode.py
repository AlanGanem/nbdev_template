import glob

def utf8encode(file_path):
	'''
	encodes a file to utf-8 and unicode charset
	'''	
	exc = []
	encodings = ['utf-8','ascii','latin-1','CP1252']
	for encoding in encodings:
		try:
			with open(file_path, 'r+', encoding=encoding, errors = 'replace') as file:				
				file.write(file.read())
				file.truncate()
			print(f'Read {file_path} as {encoding} and converted to utf-8 (unicode)')
			return
		except Exception as e:
			exc.append(e)
	print(f'It was not possible to modify {file_path} with exceptions {exc}')

def get_html_paths(roots):	
	'''
	gets path of html files recursively starting from root in roots(list of roots)
	'''
	assert isinstance(roots,(tuple,list,set))
	all_files = []
	for root in roots:
	    files = glob.glob(f'{root}/**/*.html',
	                      recursive=True)
	    all_files += files if type(files) != str else [files]

	return all_files

if __name__ == '__main__':	
	'''
	converts .html files in /docs to utf-8 and unicode charset
	'''
	paths = get_html_paths(['docs'])
	for path in paths:		
		utf8encode(path)