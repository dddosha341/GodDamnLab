from Item import Item
from Order import Order, Status
from Courier import Courier
from Storekeeper import Storekeeper
from Provider import Provider
from Worker import WorkerStatus
class Store:
    name: str
    storekeeperList: list[Storekeeper]
    providerList: list[Provider]
    orderList: list[Order]

    def __init__(self, name: str):
        self.name = name
        self.storekeeperList = list()
        self.providerList = list()
        self.orderList = list()

    def send_request(self, order: Order):
        # Упрощаем, убирая проверку на успех
        provider = self.providerList[0]  # Предполагаем, что есть только один поставщик
        self.set_storekeeper(order, provider)
        print(f'Заказ {order.orderId} был отправлен поставщику {provider.name}')

    def take_order(self, order: Order):
        provider = self.providerList[0]  # Предполагаем, что есть только один поставщик
        order.status = Status.ACCEPTED
        self.orderList.append(order)
        return True

    def set_storekeeper(self, order: Order, provider: Provider):
        for storekeeper in self.storekeeperList:
            if storekeeper.workerStatus == WorkerStatus.FREE:
                storekeeper.process_order(order, provider)
                break

    def getListprovider(self):
        if not self.providerList:
            print('У магазина нет поставщиков')
            return False
        provider = self.providerList[0]  # Один поставщик
        print(f'Provider name - {provider.name}')
        return provider

    def Catalog(self):
        provider = self.providerList[0]  # Один поставщик
        print(f'Товары {provider.name}')
        for item, quantity in provider.warehouse.items():
            print(f'  {item.name}: количество {quantity}')

    def RetItem(self, name: str):
        provider = self.providerList[0]  # Один поставщик
        for item in provider.warehouse.keys():
            if item.name == name:
                return item
        return False
