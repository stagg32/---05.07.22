account_status = int(0)
account_status_add = int(0)
price = int(0)
goods = {}

def add_money(account_status):
    account_status_add = input("Введите сумму пополнения счета (целое число): ")
    account_status_add = int(account_status_add)
    account_status += account_status_add
    print(f'У Вас на счете: {account_status} рублей')
    return account_status

def buing(account_status, goods):
    x = input("Введите сумму покупки: ")
    price = int(x)
    if price > account_status:
        print("Недостаточно средств.")
    else:
        goods[input("Введите название товара - ")] = price
        account_status -= price
    return account_status, goods

def shopping_list(goods):
    for key, value in goods.items():
        print(f'{key} ---> {value} рублей')


while True:
    choice = input("Введите варианты действий: \n1.пополнить счет\n2.покупка\n3.история покупок\n4.выход\nВаш выбор - ")
    if choice == '1':
        account_status = add_money(account_status)
    elif choice == '2':
        account_status, goods = buing(account_status, goods)
    elif choice == '3':
        shopping_list(goods)
    elif choice == '4':
        print("До свидания!")
        break
    else:
        print("Неверный пункт меню.")










