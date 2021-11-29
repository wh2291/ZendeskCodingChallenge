import requests

credentials = 'Username', 'Password'
session = requests.Session()
session.auth = credentials
zendesk = 'Individual Zendesk Website'

url = f'{zendesk}/api/v2/tickets.json'
response = session.get(url)
if response.status_code != 200:
    print(f'Error with status code {response.status_code}')
    exit()

data = response.json()


def userInterface():
    start = "Welcome to ticket viewer.\n"
    intro = "Type 'menu' to view options or 'quit' to exit."
    menu = "Select view options:  \n Enter 'all' to view all tickets \n Enter 'one' to view a single ticket \n Enter 'quit' to exit	\n"
    print(start)
    yes = True
    yes2 = True
    while yes2:
        val1 = input(intro)
        if(val1.lower() == 'menu'):
            val = input(menu)
            yes2= False
            break
        if(val1.lower() == 'quit'):
            print('Ending session, thanks for using ticket viewer')
            yes2= False
            return
        else:
            print('Invalid entry, please try again')
    while yes:
        if (val.lower() == 'menu'):
            val = input(menu)
        if (val.lower() == 'quit'):
            print('Ending session, thanks for using ticket viewer')
            return
        if (val.lower() == 'one'):
            val2 = input("Enter a ticket number")
            val2= int(val2)
            if (isinstance(val2, int)) and (val2 <= len(data['tickets'])):
                print('Ticket ID:',data['tickets'][val2-1]['id'], 'Created At:',data['tickets'][val2 - 1]['created_at'], 'Ticket Subject:',data['tickets'][val2 - 1]['subject'])
                val = input(intro)
            else:
                print("Not a valid ticket please try again")
                val = 'one'
        if (val.lower() == 'all'):
            yes3 = True
            i=0
            curr = 25

            while (yes3):
               for x in data['tickets'][i:curr]:
                   print('Ticket ID:',x['id'], 'Created At:',x['created_at'], 'Ticket Subject:',x['subject'])
               val3 = input("Enter 'next' to view the next page of tickets, other wise enter 'quit' or 'menu'")
               if (val3 == 'next'):
                   i= i +25
                   curr= curr+25
                   if(curr > len(data['tickets'])):
                       curr = len(data['tickets'])
               if (val3 == 'quit'):
                   val = 'quit'
                   break
               if(val3 == 'menu'):
                   val= 'menu'
                   break
               else:
                   print('Invalid entry try again')

userInterface()