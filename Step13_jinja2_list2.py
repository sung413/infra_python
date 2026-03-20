from jinja2 import Template

post:list = [
  {"id": 1, "title": "제목1", "content": "내용1"},
  {"id": 2, "title": "제목2", "content": "내용2"},
  {"id": 3, "title": "제목3", "content": "내용3"},
]

my_template = """
  {% for post in posts %}
  - 글번호: {{ post.id }}, 제목: {{ post.title }}, 내용: {{ post.content }}
  {% endfor %}
"""

print(Template(my_template).render(posts=post))