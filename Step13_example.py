from jinja2 import Template

info: dict = {
  "num": 1,
  "name": "김구라",
  "body": {
    "height": 180,
    "weight": 70,
  },
  "hobby": ["피아노", "당구", "영화"]
}

t = """
번호: {{ num }}
이름: {{ name }}
키: {{ body.height }}
몸무게: {{ body.weight }}
취미: {% for hobby in hobby %} 
  - {{ hobby }} 
{% endfor %}
"""
print(Template(t).render(info))