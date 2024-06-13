class Mobile:
    def __init__(self,Brand,battery,ram,camera,price):
        self.Brand=Brand
        self.battery=battery
        self.ram=ram 
        self.camera=camera 
        self.price=price
    def show(self):
        print("Brand: ",self.Brand)
        print("battery: ",self.battery)
        print("ram: ",self.ram)
        print("camera: ",self.camera)
        print("Price: ",self.price)
        print('-----------------')
        
        
        
for i in range(3):  
    obj=Mobile('apple','2000mah','5gb','48mp','90000')
    obj.show()        
obj=Mobile('keyboard','2000mah','5gb','48mp','90000')
obj.show()        
        