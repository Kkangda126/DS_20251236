class Inventory:
    stock= 0
    def __init__(self):
        self.__stock = 0
        print("새 상품이 등록 되었습니다.")

    def get_stock(self):
        return self.__stock

    def set_stock(self, amount):
        if amount >= 0:
            self.__stock = amount
        else:
            print("재고는 음수가 될 수 없습니다.")

    def add_stock(self, amount):
        if amount > 0:
            self.__stock += amount
            print(f"{amount}개가 입고 되었습니다.")
        else:
            print("0보다 작은 수량을 입고할 수는 없습니다.")
        return self.__stock

    def remove_stock(self, amount):
        if 0 < amount <= self.__stock:
            self.__stock -= amount
            print(f"{amount}개가 출고되었습니다.")
        else:
            print(f"현재보다 많은 수량이므로 출고가 불가합니다.")
        return self.__stock
    

item1 = Inventory()
item1.add_stock(10)
item1.remove_stock(3)
print("현재 재고 수량:", item1.get_stock())

item1.set_stock(20)
print("수정된 재고 수량:", item1.get_stock())