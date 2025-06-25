import re

# Should start with alphabet, can have one or more alphanumeric chars after tht
PATTERN = r'{{[a-zA-Z][\w_]+}}'


class Template:
    def __init__(self, _id, _str):
        self.id = _id
        self.str = _str
        self.variables = self.parse_template()

    def parse_template(self):
        matches = re.findall(PATTERN, self.str)

        # Remove leading and trailing braces
        matches = [match[2:-2] for match in matches]

        # Remove dups
        return set(matches)

    def render(self, kvps):
        self.validate_values(kvps)
        rendered = self.str
        for k, v in kvps.items():
            rendered = rendered.replace('{{' + k + '}}', v)
        return rendered

    def validate_values(self, kvps):
        if sorted(kvps.keys()) != sorted(self.variables):
            raise Exception('invalid keys provided')

        for _, v in kvps.items():
            if v is None:
                raise Exception('one or more values are null')

        return True

    def __str__(self):
        return f'ID - {self.id}, Content - {self.str}, Variables Detected - {self.variables}'









