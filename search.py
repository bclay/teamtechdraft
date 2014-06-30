from pygoogle import pygoogle

name = 'brynn claypoole'

g = pygoogle(name)
g.pages = 5
print '*Found %s results*'%(g.get_result_count())
urls = g.get_urls()
for index in range(15):
	print 'URL: ', urls[index]
	




