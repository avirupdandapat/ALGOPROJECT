import requests

DOMAIN = 'Southeast Asia'
TOKEN = 'dapi04ff27ce22586d5e881cfe4474acb186'

#response = requests.get(
    #'https://adb-8888568946254331.11.azuredatabricks.net/?o=8888568946254331#/api/2.0/workspace/list',
    #{"path": "/dandapat.ad/dandapat.ad@pg.com/"}, headers={'Authorization': 'Bearer %s' % TOKEN})
response = requests.get(
    'https://adb-8888568946254331.11.azuredatabricks.net/?o=8888568946254331#/api/2.0/workspace/list', headers={'Authorization': 'Bearer %s' % TOKEN})
print(response.status_code)
print(response.text)
