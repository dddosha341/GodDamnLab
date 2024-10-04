from Item import Item
from Order import Order
from Order import Status
from Store import Store


class User:
    login: str
    ID: str
    cart: list[Item]
    money: int
    addres: str
    waitOrder: list[Order]
    store: Store

    def __init__(self, login: str, ID: str, addres: str, store: Store):
        self.login = login
        self.ID = ID
        self.addres = addres
        self.store = store
        self.money = 0
        self.cart = list()
        self.waitOrder = list()

    def SumCart(self):
        Sum = int()
        for item in self.cart:
            Sum += item.costPrice
        return Sum
    def make_order(self) -> Order:
        bfCart = self.cart.copy()
        createOrder = Order(Status.PROCESSING, bfCart, '11.12.2001', self.addres)
        if (self.money < self.SumCart()):
            print("Не хватает money")
            return False
        else:
            self.cart.clear()
            self.waitOrder.append(createOrder)
            return self.store.take_order(createOrder)

    def addCart(self, item: Item, n:int):
        for i in range(n):
            self.cart.append(item)

    def DeleteCart(self, index: str):
        for item in self.cart:
            if (index == item.name):
                print(f'Был удален {item.name} из корзины')
                self.cart.remove(item)
                return
        print(f'{index} не существует в корзине')

    def DeleteAllCart(self):
        self.cart.clear()

    def PrintCart(self):
        itemdct = dict.fromkeys(self.cart, 0)
        for item in self.cart:
            itemdct[item]+=1
        i = 1
        for item in itemdct.keys():
            print(f'{i} : {item.name} {itemdct[item]}')

    def take_order(self):
        for order in self.waitOrder:
            if order.status == Status.INPOINT:
                order.status = Status.RECEIVED
                print(f'Получил заказ с ID : {order.orderId}')
                self.waitOrder.remove(order)
            if (order.status == Status.CANCEL):
                self.waitOrder.remove(order)

    def setAdress(self, adress: str):
        self.addres = adress

    def setLogin(self, login: str):
        self.login = login