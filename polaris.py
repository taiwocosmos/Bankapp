import time
import random
import mysql.connector as connection
myconn = connection.connect(host = '127.0.0.1', user = 'root', passwd = 'Oluwadamilola99$$', database = 'bank')
cursor = myconn.cursor()
def polaris():
    user = input("""
    Polaris Online Banking
    1. Log in
    2. Create account
    0. Back
    >>> """)
    if user == '1':
        time.sleep(2)
        p_login()
    elif user == '2':
        time.sleep(2)
        p_create_new()
    elif user == '0':
        time.sleep(2)
        from bankapp import welcome
        welcome()
    else:
        print('Invalid input')

def p_create_new():
    print("""
    REGISTER NEW ACCOUNT

    Enter your information >>""")
    val = []
    info = ('First_Name', 'Middle_Name', 'Last_Name', 'Age', 'Gender', 'Email', 'BVN', 'acc_number', 'balance', 'passwd', 'pin')
    querry = 'insert into polaris(First_name, Middle_name, Last_name, Age, Gender, Email, BVN, acc_number, balance, passwd, pin) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    for x in range(11):
        if info[x] == 'BVN':
            bInfo = random.randint(25654, 29231)
        elif info[x] == 'acc_number':
            bInfo = random.randint(9316021401, 9316092509)
        elif info[x] == 'balance':
            bInfo = 0
        else:
             bInfo = input(f'Enter your {info[x]}: ')
        val.append(bInfo)
    cursor.execute(querry, val)
    myconn.commit()
    time.sleep(2)
    print(f'Dear {val[0]} your Account Number is {val[7]}')
    time.sleep(2)
    p_login()

def p_login():
    global username
    global passwrd
    username = input("""
    LOG IN ACCOUNT
    
    Email >> """)
    passwrd = input("""
    Password >> """)
    val = (username, passwrd)
    querry = 'select * from polaris where Email = %s and passwd = %s'
    cursor.execute(querry, val)
    result = cursor.fetchone()
    if result:
        time.sleep(1)
        print('Processing>>>')
        time.sleep(2)
        print('LOG IN SUCCESSFUL')
        time.sleep(1)
        operation()
    else:
        print('Invalid Username or Password')
        time.sleep(1)
        p_login()

def operation():
    user = input("""
    1. Send money
    2. Buy Data/Airtime
    0. Logout
    >>> """)
    if user == '1':
        transfer()
    elif user == '2':
        data_airtime()
    elif user == '0':
        time.sleep(2)
        print('Logout Successfully')
        time.sleep(1)
        polaris()
    else:
        print('Invalid input')
        operation()

def transfer():
    user = input("""
    1. Transfer Polaris
    2. Transfer GTbank
    0. Back
    >>> """)
    if user == '1':
        time.sleep(1)
        polariss()
    elif user == '2':
        time.sleep(1)
        polaris_to_gtb()
    elif user == '0':
        time.sleep(1)
        operation()
    else:
        print('Invalid input')
        transfer()

def polariss():
    user = (input('ACCOUNT NUMBER >> '))
    while len(user) != 10:
        print('Invalid Account number; Acc number must be 10 digits')
        user = (input('ACCOUNT NUMBER >> '))
    amount = float(input('AMOUNT >> '))
    val = (user, )
    querry = 'select * from polaris where acc_number = %s'
    cursor.execute(querry, val)
    result = cursor.fetchone()
    if result:
        time.sleep(1)
        print(f'Confirm Amount N{amount} Beneficiary name {result[0]} {result[1]} {result[2]}')
        time.sleep(1)
        pin = input('Enter 4 digit pin >> ')
        val = (pin, )
        querry = 'select * from polaris where pin = %s'
        cursor.execute(querry, val)
        result2 = cursor.fetchone()
        if result2:
            time.sleep(1)
            print('PROCESSING >> ')
            if (result2[8] != 0) and (result2[8] > amount): 
                time.sleep(2)
                print('Transfer Successful >>')
            else:
                time.sleep(2)
                print('Insufficient Fund')
        else:
            print('Invalid PIN')
        newBalance = (result[8] + amount)
        val = (newBalance, user)
        querry = 'update polaris set balance = %s where acc_number = %s'
        cursor.execute(querry, val)
        myconn.commit()
        sender_balance = (result2[8] - amount)
        val_ = (sender_balance, pin)
        querry = 'update polaris set balance =%s where pin =%s'
        cursor.execute(querry, val_)
        myconn.commit()
    time.sleep(1)
    nextt = input("""
    1. Perform another Transaction
    2. Log out 
    >>> """)
    if nextt == '1':
        operation()
    elif nextt == '2':
        time.sleep(2)
        print('Log out Successful')
    else:
        print('Invalid input')

def polaris_to_gtb():
    acc = input('ACCOUNT NUMBER >> ')
    while len(acc) != 10:
        print('Invalid Account number; Acc number must be 10 digits')
        acc = input('ACCOUNT NUMBER >> ')
    amount = int(input('AMOUNT >> '))
    val = (acc, )
    querry = 'select * from gtb where acc_number =%s'
    cursor.execute(querry, val)
    result = cursor.fetchone()
    if result:
        time.sleep(1)
        print(f'Confirm Amount N{amount}, Beneficiary name {result[0]} {result[1]} {result[2]}')
        time.sleep(1)
        pin = input('Enter 4 digit PIN >> ')
        val = (pin, )
        querry = 'select * from polaris where pin =%s'
        cursor.execute(querry, val)
        result2 = cursor.fetchone()
        if result2:
            time.sleep(1)
            print('Processing >>')
            if (result2[8] != 0) and (result2[8] > amount):
                time.sleep(2)
                print('Transfer Successful')
            else:
                time.sleep(2)
                print('Insufficient Fund')
        else:
            print('Invalid PIN')
        polbalance = (result2[8] - amount)
        val = (polbalance, pin)
        querry = 'update polaris set balance =%s where pin =%s'
        cursor.execute(querry, val)
        myconn.commit()
        gtbalance = (result[8] + amount)
        val = (gtbalance, acc)
        querry = 'update gtb set balance =%s where acc_number =%s'
        cursor.execute(querry, val)
        myconn.commit()
        time.sleep(1)
    nextt = input("""
    1. Perform another Transaction
    2. Log out 
    >>> """)
    if nextt == '1':
        operation()
    elif nextt == '2':
        time.sleep(2)
        print('Log out Successful')
    else:
        print('Invalid input')

