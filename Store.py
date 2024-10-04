from Item import Item
# from User import User
from Order import Order, Status
from Courier import Courier
from Storekeeper import Storekeeper
from Provider import Provider
from Worker import WorkerStatus, Worker


class Store:
    name: str
    # productList: list[Item]
    courierList: list[Courier]
    storekeeperList: list[Storekeeper]
    providerList: list[Provider]
    # userList:list[User]
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
            if (flag):
                self.set_storekeeper(order, provider)
                self.set_courier(order)
                break
        if (not (flag)):
            print(f'Заказ {order.orderId} был отменен')
            order.status = Status.CANCEL

    # send_request - отправить заказ для провайдера (что привезти)

    def take_order(self, order: Order):
        flag = True
        for provaider in self.providerList:
            if provaider.CheckWarehouse(order):
                order.status = Status.ACCEPTED
                break
        if order.status != Status.ACCEPTED:
            order.status = Status.CANCEL
            flag = False
        self.orderList.append(order)
        return flag
    # принять заказ и начать его обрабатывать

    def set_courier(self, order: Order):
        for courier in self.courierList:
            if courier.workerStatus == WorkerStatus.FREE:
                print(f'Заказ {order.orderId} был передан курьеру')
                courier.take_order(order)
                break

    # дать заказу курьера

    def set_storekeeper(self, order: Order, provider: Provider):
        for storekeeper in self.storekeeperList:
            if storekeeper.workerStatus == WorkerStatus.FREE:
                print(f'Заказ {order.orderId} был передан упаковщику')
                storekeeper.order_assembly(order, provider)
                break

    def get_worker(self, worker: Worker):
        if (type(worker) == Courier):
            self.courierList.append(worker)
        if (type(worker) == Storekeeper):
            self.storekeeperList.append(worker)

    def get_provider(self, provider: Provider):
        self.providerList.append(provider)

    def update(self, curTime: int):
        for worker in self.courierList:
            if (worker.workerStatus == WorkerStatus.NOTWORKING):
                print('Курьер прибыл смену')
                worker.get_shift(curTime)
            elif (worker.workerStatus == WorkerStatus.FREE
                  and worker.timeEndWork <= curTime):
                print('Курьер закончил смену')
                worker.end_shift()

        for worker in self.storekeeperList:
            if (worker.workerStatus == WorkerStatus.NOTWORKING):
                print('Кладовщик прибыл смену')
                worker.get_shift(curTime)
            elif (worker.workerStatus == WorkerStatus.FREE
                  and worker.timeEndWork <= curTime):
                print('Кладовщик закончил смену')
                worker.end_shift()

        for order in self.orderList:
            if (order.status == Status.ACCEPTED):
                self.send_request(order)
            if (order.status == Status.RECEIVED):
                self.orderList.remove(order)

    # взять работника к себе и дать ему смену
    def getListprovider(self):
        if (len(self.providerList) == 0):
            print(f'У магазина нет поставщиков')
            return False
        for i in range(len(self.providerList)):
            print(f'{i + 1}: Provider name - {self.providerList[i].name}')
        index = int(input('Введите номер нужного провайдера: '))
        if 0 < index <= len(self.providerList):
            return self.providerList[index - 1]
        else:
            print('Неправильный номер поставщика')
            return False

    def Catalog(self):
        index1 = 1
        for provider in self.providerList:
            print('-' * 20)
            print(f'{index1}: Товары {provider.name}')
            index2 = 1
            for item in provider.warehouse.keys():
                print(f'  {item.name}: количество {provider.warehouse[item]}')
                index2 += 1
            index1 += 1

    def RetItem(self, name: str):
        for provider in self.providerList:
            for item in provider.warehouse.keys():
                if (item.name == name):
                    return item
        return False