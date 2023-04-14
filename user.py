def login(database, username, password):
    if username in database.keys():
        # most important line here, the password is the value of the key
        if password == database[username]:
            print(f'logged in as {username}')
            return username
        else:
            print('incorrect password')
    else:
        print('user not in database')


def register(database, username):
    if username in database.keys():
        print(f'{username} already registered')
        return ''
    elif username not in database.keys():
        return username
