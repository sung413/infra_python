from jinja2 import Template, FileSystemLoader, Environment

file_loader = FileSystemLoader('html')

env = Environment(loader=file_loader)

my_template = env.get_template('index.html')

info: dict = {
  "title": "공지사항",
  "notices": ["공지1", "공지2", "공지3"],
}

print(my_template.render(info))