from jinja2 import Template

my_template = """
    번호: {{num}}
    이름: {{name}}
    주소: {{addr}}
"""

mem1 = {
  "num": 1,
  "name": "홍길동",
  "addr": "서울"
}

mem2 = {
  "num": 2,
  "name": "트럼프",
  "addr": "미국"
}


template:Template = Template(my_template)
result = template.render(mem1)
print(result)

result2 = template.render(mem2)
print(result2)