#导入模块，使用模块中对应的函数
# import test04_function
# test04_function.make_pizza(13,'prpperono')
# test04_function.make_pizza(10,'prpperono','cheese','mushrooms')

#导入特定的函数
# from test04_function import make_pizza
# make_pizza(10,'prpperono','cheese','mushrooms')

#使用as给函数/模块指定别名
# from test04_function import make_pizza as mp
# mp(10,'prpperono','cheese','mushrooms')

#使用as给模块执行别名
import test04_function as pizza
pizza.make_pizza(10,'prpperono','cheese','mushrooms')

#导入模块中的所有函数
from test04_function import *