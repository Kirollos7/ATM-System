# Project 1
# Data  10 Users Name, Balance , Pin Code
# Electric Company
import time
Users = [{'Name' : 'Kirollos Noshy' , 'Balance' : 10500 , 'PinCode' : 2468} ,
         {'Name' : 'Mina Mousa' ,     'Balance' : 2050 ,  'PinCode' : 1234} ,
         {'Name' : 'Selvana Hany' ,   'Balance' : 1000 ,  'PinCode' : 8040} ,
         {'Name' : 'Yostina Emad' ,   'Balance' : 52555 , 'PinCode' : 9990} ,
         {'Name' : 'Mariam Kamel' ,   'Balance' : 6600 ,  'PinCode' : 8950} ,
         {'Name' : 'Romany Bekhit' ,  'Balance' : 89500 , 'PinCode' : 8000} ,
         {'Name' : 'Veronica Nosyi' , 'Balance' : 500 ,   'PinCode' : 7800} ,
         {'Name' : 'Gamel Fawzy' ,    'Balance' : 6250 ,  'PinCode' : 9560} ,
         {'Name' : 'Emad Hany' ,      'Balance' : 460 ,   'PinCode' : 7480} ,
         {'Name' : 'Abanoub Adel' ,   'Balance' : 7120 ,  'PinCode' : 6250}]


CurrentUser = {}
cPinCode = 0



def Load(t):
    for i in range(0,t):
        print('\rLoading' + '.'*i , end='')
        time.sleep(1)



def IntiialScreen():
    global cPinCode
    global CurrentUser
    found = False
    Load(3)
    print('\r##############################################################')
    print('#                 Welcome To OLearning ATM                   #')
    print('#                                                            #')
    print('#                                                            #')
    print('#              Please Enter Your Pin Code 4-Digit.           #')
    cPinCode = int(input('                               '))
    print('#                                                            #')
    print('#                                                            #')
    print('##############################################################')
    for user in Users:
        if user['PinCode'] == cPinCode:
            cPinCode = user
            found = True
    if found:
        SelectScreen()
    else:
        ErrorScreen()

    return



def ErrorScreen():
    #Load(2)
    print('\r##############################################################')
    print('#                 Welcome To OLearning ATM                   #')
    print('#                                                            #')
    print('#                                                            #')
    print('#       Error! in Your Pin Code Please Try Again!            #')
    print('#              WARING You Have Just 3 Times.                 #')
    print('#                                                            #')
    print('#                                                            #')
    print('##############################################################')

    Load(4)
    IntiialScreen()

    return



def SelectScreen():
    global op
    Load(3)
    print('\r##############################################################')
    print('#                 Welcome To OLearning ATM                   #')
    print('#                 Hi ',cPinCode['Name'],'                    #')
    print('#                                                            #')
    print('#  1- Cash Withdrawal            2- Balance Inquiry          #')
    print('#  3- Transfer                   4- Bill Payment             #')
    print('#  5- Setting                    6- EXit                     #')
    print('#                   7- Home Page                             #')
    print('#           Enter Required Operation [1,2,3,4,5,6]           #')
    op = int(input('                            '))
    print('#                                                            #')
    print('##############################################################')
    if op == 1:
        CashWithdrawal()
    elif op == 2:
        BalanceInquiry()
    elif op == 3:
        Transfer()
    elif op == 4:
        BillPayment()
    elif op == 5:
        Setting()
    elif op == 6:
        EXit()
    elif op == 7:
        IntiialScreen()
    else:
        Error()
    Load(4)

    return


def Error():
    print('\r##############################################################')
    print('#                 Welcome To OLearning ATM                   #')
    print('#                                                            #')
    print('#                                                            #')
    print('#       Error! in Your Selection Please Try Again!           #')
    print('#                                                            #')
    print('#                                                            #')
    print('#                                                            #')
    print('##############################################################')
    Load(4)
    SelectScreen()

    return


def CashWithdrawal():
    global cPinCode
    print('\r##############################################################')
    print('#                 Welcome To OLearning ATM                   #')
    print('#                                                            #')
    print('#               Please Insert Required Amount                #')
    print('#                                                            #')
    print('#                                                            #')
    amount = int(input('                         '))
    print('#                                                            #')
    print('##############################################################')

    if amount <= cPinCode['Balance']:
        cPinCode['Balance'] = cPinCode['Balance'] - amount
        BalanceInquiry()
    else:
        errorF()

    return


