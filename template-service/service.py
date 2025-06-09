from template import Template


class Service:
    def __init__(self):
        self.templates = []

    def add_template(self, _str):
        _id = len(self.templates)
        template = Template(_id, _str)
        self.templates.append(template)
        print(f'Template {_id} created and added Successfully')
        print(template)

    def render_template(self, _id, kvps):
        template = self.templates[_id]
        return template.render(kvps)

