import json
info = '''
{
  "name": "김성민",
  "addr": "과천",
  "favorite": ["과자", "초콜릿"]
}
'''
result = json.loads(info)

print("end")