import json

from hash_index.database import Database
import os

db = Database()
choices = {
    'create_table': {
        'description': 'Create table',
        'fn': db.create_table
    }
    # 'create_index': {
    #     'description': 'Create Index',
    #     'fn':
    # }
}

# TODO
# 1. Improve Menu - Think about a general design
# 2. Pythonic way to append or create in hash index
# 3. Pass by reference and using copy() methods - Is there a better way?
# 4. Check thread safety of operations
# 5. general refactoring (for eg. creating constants)
# 6. Implement compaction and merging

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
                print('Error - Input should be a JSON list')
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
   #show_main_menu()
    table = db.create_table('customers', ['id', 'name'])
    table.insert({
        'id': 1,
        'name': 'ojasva'
    })
    table.insert({
        'id': 2,
        'name': 'ojasva'
    })
    table.insert({
            'id': 12,
            'name': 'ojasva'
    })
    table.insert({
        'id': 12,
        'name': 'ojas'
    })
    table.insert({
        'id': 112,
        'name': 'ojasjain'
    })

    table.create_hash_index('id')
    table.create_hash_index('name')

    # print(table.get('id', 112))
    # print(table.get('name', 'oasdasdsadasdsadsadasds'))
    table.delete('id', 12)
    # table.print_hash_table('id')
    # table.print_hash_table('name')

    table.insert({
        'id': 431,
        'name': 'John'
    })
    table.insert({
        'id': 786,
        'name': 'M'
    })
    table.insert({
    'id': 100,
    'name': 'J'
    })

    table.update('id', 100, 'name', 'Jain')
    table.update('name', 'John', 'name', 'Von')
    print(table.get('id', 1))
    print(table.get('id', 2))
    print(table.get('id', 12)) # error expected
    print(table.get('id', 112))
    print(table.get('id', 431))
    print(table.get('id', 786))
    print(table.get('id', 100))

    print(table.get('name', 'ojasva'))
    print(table.get('name', 'ojas')) # error expected
    print(table.get('name', 'ojasjain'))
    print(table.get('name', 'John')) # error expected
    print(table.get('name', 'M'))
    print(table.get('name', 'J')) # error expected
    print(table.get('name', 'Jain'))
    print(table.get('name', 'Von'))





