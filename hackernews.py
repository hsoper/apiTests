import requests
u = 'https://hacker-news.firebaseio.com/v0/maxitem.json?print=pretty'
response = requests.get(u)
data = response.json()
code = int(data)
u = f'https://hacker-news.firebaseio.com/v0/item/{code}.json?print=pretty'
response = requests.get(u)
story = response.json()
while story['type'] != 'story':
    code -= 1
    u = f'https://hacker-news.firebaseio.com/fv0/item/{code}.json?print=pretty'
    response = requests.get(u)
    story = response.json()
url = "No link was given"
by = "No author was given"
title = "No title was given"
for key, item in story.items():
    if key == 'title':
        title = item
    elif key == 'by':
        by = item
    elif key == 'url':
        url = item
print('Title : ', title, '\nAuthor : ', by, "\nLink : ", url)
