import json

from hash_index.database import Database
import os

db = Database()
choices = {
    'create_table': {
        'description': 'Create table',
        'fn': db.create_table
    }
}


def show_main_menu():
    while True:
        choice = input('Provide input file name (Press q to quit): ').strip()
        if choice == 'q':
            exit()
        process_input_file(choice)


def validate_choice_object(obj):
    if 'choice' not in obj:
        return False, 'choice not provided'
    if obj['choice'] not in choices.keys():
        return False, 'invalid choice provided'
    if 'input' not in obj:
        return False, 'input not provided'
    return True, None


def process_input_file(choice):
    path = os.path.join('inputs/', choice + '.json')
    if not os.path.exists(path):
        print(f'Error - {path} does not exist')
        return
    try:
        with open(path, 'r') as file:
            payload = json.loads(file.read())
            if not isinstance(payload, list):
                print('Input should be a JSON list')
                return
            for obj in payload:
                success, error = validate_choice_object(obj)
                if not success:
                    print(error)
                    continue
                choice = obj['choice']
                fn = choices[choice]['fn']
                print('Input - ' + choices[choice]['description'])
                fn(**obj['input'])
    except json.JSONDecodeError:
        print('Error - Invalid JSON input')
    except Exception as e:
        print(f'Error - Unexpected exception occurred: {e}')


if __name__ == '__main__':
    show_main_menu()
