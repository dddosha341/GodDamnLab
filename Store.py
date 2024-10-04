from Item import Item
from Order import Order, Status
from Courier import Courier
from Storekeeper import Storekeeper
from Provider import Provider
from Worker import WorkerStatus


class Store:
    name: str
    courierList: list[Courier]
    storekeeperList: list[Storekeeper]
    providerList: list[Provider]
    orderList: list[Order]

    def __init__(self, name: str):
        self.name = name
        self.courierList = list()
        self.storekeeperList = list()
        self.providerList = list()
        self.orderList = list()

    def send_request(self, order: Order):
        flag = False
        for provider in self.providerList:
            flag = provider.send_order(order)
            if flag:
                self.set_storekeeper(order, provider)
                self.set_courier(order)
                break
        if not flag:
            print(f'Заказ {order.orderId} был отменен')
            order.status = Status.CANCEL

    def take_order(self, order: Order):
        flag = True
        for provider in self.providerList:
            if provider.CheckWarehouse(order):
                order.status = Status.ACCEPTED
                break
        if order.status != Status.ACCEPTED:
            order.status = Status.CANCEL
            flag = False
        self.orderList.append(order)
        return flag

    def set_courier(self, order: Order):
        for courier in self.courierList:
            if courier.workerStatus == WorkerStatus.FREE:
                print(f'Заказ {order.orderId} был передан курьеру')
                courier.take_order(order)
                break

    def set_storekeeper(self, order: Order, provider: Provider):
        for storekeeper in self.storekeeperList:
            if storekeeper.workerStatus == WorkerStatus.FREE:
                storekeeper.process_order(order, provider)
                break

    def getListprovider(self):
        if not self.providerList:
            print('У магазина нет поставщиков')
            return False
        for i, provider in enumerate(self.providerList, 1):
            print(f'{i}: Provider name - {provider.name}')
        index = int(input('Введите номер нужного провайдера: '))
        if 0 < index <= len(self.providerList):
            return self.providerList[index - 1]
        else:
            print('Неправильный номер поставщика')
            return False

    def Catalog(self):
        for i, provider in enumerate(self.providerList, 1):
            print('-' * 20)
            print(f'{i}: Товары {provider.name}')
            for item, quantity in provider.warehouse.items():
                print(f'  {item.name}: количество {quantity}')

    def RetItem(self, name: str):
        for provider in self.providerList:
            for item in provider.warehouse.keys():
                if item.name == name:
                    return item
        return False
