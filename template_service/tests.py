import unittest
from service import Service


class RenderTest(unittest.TestCase):

    def setUp(self):
        self.s = Service()
        self.s.add_template('Just a quick reminder: {{event}} is due soon. Please check it out!')
        self.s.add_template('Hello {{name}}, your {{order}} has been confirmed. '
                            'Track it here: {{link}}. Thank you! – {{company}}')
        self.s.add_template('Hello {{name}}, your name is {{name}}.')
        print('------------------------------------------------')

    def test_render_template_1(self):
        kvps = {
            'event': 'Tax Submission'
        }
        expected = 'Just a quick reminder: Tax Submission is due soon. Please check it out!'
        self.assertEqual(expected, self.s.render_template(0, kvps))

    def test_render_template_2(self):
        kvps = {
            'name': 'Ojasva',
            'order': '123',
            'link': 'https://www.google.com',
            'company': 'RZP'
        }
        expected = 'Hello Ojasva, your 123 has been confirmed. Track it here: https://www.google.com. Thank you! – RZP'
        self.assertEqual(expected, self.s.render_template(1, kvps))

    def test_render_template_3(self):
        kvps = {
            'name': 'Ojasva'
        }
        expected = 'Hello Ojasva, your name is Ojasva.'
        self.assertEqual(expected, self.s.render_template(2, kvps))


if __name__ == '__main__':
    unittest.main()