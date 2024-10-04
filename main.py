from Courier import Courier
from Item import Item
import Order
from Provider import Provider
from Store import Store
from Storekeeper import Storekeeper
from User import User
import uuid

ozon = Store('OZON')
userlst = list()
time = 0
def Day():
    ozon.update(time)
    for user in userlst:
        user.take_order()
    pass
def Interfaсe(user: User):
    global time
    while True:
        time += 1
        time %= 24
        print('Действия: ')
        print('1 - Посмотреть каталог')
        print('2 - Добавить товар в корзину')
        print('3 - Удалить товар из корзины')
        print('4 - Посмотреть корзину')
        print('5 - Сделать заказ')
        print('6 - Изменить адресс доставки')
        print('7: Удалить корзину')
        print('8: Закинуть шекелей')
        n = int(input())
        match n:
            case 1:
                user.store.Catalog()
            case 2:
                name = input('Введите название предмета: ')
                item = user.store.RetItem(name)
                if (item != False):
                    n = int(input("Введите количество предметов"))
                    user.addCart(item, n)
                else:
                    print('Товара не существует')
            case 3:
                name = input('Введите название предмета: ')
                user.DeleteCart(name)
            case 4:
                user.PrintCart()
            case 5:
                if (len(user.cart) != 0):
                    if user.make_order():
                        print(f'Заказ с ID: {user.waitOrder[-1].orderId} был создан')
                else:
                    print('Корзина пустая, невозможно создать заказ')

            case 6:
                address = input('Введите адресс пользователя: ')
                user.setAdress(address)
            case 7:
                if (len(user.cart) != 0):
                    user.DeleteAllCart()
                    print('Корзина была очищена')
                else:
                    print('Корзина пустая')
            case 8:
                money = int(input('Сколько закинуть шекелейг: '))
                user.money += money
            case _:
                return


def AddProvider(provider: Provider):
    n = int(input('Введите количество предметов которые желаете добавить: '))
    lstItems = list()
    while n:
        ID = input(f'{n}: Введите индетификатор предмета: ')
        name = input(f'{n}:Введите название предмета: ')
        cost = input(f'{n}:Введите стоимость предмета: ')
        newItem = Item(ID, name, cost)
        count = int(input(f'{n}:Введите количество предмета: '))
        for i in range(count):
            lstItems.append(newItem)
        n -= 1
    provider.update_stocks(lstItems)

def menu():
    while True:
        print('Действия: ')
        print('1 - Добавить нового пользователя и выбрать как активного')
        print('2 - Добавить кладовщика')
        print('3 - Добавить курьера')
        print('4 - Добавить поставщика')
        print('5 - Добавить предметы поставщику')
        print('6 - Смоделировать день')
        n = int(input())
        match n:
            case 1:
                login = input('Введите логин пользователя: ')
                ID = uuid.uuid1()
                address = input('Введите адресс пользователя: ')
                newUser = User(login, ID, address, ozon)
                userlst.append(newUser)
                Interfaсe(newUser)
            case 2:
                newStoreKeeper = Storekeeper(6)
                ozon.get_worker(newStoreKeeper)
                print('Был добавлен кладовщика')
            case 3:
                newCourier = Courier(6)
                ozon.get_worker(newCourier)
                print('Был добавлен курьер')
            case 4:
                login = input('Введите название поставщика: ')
                newProvider = Provider(login)
                ozon.get_provider(newProvider)
            case 5:
                provider = ozon.getListprovider()
                if (provider != False):
                    AddProvider(provider)
            case 6:
                Day()
            case _:
                return
menu()










