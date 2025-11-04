from datetime import datetime
import json

with open('server.json') as file:
   server = json.loads(file)

def save_server():
   with open('server.json') as file:
      json.dump(server, file)

def f():
   print('=== Messenger ===')
   print('u.users')
   print('G.Groupes')
   print('x. Leave')
   print('m.messages')
   choice = input('Select an option: ')
   if choice == 'x':
    print('Bye!')
   elif choice == 'u':
        afficherusers()
   elif choice == 'G':
     affichergroupe()
   elif choice == 'm':
     for i in range (len(server['messages'])):
        print(server['messages'])
        print('r.retourmenu')
        choice = input('Select an option: ')
        if choice == 'r':
         f()
    
   else:
        print('Unknown option:', choice)


def afficherusers():
    for i in range (len(server['users'])):
        print(server['users'][i])
        print(server['users'][i]['name'],server['users'][i]['id'])
    print('r.retourmenu')
    print('aj.ajouter un uttilisateur')
    choice = input('Select an option: ')
    if choice == 'r':
        f()
    elif choice == 'aj':
        nom=input('nom du user')
        newid= len(server['users'])+1
        server['users'].append({'id':newid , 'name':nom})
        save_server()
        f()

def affichergroupe():
   for i in range (len(server['channels'])):
        print(server['channels'][i]['name'],server['channels'][i]['member_ids'])
   print('r.retourmenu')
   print('ajg.ajoutergroupe')
   choice = input('Select an option: ')
   if choice == 'r':
     f()
   elif choice == 'ajg':
      nom2=input('nom du groupe')
      newid2=len(server['channels'])+1
      server['channels'].append({'id':newid2,'name':nom2,'member_ids': []})
      nb=int(input('nombre de personnes dans le groupe'))
      for i in range(nb+1):
         x=input('id uttilisateur')
         server['channels'][-1]['member_ids'].append(x)
      save_server()
      f()

         
f()

