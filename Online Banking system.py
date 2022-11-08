print('Welcome to bank of pradice')
balances=0
chances=5
while True:
    pin = int(input('Please input your password:'))
    if pin == (1234):
        print('You entered your password')
        userinput = int(input('Which type of service would you take?'))
        if userinput == 1:
            print('Your balances is: $', balances)
        if userinput == 2:
            print('How much would you like to withdrow:')
            wdamount = int(input())
            balances = balances - wdamount
            if balances <= 0:
                print('Balance is unableable .Please cheak your balance and retry again')
        if userinput == 3:
            sendnum = int(input('Please input reciever account number:'))
            sendamt = int(input('Amount:'))
            sendpsd = int(input('Enter your password:'))
            if sendpsd==pin:
                print(f'Your sending amount ${sendamt} sucessfully send')
                balances=balances-sendamt
                if balances<= sendamt:
                    print(f'Your balances is less then ${balances}')
            else:
                print('Incorrect password!')
        if userinput == 4:
            ciamt=int(input("How much would you like to cash in:"))
            cibank=int(input('Please input your bank account number:'))
            cipin=int(input('Inter bank ac password:'))
            print('sucessfully cash in!')
            balances=balances+ciamt
            continue
    else:
        print('Invaid Password')
        if pin != (1234):
            chances = chances - 1
            if chances <= 0:
                print('no more tries')
                break



