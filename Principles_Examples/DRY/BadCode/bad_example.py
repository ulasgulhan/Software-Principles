burak_account = {
    'account_no': '12345',
    'full_name': 'Burak Yılmaz',
    'user_name': 'beast',
    'password': '123',
    'balance': 3000,
    'additional_balance': 1000
}

hakan_account = {
    'account_no': '98765',
    'full_name': 'Hakan Yılmaz',
    'user_name': 'bear',
    'password': '123',
    'balance': 5000,
    'additional_balance': 1000
}

ipek_account = {
    'account_no': '56789',
    'full_name': 'İpek Yılmaz',
    'user_name': 'keko',
    'password': '123',
    'balance': 8000,
    'additional_balance': 1000
}

users = [burak_account, hakan_account, ipek_account]


# In this function, we are using codes that was previously written.
def send_money(sender_account: dict, reciver_account_no: str, amount: int) -> None: 
    for user in users: 
        if user['account_no'] == reciver_account_no:
            if sender_account['balance'] >= amount:
                sender_account['balance'] -= amount
                user['balance'] += amount
            else:
                total_balance = sender_account['balance'] + sender_account['additional_balance']
                if total_balance >= amount:
                    use_additional_balance = input('Insufficent balance. Do you want to use additional balance? ("yes" or "no") ').lower()
                    if use_additional_balance == 'yes':
                        amount_used_additional_balance = amount - sender_account['balance']
                        sender_account['balance'] = 0
                        sender_account['additional_balance'] -= amount_used_additional_balance
                        user['balance'] += amount
                    elif use_additional_balance == 'no':
                        print('Transaction has been cancaled..!')

                    else:
                        print('Please type valid answer like "yes" or "no"')
                else:
                    print('Insufficent balance. Transaction has been cancaled..!')


def add_money(account: dict, amount: int) -> None:
    account['balance'] += amount
    if account['additional_balance'] < 1000:
        transfered_amount = 1000 - account['additional_balance']
        account['balance'] -= transfered_amount
        account['additional_balance'] += transfered_amount


def withdraw_money(account: dict, money: int) -> None:
    if money <= account['balance']:
        account.update({'balance': account['balance'] - money})
    elif money <= account['balance'] + account['additional_balance']:
        question = input('Do you want to use additional balance?: ')
        if question == 'yes':
            account.update({'balance': account['balance'] - money})
            account.update({'additional_balance': account['balance'] + account['additional_balance']})
            account.update({'balance': account['balance'] * 0})
        elif question == 'no':
            print('Process closing')
        else:
            print('This is a yes or no question')
    else:
        print('Not enough money')
