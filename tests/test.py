# import requests, json, yaml

# with open('config.local.yaml', 'r') as ymlfile:
#     config = yaml.load(ymlfile)

# domain = 'http://8.142.54.87:1880'

# r = requests.post(
#     f'{domain}/c/login', data={'principal': config['harbor']['username'], 'password': config['harbor']['password']}
# )

# r1 = requests.get(f'{domain}/api/users/current', cookies=r.cookies)

# result = json.loads(r1.text)

# print(result)


hobbies = ['swiming']


print(hobbies, type(hobbies))
