from Worker import Worker,WorkerStatus
from Order import Order
from Order import Status
class Courier(Worker):

    def take_order(self,order:Order):
        if(self.workerStatus == WorkerStatus.FREE):
            self.workerStatus = WorkerStatus.INPROGRESSWORK
            self.currentWork = order
            order.ChangeStatus(Status.ONTHEWAY)
            print(f'Доставляет заказ по адресу {order.address}')
            self.giveOrder()

    def giveOrder(self):
        self.currentWork.status = Status.INPOINT
        self.workerStatus = WorkerStatus.FREE
        print(f'Курьер Доставил заказ по адресу {self.currentWork.address}')
        self.currentWork = None






