from Order import Order,Status
from Item import Item

class Provider: # поставщик

    name:str
    warehouse: dict[(Item,int)]

    def CheckWarehouse(self, order:Order):
        lst = dict()
        flag = True
        for item in order.itemList:
            if item in self.warehouse.keys():
                lst[item] = (order.itemList.count(item), self.warehouse[item])
            else:
                flag = False
                break
        if flag:
            print("Предметы из заказа | количесвто в заказе| количество на складе")
            for key in lst.keys():
                print(key, lst[key][0], lst[key][1])
            n = int(input("Если согласны на уменьшение товаров введите 1, иначе 0"))
            if n == 1:
                productlist = list()
                for key in lst.keys():
                    for i in range(min(lst[key][0], lst[key][1])):
                        productlist.append(key)
                order.itemList = productlist
            else:
                flag = False
        return flag

    def __init__(self,name:str):
        self.name = name
        self.warehouse = dict()
    def send_order(self,order:Order):
        flag = True
        for item in order.itemList:
            if not (item in self.warehouse.keys()) or order.itemList.count(item) > self.warehouse[item]: flag = False
        return flag
    def update_stocks(self,itemList:list[Item]):
        for item in itemList:
            if(item in self.warehouse.keys()): self.warehouse[item] += 1
            else: self.warehouse[item] = 1