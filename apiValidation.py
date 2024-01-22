
import requests
from utilities.configuration import *
from utilities.resources import apiResources

config = getConfig()
url = config['API']['endpoint'] + apiResources.getPeople
response = requests.get(url)
print(response.text)
# dict_response = json.loads(response.text)
json_response = response.json()
print(json_response)
# Checking Status Code for success response
print(response.status_code)
assert response.status_code == 200

# print(response.)

# print(json_response['results'][1]['height'])

# Verify that the total number of people where height is greater than 200 matches the expected count
count = 0
names = []
for i in range(len(json_response['results'])):
    if int(json_response['results'][i]['height']) > 100:
        count += 1
        names.append(json_response['results'][i]['name'])
print(count)
print(names)
assert count == 8

# Verify that the ten individuals returned are:
expected_names = ['Luke Skywalker', 'C-3PO', 'Darth Vader', 'Leia Organa', 'Owen Lars', 'Beru Whitesun lars',
                  'Biggs Darklighter', 'Obi-Wan Kenobi']
assert expected_names == names

# Verify that the total number of people checked equals the expected count
assert json_response['count'] == 82
