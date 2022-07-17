class Car:
    """汽车信息"""
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        #给默认值
        self.odometer_reading=3000
    def get_descriptive_name(self):
        """返回描述性信息"""
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """打印汽车的里程"""
        print(f"This car has {self.odometer_reading} miles on it.")
    #新增修改里程数的方法
    def update_odometer(self,mileage):
        """将里程表读数设置为指定值"""
        self.odometer_reading=mileage
    #新增方法
    def increment_odometer(self,miles):
        """将里程表读书增加指定的量"""
        self.odometer_reading+=miles

    #Car类新增方法：油箱
    def fill_gas_tank(self):
        print("This car needs a gas tank！")

# my_new_car=Car('audi','a4',2019)
# print(my_new_car.get_descriptive_name())
# # my_new_car.read_odometer()
# # my_new_car.odometer_reading=3000
# # my_new_car.read_odometer()
# #创建实例并条用方法
# my_new_car.update_odometer(50)
# my_new_car.read_odometer()
# #通过方法对属性值进行递增
# my_new_car.update_odometer(23_500)
# my_new_car.read_odometer()

