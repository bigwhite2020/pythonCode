from basicTool.test06_class_car import Car
class ElectricCar(Car):
    """电动汽车"""
    def __init__(self,make,model,year):
        """初始化父类方法"""
        super().__init__(make,model,year)
        #设置电瓶容量初始值
        self.battery=Battery()

    # #新增方法
    # def describe_battery(self):
    #     """打印电瓶容量信息"""
    #     print(f"This car has a {self.battery_size} -kwh battery.")

    # #重写父类方法
    # def fill_gas_tank(self):
    #     """电动车没有油箱"""
    #     print("This car doesn't need a gas tank!")

class Battery:
    """电动汽车电瓶的信息"""
    def __init__(self,battery_size=75):
        """初始化电瓶的属性"""
        self.battery_size=battery_size

    def describe_battery(self):
        """打印电瓶容量信息"""
        print(f"This car has a {self.battery_size} -kwh battery.")
    def get_range(self):
        """打印电瓶的续航里程"""
        if self.battery_size==75:
            range=260
        elif self.battery_size==100:
            range=315
        print(f"This car can go about {range} miles on a full charge")

#创建ElecticCar实例，赋给变量my_tesla
my_tesla=ElectricCar('tesla','model s',2020)
#print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()