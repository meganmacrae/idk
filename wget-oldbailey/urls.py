
urls = '';
f=open('urls.txt','w')
for x in range(1, 2645):
    urls = 'https://www.oldbaileyonline.org/search.jsp?count=0&_offences_offenceCategory_offenceSubcategory=kill_murder&form=stats_offences/1/2645%d.jpg\n' % (x)
    f.write(urls)
f.close
