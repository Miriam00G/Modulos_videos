import sys

clients = [
    {
        'name': 'Joel',
        'company': 'Google',
        'email': 'joel@google.com',
        'position': 'Software engineer',
    },
    {
        'name': 'Miryam',
        'company': 'Facebook',
        'email': 'miryam@facebook.com',
        'position': 'Data engineer',
    }
]

def create_client(client):
    if client not in clients:
        clients.append(client)
        print(f"Client '{client['name']}' has been added.")
    else:
        print("Client is already in the client's list")

def list_clients():
    print('{:<5} | {:<10} | {:<10} | {:<20} | {:<15}'.format('ID', 'Name', 'Company', 'Email', 'Position'))
    print('*' * 60)
    for idx, client in enumerate(clients):
        print('{:<5} | {:<10} | {:<10} | {:<20} | {:<15}'.format(
            idx,
            client['name'],
            client['company'],
            client['email'],
            client['position']
        ))

def update_client(client_id, updated_client):
    if 0 <= client_id < len(clients):
        clients[client_id] = updated_client
        print(f"Client ID {client_id} has been updated.")
    else:
        print("Client not in the client's list")

def delete_client(client_id):
    if 0 <= client_id < len(clients):
        deleted_client = clients.pop(client_id)
        print(f"Client '{deleted_client['name']}' has been deleted.")
    else:
        print(f"Client ID {client_id} is not in the client's list")

def search_client(client_name):
    for client in clients:
        if client['name'].lower() == client_name.lower():
            return True
    return False

def _get_client_field(field_name, message='What is the client {}? '):
    field = None
    while not field:
        field = input(message.format(field_name))
    return field

def __get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }
    return client

def __print_welcome():
    print("WELCOME TO PLATZI VENTAS")
    print('*' * 50)
    print("What would you like to do today?")
    print("[C]reate client")
    print("[L]ist clients")
    print("[U]pdate client")
    print("[D]elete client")
    print("[S]earch client")

if __name__ == '__main__':
    __print_welcome()
    command = input().upper()

    if command == 'C':
        client = __get_client_from_user()
        create_client(client)
        list_clients()

    elif command == 'L':
        list_clients()

    elif command == 'U':
        client_id = int(_get_client_field('id'))
        updated_client = __get_client_from_user()
        update_client(client_id, updated_client)
        list_clients()

    elif command == 'D':
        client_id = int(_get_client_field('id'))
        delete_client(client_id)
        list_clients()

    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name)
        if found:
            print(f"The client '{client_name}' is in the client's list")
        else:
            print(f"The client '{client_name}' is not in our client's list")
    else:
        print("Invalid command")
