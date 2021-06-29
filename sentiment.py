import requests
user = input("Input any text\n")
url = 'http://text-processing.com/api/sentiment/'
myobj = {'text': user}

response = requests.post(url, data = myobj)
data = response.json()
temp = ''
for key,item in data.items():
  if(type(item) is dict):
    for k,i in item.items():
      temp += f"\n\t\t{k} : {i}"
    print(key,":",temp)
  else:
    print(key,":",item)