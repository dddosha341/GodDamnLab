from Worker import Worker, WorkerStatus
from Order import Order, Status
from Provider import Provider


class Storekeeper(Worker):

    def order_assembly(self, order: Order, provider: Provider):
        if (self.workerStatus == WorkerStatus.FREE):
            self.workerStatus = WorkerStatus.INPROGRESSWORK
            self.currentWork = order
            print(f'Работает над заказом ID: {order.orderId}')
            self.package(provider)

    def package(self, provider: Provider):
        self.currentWork.ChangeStatus(Status.INSTOCK)
        for item in self.currentWork.itemList:
            provider.warehouse[item] -= 1
        self.currentWork = None
        print("Упаковал заказ")
        self.workerStatus = WorkerStatus.FREE

