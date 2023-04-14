from calendar import firstweekday
from donations_pkg.homepage import show_homepage
from donations_pkg.homepage import donate
from donations_pkg.homepage import show_donations
from donations_pkg.user import login
from donations_pkg.user import register


database = {"aaron": "1234"}
donations = []
authorized_user = ""
while True:
    print("          === DonateMe Homepage ===          ")
    show_homepage()
    if authorized_user == '':
        print('You must be logged in to donate:')
    else:
        print(f'logged in {authorized_user}')

    option = input("Enter option: ")
    if option == '1':
        username = input("enter Username: ")
        password = input("enter password: ")
        authorized_user = login(database, username, password)

    elif option == '2':
        username = input("enter Username: ")
        password = input("enter password: ")
        authorized_user = register(database, username)
        if authorized_user != '':
            database[username] = password
            print(f'Username {username} is registered!')

    elif option == '3':
        if authorized_user == '':
            print('login before donating')
        elif authorized_user != '':
            donation_string = donate(username)
            donations.append(donation_string)

    elif option == '4':
        if authorized_user == '':
            print('login before showing donations')
        elif authorized_user != '':
            (show_donations(donations))


fic_website()
