import yaml

info = '''
info:
  name: John Doe
  age: 30
  email: john.doe@example.com
'''
result = yaml.load(info, Loader=yaml.FullLoader)
yaml.safe_load(info)
print(result)

result2 = yaml.dump(result)
print(result2)