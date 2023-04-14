def show_homepage():
    x = '''
    === DonateMe Homepage ===
    '''
    print(x)
    print("------------------------------------------")
    print("| 1.    Login     | 2.    Register       |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Donate    | 4.    Show Donations |")
    print("------------------------------------------")
    print("|              5.    Exit                |")
    print("------------------------------------------")


def donate(username):
    donate_amt = input('donate amount: ')
    donate_sting = f'{username} donated ${donate_amt}'
    print('Thank You,', donate_sting)
    return donate_amt


def show_donations(donations):
    print('\n -- All Donations---')
    if len(donations) == 0:
        print("No donations")
    elif len(donations) > 0:
        for entries in donations:
            print(entries)
