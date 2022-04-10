# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年04月08日
"""


class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_doometer(self):
        """打印一条指出汽车里程的消息"""
        print(f"This car has {self.odometer_reading} mile in it")

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


class Battery:
    """一次模拟点哦对那个汽车电瓶的简单尝试。"""

    def __init__(self, battery_size=75):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery_size}-KWh battery")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 75:
            r = 260
        elif self.battery_size == 100:
            r = 315
        print(f"This car can go about {r} miles on a full charge.")

    def upgrate_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100

class ElectricCar(Car):
    """电动汽车的独特之处。"""

    def __init__(self, make, model, year):
        """
        初始化父类的属性。
        再初始化电动汽车特有的属性。
        """
        super().__init__(make, model, year)
        self.battery = Battery()
    #     self.battery_size = 75
    # def describe_battery(self):
    #     """打印一条描述电池容量的消息。"""
    #     print(f"This car has a {self.battery_size}-KWh battery")


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrate_battery()
my_tesla.battery.get_range()

