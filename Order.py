from dataclasses import dataclass
from enum import Enum
from Item import Item
import uuid


class Status(Enum):
    PROCESSING = 0  # обработка
    ACCEPTED = 1  # приянт
    INSTOCK = 2  # сборка на складе
    ONTHEWAY = 3  # в пути
    INPOINT = 4  # в пунткте
    RECEIVED = 5  # получен
    CANCEL = 6  # отменен

@dataclass
class Order:
    orderId: str
    status: Status
    itemList: list[Item]
    timeCreation: str
    address: str

    # collector: User

    def __init__(self, status: Status, itemList: list[Item], timeCreation: str, adress):
        self.orderId = uuid.uuid1()
        self.status = status
        self.itemList = itemList
        self.timeCreation = timeCreation
        self.address = adress
        # self.collector = collector

    def ChangeStatus(self, status: Status):
        self.status = status

# Что находится в заказе? Статус доставки, список товаров, время создания-время доставки, кто собирал-доставлял