from dataclasses import dataclass

@dataclass
class Item:
    idItemStorage: str
    name: str
    costPrice: float

    def __init__ (self, idItemStorage: str, name: str, costPrice: float):
        self.idItemStorage = idItemStorage
        self.name = name
        self.costPrice = float(costPrice)

    def __hash__(self):
        return hash(self.name)

# Что должно быть? Id внутри системы складов, id внутри системы поставщика, название, себестоимость

