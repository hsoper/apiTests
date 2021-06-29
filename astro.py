import requests 

response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()
print("Status Code :",response.status_code)
people = data['people']

for i in range(0,5):
  print(people[i]['name'])