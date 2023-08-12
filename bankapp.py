import time
def welcome():
    user = input("""
    ONLINE BANKING SYSTEM

    1. Deposit Money
    2. Polaris Bank
    3. GTBank
    >>> """)
    if user == '1':
        time.sleep(1)
        deposit()
    elif user == '2':
        time.sleep(1)
        from polaris import polaris
        polaris()
    elif user == '3':
        time.sleep(1)
        from gtbank import gt
        gt()
    else:
        print('Invalid input')


def deposit():
    user = input("""
    1. Deposit to GTBank
    2. Deposit to Polaris
    0. Back
    >>> """)
    if user == '1':
        from gtbank import deposit_gtb
        deposit_gtb()
    elif user == '2':
        from polaris import deposit_pol
        deposit_pol()
    elif user == '0':
        time.sleep(1)
        welcome()
    else:
        print('Invalid input')
welcome()