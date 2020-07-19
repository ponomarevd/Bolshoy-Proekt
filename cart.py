from cartitem import cartitem 
from typing import List

class Cart: 
    __cartitems: List[cartitem] = []

    def AddProduct(self, product, qty = 1): 
        newProduct = cartitem(product, qty)
        if product.qty <= newProduct.product.stock and product.qty > 0: 
            self.__cartitems.append(newProduct)
        else: 
            print("Недостаточно товара на складе") 
        
    def removeProduct(self, productID):
        foundCartItem = next((i for i in self.__cartitems if i.product.id == productID), None)
        self.__cartitems.remove(foundCartItem)  
    
    def changeQty(self, productID, newQty):
        foundCartItem = next((i for i in self.__cartitems if i.product.id == productID), None)
        for i in self.__cartitems: 
            if newQty <= i.product.stock: 
                foundCartItem.qty = newQty 
            else: 
                print("Недостаточно товара на складе")

    def getTotalPrice(self):
        total = 0
        for cartitem in self.__cartitems: 
            if cartitem.product.stock >= cartitem.qty: 
                sum = cartitem.product.price * cartitem.qty   
                total = total + sum 
        return total
        
    def getReportData(self):
        result = []
        for item in self.__cartItems:
            result.append([item.product.id, item.qty])
        return result
