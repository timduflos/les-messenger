from datetime import datetime

server = {
    'users': [
        {'id': 41, 'name': 'Alice'},
        {'id': 23, 'name': 'Bob'}
    ],
    'channels': [
        {'id': 12, 'name': 'Town square', 'member_ids': [41, 23]}
    ],
    'messages': [
        {
            'id': 18,
            'reception_date': datetime.now(),
            'sender_id': 41,
            'channel': 12,
            'content': 'Hi 👋'
        }
    ]
}

print('=== Messenger ===')
print('u.users')
print('G.Groupes')
print('x. Leave')
print('m.messages')
choice = input('Select an option: ')
if choice == 'x':
    print('Bye!')
elif choice == 'u':
 for i in range (len(server['users'])):
    print(server['users'][i]['name'],server['users'][i]['id'])
elif choice == 'G':
   for i in range (len(server['channels'])):
    print(server['channels'][i]['name'],server['channels'][i]['member_ids'])
elif choice == 'm':
   for i in range (len(server['messages'])):
    print(server['messages'])
   
else:
    print('Unknown option:', choice)
