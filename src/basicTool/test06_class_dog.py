class Dog():
    """模拟小狗的简单尝试"""
    def __init__(self,name,age):
        """初始化属性name,age"""
        self.name=name
        self.age=age
    def sit(self):
        """小狗蹲下"""
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        """小狗打滚"""
        print(f"{self.name} rolled over")

my_dog=Dog('xiaobai',12)
# print(f'My dog\'s name is {my_dog.name}.')
# print(f'My dog is {my_dog.age} years old')
my_dog.sit()
my_dog.roll_over()

