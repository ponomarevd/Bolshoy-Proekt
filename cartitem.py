from product import Product 

class cartitem: 
    def __init__(self, product, qty): 
        self.__product = product 
        self.__qty = qty

    @property 
    def product(self): 
        return self.__product

    @property 
    def qty(self): 
        return self.__qty 
    
    @qty.setter 
    def qty(self, qty): 
        if qty > 0: 
            self.__qty = qty 
        else: 
            print("Некорректно выбрано значение")
    