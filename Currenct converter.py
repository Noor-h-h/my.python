import os 
import time

dollar="""||====================================================================||
||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
||(100)==================| FEDERAL RESERVE NOTE |================(100)||
||\\$//        ~         '------========--------'                \\$//||
||<< /        /$\              // ____ \\                         \ >>||
||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
||<<|        \\ //           || <||  >\  ||                        |>>||
||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
||>>|  12                     *\\/___\_//*   1989                  |<<||
||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\||
||(100)===================  ONE HUNDRED DOLLARS =================(100)||
||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
||====================================================================||


"""
#نضيف متغير دولار الى القاموس حتى كلما نستدعي يطلع 
exchange_rates={
    "":dollar,
    "USD":1.0,
    "EUR":0.8,
    "EGP":30.9,
    "RMB":6.5,
}

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def display_rates():
    print("Welcome to currenct converter ")
#استخدمت حلقه الفور حتى تنطبع الحلقات بالترتيب حتى اي تعديل مستقبلي للعمله 
#اعدلها فقط من فوك بدون حاجه اي تعديل اضافي 
    for currency in exchange_rates:
        print(f"{currency} : {exchange_rates[currency]}")

def currency_converter():
    clear_screen()
    display_rates()


#يدخل المستخدم رمز العملة ويحوله لاحرف كبيرة لتوحيد المقارنات لاحقا
#نخليه برا الللوب لان هذا قرار ميتكرر الا اذا بدا عملية تحول جديده بالكامل 
    from_currency=input("\n choose a currency to convert from : ").upper()

    while True:
      amount=float(input("Enter the amount :"))
      confirmation=input(f"\n you entered {amount} and {from_currency} do you confirme?").upper()
#اذا وضع المستخدم حرف واي تنكسر الحلقه وتكمل الداله واذا ما خله واي ينعاد طلع المبلغ 
      if confirmation =='Y':
          break

    clear_screen()
    display_rates()


#يطلب العملة اللي يريد يحول الها 
    to_currency=input("\n Choose a currency to convert to : "). upper()
     
    print("check waite 2 sec")
    time.sleep(2)
    print(f"Chacking for {to_currency}s test rates available ....Please wait ")
    time.sleep(3)
    print(f"Getting a discount price for {from_currency}....Please wait")
    time.sleep(2)

    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        
        print("Invilid currency ,conversion canclled ")
        time.sleep(2)
        currency_converter()

    new_rate=exchange_rates[to_currency]/ exchange_rates[from_currency]

    converted_amount=amount*new_rate

    clear_screen()
    print(f"Preparing the deal from {from_currency} to {to_currency}...please wait \n")
    time.sleep(2)
    print(f"{amount}{from_currency} is equal to {round(converted_amount,2)}{to_currency}")
    time.sleep(2)

    accept_tranction=input(f"\n Do you accept this transction (y/n)").upper()

    if accept_tranction =='y':
        print("Transction successfull")
    else:
        print("Transction cancelled")
    
    another_convertion=input("\n Do you want to perfers another conversion (y/n):").upper()

    if another_convertion=='y':
        currency_converter()

    else:
        print("Thanks fo using the currency converter")

currency_converter()