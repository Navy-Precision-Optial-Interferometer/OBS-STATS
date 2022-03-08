import requests
from bs4 import BeautifulSoup, SoupStrainer
n_files = 36  # change to however many you want to download, there are about 4800 in the archive but 1000 goes back to 2015

# Connect to the starlog archive page and pull all of its html "content"
s=requests.Session()
s.auth=('SEXTANS USERNAME', 'SEXTANS PASSWORD')
#r = 'http://sextans.lowell.edu/npoi-internal/observing/starLogs/starLogArchive.html'
#r = 'http://sextans.lowell.edu/npoi-internal/observing/obsLogs/obsLogArchive.html'
r = 'http://sextans.lowell.edu/npoi-internal/observing/obsLists/obsListArchive.html'

content = s.get(r).content

# Find and make a list of all the starlog links on the archive page
all_starlogs = []
for link in BeautifulSoup(content, parse_only=SoupStrainer('a'), features='html.parser'):
    if hasattr(link, "href"):
        all_starlogs.append(link['href'])
        
#all_files = ['http://sextans.lowell.edu/npoi-internal/observing/starLogs/' + all_starlogs[i] for i in range(len(all_starlogs))]
#all_files = ['http://sextans.lowell.edu/npoi-internal/observing/obsLogs/' + all_starlogs[i] for i in range(len(all_starlogs))]
all_files = ['http://sextans.lowell.edu/npoi-internal/observing/obsLists/' + all_starlogs[i] for i in range(len(all_starlogs))]

#print(all_starlogs[0][11:])

# starlogs, obslists
for i in range(n_files):
    with open(all_starlogs[i][11:] + '.txt', 'w+') as f:
        f.write(s.get(all_files[i]).content.decode())
        f.close()
        if i % 10 == 0:
            print(i)

# obslogs
'''for i in range(n_files):
    with open(all_starlogs[i][10:] + '.txt', 'w+') as f:
        f.write(s.get(all_files[i]).content.decode())
        f.close()
        if i % 10 == 0:
            print(i)'''
