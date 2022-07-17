# -*- coding: utf-8 -*-
"""
http://blog.csdn.net/chenghit
"""

# -*- coding: utf-8 -*-
"""
http://blog.csdn.net/chenghit
"""
import wx
app = wx.App()
#创建一个顶级窗口作为wx.Frame类的对象,设置窗体的大小
window = wx.Frame(None, title = "wxPython Frame", size = (300,200))
#将一个Panel对象放入框架中
panel = wx.Panel(window)
#添加一个StaticText对象以在窗口内的所需位置显示'Hello World'，并设置位置
label = wx.StaticText(panel, label = "Hello World", pos = (0,0))
#通过show（）方法激活框架窗口
window.Show(True)
#window.ShowFullScreen(True)
#输入Application对象的主事件循环
app.MainLoop()