def data_airtime():
    user = input("""
    1. Airtime
    2. Data
    >>> """)
    if user == '1':
        phone = input('Phone Number >> ')
        amount = int(input('Amount >> '))
        while len(phone) != 11:
            print('Phone number must be 11 digits')
            phone = input('Phone Number >> ')
        if phone.startswith(('0806', '0803', '0814', '0706', '0703', '0903')):
            number = 'MTN'
            print(f'Recharge {number} {phone} Airtime amount of N{amount}')
        elif phone.startswith(('0802', '0904', '0812', '0708', '0808')):
            number = 'AIRTEL'
            print(f'Recharge {number} {phone} Airtime amount of N{amount}')
        elif phone.startswith(('0805', '0905', '0815', '0705')):
            number = 'GLO'
            print(f'Recharge {number} {phone} Airtime amount of N{amount}')
        else:
            number = 'Unknown number'
        time.sleep(1)
        pn = input('PIN >> ')
        val = (pn, )
        querry = 'select * from polaris where pin = %s'
        cursor.execute(querry, val)
        result = cursor.fetchone()
        if result:
            time.sleep(1)
            print('Processing >>>')
            if (result[8] != 0) and (result[8] > amount):
                time.sleep(2)
                print('Transaction Successful')
            else:
                time.sleep(2)
                print('Insufficient Fund')
        else:
            print('Wrong PIN')
            time.sleep(1)
            data_airtime()
        newB = (result[8] - amount)
        val2 = (newB, pn)
        querry = 'update polaris set balance =%s where pin =%s'
        cursor.execute(querry, val2)
        myconn.commit()
    elif user == '2':
        phn = input('Phone number >> ')
        while len(phn) != 11:
            print('Phone number must be 11 digits')
            phn = input('Phone number >> ')
        if phn.startswith(('0806', '0803', '0814', '0706', '0703', '0903')):
            numb = 'MTN'
            m = input("""
            1. N1,000 for 1.5GB
            2. N1200 for 2GB
            3. N1,500 for 3GB
            4. N2,000 for 4.5GB
            >>> """)
            if m == '1':
                print(f'Recharge {numb} {phn} 1.5GB for N1000')
            elif m =='2':
                print(f'Recharge {numb} {phn} 2GB for N1200')
            elif m == '3':
                print(f'Rechare {numb} {phn} 3GB for N1500')
            elif m == '4':
                print(f'Recharge {numb} {phn} 4.5GB for N2000')
            else:
                print('Invalid input') 
        elif phn.startswith(('0802', '0904', '0812', '0708', '0808')):
            number = 'AIRTEL'
            m = input("""
            1. N500 for 1.5GB
            2. N1000 for 2GB
            3. N2000 for 3GB
            4. N2,500 for 4.5GB
            >>> """)
            if m == '1':
                print(f'Recharge {numb} {phn} 1.5GB for N500')
            elif m =='2':
                print(f'Recharge {numb} {phn} 2GB for N1500')
            elif m == '3':
                print(f'Rechare {numb} {phn} 3GB for N2000')
            elif m == '4':
                print(f'Recharge {numb} {phn} 4.5GB for N2500')
            else:
                print('Invalid input') 
        elif phn.startswith(('0805', '0905', '0815', '0705')):
            number = 'GLO'
            m = input("""
            1. N1,500 for 2GB
            2. N2000 for 3GB
            3. N2,500 for 5GB
            4. N3,000 for 7GB
            >>> """)
            if m == '1':
                print(f'Recharge {numb} {phn} 2GB for N1500')
            elif m =='2':
                print(f'Recharge {numb} {phn} 3GB for N2000')
            elif m == '3':
                print(f'Rechare {numb} {phn} 5GB for N2500')
            elif m == '4':
                print(f'Recharge {numb} {phn} 7GB for N3000')
            else:
                print('Invalid input') 
        else:
            number = 'Unknown number'
        time.sleep(1)
        pn = input('PIN >> ')
        val = (pn, )
        querry = 'select * from polaris where pin = %s'
        cursor.execute(querry, val)
        result2 = cursor.fetchone()
        if result2:
            time.sleep(1)
            print('Processing >>>')
            if (result2[8] != 0) and (result2[8] > 5000):
                time.sleep(2)
                print('Transaction Successful')
            else:
                print('Insufficient Fund')
        else:
            print('Wrong PIN')
            time.sleep(1)
            data_airtime()

def deposit_pol():
    user = input('ACCOUNT NUMBER >> ')
    user2 = int(input('AMOUNT >> '))
    val = (user, )
    querry = 'select * from polaris where acc_number = %s'
    cursor.execute(querry, val)
    result = cursor.fetchone()
    if result:
        time.sleep(2)
        print(f'Confrim Amount N{user2} Beneficiary name {result[0]} {result[1]} {result[2]}')
        time.sleep(3)
        print('Transaction Successful')
        newBalance = (result[8] + user2)
        val = (newBalance, user)
        querry = 'update polaris set balance = %s where acc_number = %s'
        cursor.execute(querry, val)
        myconn.commit()