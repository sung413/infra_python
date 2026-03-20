from jinja2 import Template

my_template = """
친구목록
{% for name in friends %}
- {{ name }}
{% endfor %}
"""

template:Template = Template(my_template)

friends = ["홍길동", "이순신", "안정환"]
result:str = template.render(friends=friends)
print(result)

