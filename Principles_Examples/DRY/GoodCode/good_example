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


def send_money(auth: dict, acc_no: str, money) -> None:
    for no in users:
        if no['account_no'] == acc_no:
            withdraw_money(auth, money) # Here, we use the existing functions so that we don't repeat ourselves.
            add_money(no, money)
        else:
            print('No account found..!')


def add_money(auth: dict, money) -> None:
    if auth['additional_balance'] < 1000:
        auth.update({'additional_balance': auth['additional_balance'] + money})
        if auth['additional_balance'] > 1000:
            extra = auth['additional_balance'] - 1000
            auth.update({'balance': auth['balance'] + extra})
            auth.update({'additional_balance': auth['additional_balance'] - extra})
    else:
        auth.update({'balance': auth['balance'] + money})



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
