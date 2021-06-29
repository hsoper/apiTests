import requests
response = requests.get('https://hacker-news.firebaseio.com/v0/maxitem.json?print=pretty')
data = response.json()
code = int(data)
response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{code}.json?print=pretty')
story = response.json()

while story['type'] != 'story':
  code -=1
  response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{code}.json?print=pretty')
  story = response.json()
print(story)
url = "No link was given"
by = "No author was given"
title = "No title was given"
for key,item in story.items():
  if key == 'title':
    title = item
  elif key == 'by':
    by = item
  elif key == 'url':
    url = item
print('Title : ',title,'\nAuthor : ',by,"\nLink : ",url)