def errorF():
    print('\r##############################################################')
    print('#                 Welcome To OLearning ATM                   #')
    print('#                                                            #')
    print('#               Sorry You Don`t Have Balance!                #')
    print('#          Please Try Again And Enter a less Money.          #')
    print('#                                                            #')
    print('#                                                            #')
    print('#                                                            #')
    print('##############################################################')

    Load(5)
    CashWithdrawal()

    return


def BalanceInquiry():
    print('\r##############################################################')
    print('#                 Welcome To OLearning ATM                   #')
    print('#                                                            #')
    print('#              Balance = ',cPinCode['Balance'],'$            #')
    print('#                                                            #')
    print('#                                                            #')
    print('#                                                            #')
    print('#                                                            #')
    print('##############################################################')

    Load(6)
    SelectScreen()
    return



def Transfer():
    global cPinCode
    global  name
    print('\r##############################################################')
    print('#                 Welcome To OLearning ATM                   #')
    print('#                                                            #')
    print('#               Please Insert Required Amount                #')
    print('#                                                            #')
    print('#                                                            #')
    amount = int(input('                         '))
    name   =  input('         Enter The Person Name :\t')
    print('#                                                            #')
    print('##############################################################')

    if amount <= cPinCode['Balance']:
        cPinCode['Balance'] = cPinCode['Balance'] - amount
        BalanceInquiry()
    else:
        errorF()
    if name == cPinCode['Name']:
        cPinCode['Balance'] = cPinCode['Balance'] - amount
        BalanceInquiry()
    else:
        errorF()

    return


def BillPayment():
    global cPinCode
    global name
    print('\r##############################################################')
    print('#                 Welcome To OLearning ATM                   #')
    print('#                      Bill Payment                          #')
    print('#               Please Insert Required Amount                #')
    print('#                                                            #')
    print('#                                                            #')
    amount = int(input('                         '))
    name = input('         Enter The Company Name :\t')
    print('#                                                            #')
    print('##############################################################')

    if amount <= cPinCode['Balance']:
        cPinCode['Balance'] = cPinCode['Balance'] - amount
        BalanceInquiry()
    else:
        errorF()


    return



def Setting():
    global Choice
    print('\r##############################################################')
    print('#                 Welcome To OLearning ATM                   #')
    print('#                    Choice from 1 to 3                      #')
    print('#                                                            #')
    print('#     1- Change Data                  2- Change Pin Code     #')
    print('#                     3- Contact US                          #')
    print('#                                                            #')
    Choice = int(input('                            '))
    print('#                                                            #')
    print('##############################################################')
    if Choice == 1:
        ChangeData()
    elif Choice == 2:
        CHPIN()
    elif Choice == 3:
        Contact()

    else:
        Load(4)
        Error()
        Load(2)
        SelectScreen()
    return


def Contact():
    print('\r#################################################################')
    print('#                 Welcome To OLearning ATM                      #')
    print('#                       Contact US                              #')
    print('#                                                               #')
    print('#                                                               #')
    print('#   Mobile: +201280255072     https://www.OLreaning.com         #')
    print('#   TEL : 0224392747          Work: Kerlis.Noshy@oi.edu.eg      #')
    print('#   Fax : 326588              E-mail: kirollosnoshi@gmail.com   #')
    print('#################################################################')
    Load(8)
    SelectScreen()

    return

def CHPIN():
    print('\r#################################################################')
    print('#                 Welcome To OLearning ATM                      #')
    print('#                       Change Pin Code                         #')
    print('#                                                               #')
    print('#                                                               #')
    print('#                         Coming Soon                           #')
    print('#                                                               #')
    print('#                                                               #')
    print('#################################################################')
    Load(10)
    SelectScreen()
    return

def ChangeData():
    print('\r#################################################################')
    print('#                 Welcome To OLearning ATM                      #')
    print('#                       Change Data                             #')
    print('#                                                               #')
    print('#                                                               #')
    print('#                        Coming Soon                            #')
    print('#                                                               #')
    print('#                                                               #')
    print('#################################################################')
    Load(10)
    SelectScreen()
    return


def EXit():
    exit()
    return



IntiialScreen()
