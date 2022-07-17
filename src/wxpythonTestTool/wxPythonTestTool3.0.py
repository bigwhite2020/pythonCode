# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
import base64
import hashlib
import wx
import wx.xrc
import time
import json


# last updateTime 2022/03/06
###########################################################################
## Class MyFrame
###########################################################################

class MyFrame( wx.Frame ):

    def __init__(self, parent):
        wx.Frame.__init__( self, parent, id=wx.ID_ANY, title=u"测试小工具3.0", pos=wx.DefaultPosition,
                           size=wx.Size( 421, 118 ), style=wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        gbSizer=wx.GridBagSizer( 0, 0 )
        gbSizer.SetFlexibleDirection( wx.BOTH )
        gbSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.button1=wx.Button( self, wx.ID_ANY, u"时间戳转换(1)", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer.Add( self.button1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.button2=wx.Button( self, wx.ID_ANY, u"json校验(2)", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer.Add( self.button2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.button3=wx.Button( self, wx.ID_ANY, u"常用加解密(3)", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer.Add( self.button3, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.button4=wx.Button( self, wx.ID_ANY, u"置顶便笺(4)", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer.Add( self.button4, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.button5=wx.Button( self, wx.ID_ANY, u"ext(5)", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer.Add( self.button5, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.button6=wx.Button( self, wx.ID_ANY, u"ext(6)", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer.Add( self.button6, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.button7=wx.Button( self, wx.ID_ANY, u"ext(7)", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer.Add( self.button7, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.button8=wx.Button( self, wx.ID_ANY, u"ext(8)", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer.Add( self.button8, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.SetSizer( gbSizer )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.button1.Bind( wx.EVT_BUTTON, self.fun1 )
        self.button2.Bind( wx.EVT_BUTTON, self.fun2 )
        self.button3.Bind( wx.EVT_BUTTON, self.fun3 )
        self.button4.Bind( wx.EVT_BUTTON, self.fun4 )
        self.button5.Bind( wx.EVT_BUTTON, self.fun5 )
        self.button6.Bind( wx.EVT_BUTTON, self.fun6 )
        self.button7.Bind( wx.EVT_BUTTON, self.fun7 )
        self.button8.Bind( wx.EVT_BUTTON, self.fun8 )

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class

    def fun1(self, event):
        # self.frame = wx.Frame1( None ,title="测试",size=(300,100),pos=(100,100))
        # self.frame.Show()
        main=MyFrame1( None )
        main.Show()
        # print( round( time.time() * 1000 ) )

    def fun2(self, event):
        # self.frame = wx.Frame2( None ,title="测试",size=(300,100),pos=(100,100))
        # self.frame.Show()
        main=MyFrame2( None )
        main.Show()

        # print(round( time.time() * 1000 ))
        # self.m_textCtrl1.SetValue( str( round( time.time() * 1000 ) ) )

    def fun3(self, event):
        main=MyFrame3( None )
        main.Show()

    def fun4(self, event):
        main=MyFrame4( None )
        main.Show()

    def fun5(self, event):
        event.Skip()

    def fun6(self, event):
        event.Skip()

    def fun7(self, event):
        event.Skip()

    def fun8(self, event):
        event.Skip()


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1( wx.Frame ):

    def __init__(self, parent):
        wx.Frame.__init__( self, parent, id=wx.ID_ANY, title=u"时间戳转换(1)", pos=wx.DefaultPosition,
                           size=wx.Size( 780, 300 ), style=wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        gbSizer1=wx.GridBagSizer( 0, 0 )
        gbSizer1.SetFlexibleDirection( wx.BOTH )
        gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        gbSizer1_1=wx.GridBagSizer( 0, 0 )
        gbSizer1_1.SetFlexibleDirection( wx.BOTH )
        gbSizer1_1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.button1_1_1=wx.Button( self, wx.ID_ANY, u"刷新当前时间戳与日期", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1_1.Add( self.button1_1_1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.textCtrl1_1_2=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1_1.Add( self.textCtrl1_1_2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.button1_1_3=wx.Button( self, wx.ID_ANY, u"复制", wx.DefaultPosition, wx.Size( 50, -1 ), 0 )
        gbSizer1_1.Add( self.button1_1_3, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.button1_1_4=wx.Button( self, wx.ID_ANY, u"清除", wx.DefaultPosition, wx.Size( 50, -1 ), 0 )
        gbSizer1_1.Add( self.button1_1_4, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gbSizer1.Add( gbSizer1_1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        gbSizer1_2=wx.GridBagSizer( 0, 0 )
        gbSizer1_2.SetFlexibleDirection( wx.BOTH )
        gbSizer1_2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.button1_2_1=wx.Button( self, wx.ID_ANY, u"转换日期格式为时间戳", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1_2.Add( self.button1_2_1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.textCtrl1_2_2=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125, -1 ), 0 )
        gbSizer1_2.Add( self.textCtrl1_2_2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.textCtrl1_2_3=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1, -1 ), 0 )
        gbSizer1_2.Add( self.textCtrl1_2_3, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.button1_2_4=wx.Button( self, wx.ID_ANY, u"复制", wx.DefaultPosition, wx.Size( 50, -1 ), 0 )
        gbSizer1_2.Add( self.button1_2_4, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gbSizer1.Add( gbSizer1_2, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        gbSizer1_3=wx.GridBagSizer( 0, 0 )
        gbSizer1_3.SetFlexibleDirection( wx.BOTH )
        gbSizer1_3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.button1_3_1=wx.Button( self, wx.ID_ANY, u"转换日期格式为时间戳", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1_3.Add( self.button1_3_1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.textCtrl1_3_2=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50, -1 ), 0 )
        gbSizer1_3.Add( self.textCtrl1_3_2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.staticText1_3_3=wx.StaticText( self, wx.ID_ANY, u"年", wx.DefaultPosition, wx.Size( 20, -1 ), 0 )
        self.staticText1_3_3.Wrap( -1 )
        self.staticText1_3_3.SetFont( wx.Font( 14, 74, 90, 92, False, "微软雅黑" ) )

        gbSizer1_3.Add( self.staticText1_3_3, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.textCtrl1_3_4=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30, -1 ), 0 )
        gbSizer1_3.Add( self.textCtrl1_3_4, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.staticText1_3_5=wx.StaticText( self, wx.ID_ANY, u"月", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticText1_3_5.Wrap( -1 )
        self.staticText1_3_5.SetFont( wx.Font( 14, 74, 90, 92, False, "微软雅黑" ) )

        gbSizer1_3.Add( self.staticText1_3_5, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.textCtrl1_3_6=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30, -1 ), 0 )
        gbSizer1_3.Add( self.textCtrl1_3_6, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.staticText1_3_7=wx.StaticText( self, wx.ID_ANY, u"日", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticText1_3_7.Wrap( -1 )
        self.staticText1_3_7.SetFont( wx.Font( 14, 74, 90, 92, False, "微软雅黑" ) )

        gbSizer1_3.Add( self.staticText1_3_7, wx.GBPosition( 0, 6 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.textCtrl1_3_8=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1, -1 ), wx.Size( 30, -1 ), 0 )
        gbSizer1_3.Add( self.textCtrl1_3_8, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.staticText1_3_9=wx.StaticText( self, wx.ID_ANY, u"时", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticText1_3_9.Wrap( -1 )
        self.staticText1_3_9.SetFont( wx.Font( 14, 74, 90, 92, False, "微软雅黑" ) )

        gbSizer1_3.Add( self.staticText1_3_9, wx.GBPosition( 0, 8 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.textCtrl1_3_10=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30, -1 ), 0 )
        gbSizer1_3.Add( self.textCtrl1_3_10, wx.GBPosition( 0, 9 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.staticText1_3_11=wx.StaticText( self, wx.ID_ANY, u"分", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticText1_3_11.Wrap( -1 )
        self.staticText1_3_11.SetFont( wx.Font( 14, 74, 90, 92, False, "微软雅黑" ) )

        gbSizer1_3.Add( self.staticText1_3_11, wx.GBPosition( 0, 10 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.textCtrl1_3_12=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30, -1 ), 0 )
        gbSizer1_3.Add( self.textCtrl1_3_12, wx.GBPosition( 0, 11 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.staticText1_3_13=wx.StaticText( self, wx.ID_ANY, u"秒", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticText1_3_13.Wrap( -1 )
        self.staticText1_3_13.SetFont( wx.Font( 14, 74, 90, 92, False, "微软雅黑" ) )

        gbSizer1_3.Add( self.staticText1_3_13, wx.GBPosition( 0, 12 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.textCtrl1_3_14=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1_3.Add( self.textCtrl1_3_14, wx.GBPosition( 0, 13 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.button1_3_15=wx.Button( self, wx.ID_ANY, u"复制", wx.DefaultPosition, wx.Size( 50, -1 ), 0 )
        gbSizer1_3.Add( self.button1_3_15, wx.GBPosition( 0, 14 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gbSizer1.Add( gbSizer1_3, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        gbSizer1_4=wx.GridBagSizer( 0, 0 )
        gbSizer1_4.SetFlexibleDirection( wx.BOTH )
        gbSizer1_4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.button1_4_1=wx.Button( self, wx.ID_ANY, u"转换时间戳为日期格式", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1_4.Add( self.button1_4_1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.textCtrl1_4_2=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1, -1 ), 0 )
        gbSizer1_4.Add( self.textCtrl1_4_2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.textCtrl1_4_3=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125, -1 ), 0 )
        gbSizer1_4.Add( self.textCtrl1_4_3, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.button1_4_3=wx.Button( self, wx.ID_ANY, u"复制", wx.Point( -1, -1 ), wx.Size( 50, -1 ), 0 )
        gbSizer1_4.Add( self.button1_4_3, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gbSizer1.Add( gbSizer1_4, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        self.SetSizer( gbSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.button1_1_1.Bind( wx.EVT_BUTTON, self.fun1_1_1 )
        self.button1_1_3.Bind( wx.EVT_BUTTON, self.fun1_1_3 )
        self.button1_1_4.Bind( wx.EVT_BUTTON, self.fun1_1_4 )
        self.button1_2_1.Bind( wx.EVT_BUTTON, self.fun1_2_1 )
        self.button1_2_4.Bind( wx.EVT_BUTTON, self.fun1_2_4 )
        self.button1_3_1.Bind( wx.EVT_BUTTON, self.fun1_3_1 )
        self.button1_3_15.Bind( wx.EVT_BUTTON, self.fun1_3_15 )
        self.button1_4_1.Bind( wx.EVT_BUTTON, self.fun1_4_1 )
        self.button1_4_3.Bind( wx.EVT_BUTTON, self.fun1_4_3 )

        # 默认打开页面时调用初始化方法
        self.fun1_1_1( self )

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class

    def fun1_1_1(self, event):

        # 默认给一个当前时间戳
        self.textCtrl1_1_2.SetValue( str( round( time.time()*1000 ) ) )

        # 默认给时间的年、月、日、时、分、秒给2-7~17,如：2021-01-01 00:00:00
        self.textCtrl1_2_2.SetValue( time.strftime( "%Y-%m-%d %H:%M:%S", time.localtime() ) )

        # 默认给时间的年、月、日、时、分、秒给2-7~17,如：2021-01-01 00:00:00
        self.textCtrl1_3_2.SetValue( time.strftime( "%Y-%m-%d %H:%M:%S", time.localtime() )[0:4] )
        self.textCtrl1_3_4.SetValue( time.strftime( "%Y-%m-%d %H:%M:%S", time.localtime() )[5:7] )
        self.textCtrl1_3_6.SetValue( time.strftime( "%Y-%m-%d %H:%M:%S", time.localtime() )[8:10] )
        self.textCtrl1_3_8.SetValue( time.strftime( "%Y-%m-%d %H:%M:%S", time.localtime() )[11:13] )
        self.textCtrl1_3_10.SetValue( time.strftime( "%Y-%m-%d %H:%M:%S", time.localtime() )[14:16] )
        self.textCtrl1_3_12.SetValue( time.strftime( "%Y-%m-%d %H:%M:%S", time.localtime() )[17:19] )

        # 默认给一个当前时间戳
        self.textCtrl1_4_2.SetValue( str( round( time.time()*1000 ) ) )

    def fun1_1_3(self, event):
        data=self.textCtrl1_1_2.GetValue()
        onCopy( self, data )

    # 清除文本内容
    def fun1_1_4(self, event):
        self.textCtrl1_1_2.Clear()
        self.textCtrl1_2_2.Clear()
        self.textCtrl1_2_3.Clear()
        self.textCtrl1_3_2.Clear()
        self.textCtrl1_3_4.Clear()
        self.textCtrl1_3_6.Clear()
        self.textCtrl1_3_8.Clear()
        self.textCtrl1_3_10.Clear()
        self.textCtrl1_3_12.Clear()
        self.textCtrl1_4_2.Clear()
        self.textCtrl1_4_3.Clear()

    def fun1_2_1(self, event):
        try:
            date=self.textCtrl1_2_2.GetValue()
            self.textCtrl1_2_3.SetValue( date_to_timestamp( date )+"000" )
        except ValueError:
            toastone=wx.MessageDialog( None, "日期格式异常!请输入如下日期格式：2021-06-03 01:21:56", "错误信息提示",
                                       wx.YES_DEFAULT|wx.ICON_QUESTION )
            if toastone.ShowModal()==wx.ID_YES:  # 如果点击了提示框的确定按钮
                toastone.Destroy()  # 则关闭提示框

    def fun1_2_4(self, event):
        data=self.textCtrl1_2_3.GetValue()
        onCopy( self, data )

    def fun1_3_1(self, event):
        try:
            date=self.textCtrl1_3_2.GetValue()+"-"+self.textCtrl1_3_4.GetValue()+"-"+self.textCtrl1_3_6.GetValue()+" "+self.textCtrl1_3_8.GetValue()+":"+self.textCtrl1_3_10.GetValue()+":"+self.textCtrl1_3_12.GetValue()
            self.textCtrl1_3_14.SetValue( date_to_timestamp( date )+"000" )
        except ValueError:
            toastone=wx.MessageDialog( None, "日期格式异常!请输入如下日期格式：2021-06-03 01:21:56", "错误信息提示",
                                       wx.YES_DEFAULT|wx.ICON_QUESTION )
            if toastone.ShowModal()==wx.ID_YES:  # 如果点击了提示框的确定按钮
                toastone.Destroy()  # 则关闭提示框

    def fun1_3_15(self, event):
        data=self.textCtrl1_3_14.GetValue()
        onCopy( self, data )

    def fun1_4_1(self, event):
        try:
            timestamp=self.textCtrl1_4_2.GetValue()
            if len( timestamp ) not in [10, 13]:
                toastone=wx.MessageDialog( None, "时间戳非10位或13位!", "错误信息提示", wx.YES_DEFAULT|wx.ICON_QUESTION )
                if toastone.ShowModal()==wx.ID_YES:  # 如果点击了提示框的确定按钮
                    toastone.Destroy()  # 则关
            else:
                self.textCtrl1_4_3.SetValue( timestamp_to_date( timestamp ) )
        except ValueError:
            toastone=wx.MessageDialog( None, "时间戳格式非法", "错误信息提示", wx.YES_DEFAULT|wx.ICON_QUESTION )
            if toastone.ShowModal()==wx.ID_YES:  # 如果点击了提示框的确定按钮
                toastone.Destroy()  # 则关闭提示框

    def fun1_4_3(self, event):
        data=self.textCtrl1_4_3.GetValue()
        onCopy( self, data )


###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2( wx.Frame ):

    def __init__(self, parent):
        wx.Frame.__init__( self, parent, id=wx.ID_ANY, title=u"json校验(2)", pos=wx.DefaultPosition,
                           size=wx.Size( 1030, 400 ), style=wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        gbSizer2=wx.GridBagSizer( 0, 0 )
        gbSizer2.SetFlexibleDirection( wx.BOTH )
        gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        gbSizer2_1=wx.GridBagSizer( 0, 0 )
        gbSizer2_1.SetFlexibleDirection( wx.BOTH )
        gbSizer2_1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.button2_1_1=wx.Button( self, wx.ID_ANY, u"格式化校验(左_右)", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2_1.Add( self.button2_1_1, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.button2_1_2=wx.Button( self, wx.ID_ANY, u"复制(左)", wx.DefaultPosition, wx.Size( 60, -1 ), 0 )
        gbSizer2_1.Add( self.button2_1_2, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.button2_1_3=wx.Button( self, wx.ID_ANY, u"复制(右)", wx.DefaultPosition, wx.Size( 60, -1 ), 0 )
        gbSizer2_1.Add( self.button2_1_3, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.button2_1_4=wx.Button( self, wx.ID_ANY, u"去除转义(左_左)", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2_1.Add( self.button2_1_4, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.button2_1_5=wx.Button( self, wx.ID_ANY, u"去除空白(右_右)", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2_1.Add( self.button2_1_5, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.button2_1_6=wx.Button( self, wx.ID_ANY, u"清除", wx.DefaultPosition, wx.Size( 50, -1 ), 0 )
        gbSizer2_1.Add( self.button2_1_6, wx.GBPosition( 0, 6 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gbSizer2.Add( gbSizer2_1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        gbSizer2_2=wx.GridBagSizer( 0, 0 )
        gbSizer2_2.SetFlexibleDirection( wx.BOTH )
        gbSizer2_2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.textCtrl2_2_1=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500, 280 ),
                                        wx.TE_MULTILINE )
        gbSizer2_2.Add( self.textCtrl2_2_1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.textCtrl2_2_2=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500, 280 ),
                                        wx.TE_MULTILINE )
        gbSizer2_2.Add( self.textCtrl2_2_2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gbSizer2.Add( gbSizer2_2, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        self.SetSizer( gbSizer2 )
        self.Layout()

        # 状态栏
        self.statusbar2=self.CreateStatusBar()
        # 将状态栏分割为1个部分
        self.statusbar2.SetFieldsCount( 1 )
        # 分割状态栏的比例为3：2：1，用负数表示
        # statusbar2.SetStatusWidths( [-1] )
        # 每部分状态栏显示的值，当鼠标停在menu上时，0号状态栏会临时显示上面menu里的提示信息
        self.statusbar2.SetStatusText( "就绪", 0 )

        self.Centre( wx.BOTH )

        # Connect Events
        self.button2_1_1.Bind( wx.EVT_BUTTON, self.fun2_1_1 )
        self.button2_1_2.Bind( wx.EVT_BUTTON, self.fun2_1_2 )
        self.button2_1_3.Bind( wx.EVT_BUTTON, self.fun2_1_3 )
        self.button2_1_4.Bind( wx.EVT_BUTTON, self.fun2_1_4 )
        self.button2_1_5.Bind( wx.EVT_BUTTON, self.fun2_1_5 )
        self.button2_1_6.Bind( wx.EVT_BUTTON, self.fun2_1_6 )

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def fun2_1_1(self, event):
        try:
            data_json=self.textCtrl2_2_1.GetValue()
            # data_json='{"test01"      :          "abc","test02":                      123}'
            data_json_formated=json_Data_format( data_json )
            self.textCtrl2_2_2.SetValue( data_json_formated )
            # print(self.m_textCtrl9.GetValue())
            # self.m_staticText21.S(data_json_formated)
            # print(self.m_staticText21.GetValue())
            self.statusbar2.SetStatusText( "json校验成功", 0 )
        except Exception as e:
            self.statusbar2.SetStatusText( f"json校验失败,请重新输入，错误为{e}", 0 )
            # print("json校验失败，错误为:",e)

    def fun2_1_2(self, event):
        data=self.textCtrl2_2_1.GetValue()
        onCopy( self, data )

    def fun2_1_3(self, event):
        data=self.textCtrl2_2_2.GetValue()
        onCopy( self, data )

    # 去除转义左_左
    def fun2_1_4(self, event):
        try:
            data_json=self.textCtrl2_2_1.GetValue()
            data_json_res=data_json.replace( r"\n", "" ).replace( r"\t", "" ).replace( r"\r", "" ).replace( r'\"', '"' )
            self.textCtrl2_2_1.SetValue( data_json_res )
            self.statusbar2.SetStatusText( r'去除转义(\n \r \t \"->"）成功', 0 )
        except Exception as e:
            self.statusbar2.SetStatusText( f"json校验失败,请重新输入，错误为{e}", 0 )

    ##去除空白右到右
    def fun2_1_5(self, event):
        try:
            data_json=self.textCtrl2_2_2.GetValue()
            data_json_formated=json_Data_format2( data_json ).replace( " ", "" )
            self.textCtrl2_2_2.SetValue( data_json_formated )
            self.statusbar2.SetStatusText( "去除空白成功", 0 )
        except Exception as e:
            self.statusbar2.SetStatusText( f"json校验失败,请重新输入，错误为{e}", 0 )

    def fun2_1_6(self, event):
        self.textCtrl2_2_1.Clear()
        self.textCtrl2_2_2.Clear()


###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3( wx.Frame ):

    def __init__(self, parent):
        wx.Frame.__init__( self, parent, id=wx.ID_ANY, title=u"常用加解密(3)", pos=wx.DefaultPosition,
                           size=wx.Size( 750, 210 ), style=wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        gbSizer3=wx.GridBagSizer( 0, 0 )
        gbSizer3.SetFlexibleDirection( wx.BOTH )
        gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        gbSizer3_1=wx.GridBagSizer( 0, 0 )
        gbSizer3_1.SetFlexibleDirection( wx.BOTH )
        gbSizer3_1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.button3_1_1=wx.Button( self, wx.ID_ANY, u"base64加密(左_右)", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer3_1.Add( self.button3_1_1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.button3_1_2=wx.Button( self, wx.ID_ANY, u"base64解密(右_左)", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer3_1.Add( self.button3_1_2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.button3_1_3=wx.Button( self, wx.ID_ANY, u"MD5加密(左_右)", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer3_1.Add( self.button3_1_3, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.button3_1_4=wx.Button( self, wx.ID_ANY, u"sha256加密(左_右)", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer3_1.Add( self.button3_1_4, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.button3_1_5=wx.Button( self, wx.ID_ANY, u"复制(左)", wx.DefaultPosition, wx.Size( 60, -1 ), 0 )
        gbSizer3_1.Add( self.button3_1_5, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.button3_1_6=wx.Button( self, wx.ID_ANY, u"复制(右)", wx.DefaultPosition, wx.Size( 60, -1 ), 0 )
        gbSizer3_1.Add( self.button3_1_6, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.button3_1_7=wx.Button( self, wx.ID_ANY, u"清除", wx.DefaultPosition, wx.Size( 50, -1 ), 0 )
        gbSizer3_1.Add( self.button3_1_7, wx.GBPosition( 0, 6 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gbSizer3.Add( gbSizer3_1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        gbSizer3_2=wx.GridBagSizer( 0, 0 )
        gbSizer3_2.SetFlexibleDirection( wx.BOTH )
        gbSizer3_2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.textCtrl3_2_1=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350, 100 ),
                                        wx.TE_MULTILINE )
        gbSizer3_2.Add( self.textCtrl3_2_1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.textCtrl3_2_2=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350, 100 ),
                                        wx.TE_MULTILINE )
        gbSizer3_2.Add( self.textCtrl3_2_2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gbSizer3.Add( gbSizer3_2, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        self.SetSizer( gbSizer3 )
        self.Layout()

        # 状态栏
        self.statusbar3=self.CreateStatusBar()
        # 将状态栏分割为1个部分
        self.statusbar3.SetFieldsCount( 1 )
        # 分割状态栏的比例为3：2：1，用负数表示
        # statusbar.SetStatusWidths( [-1] )
        # 每部分状态栏显示的值，当鼠标停在menu上时，0号状态栏会临时显示上面menu里的提示信息
        self.statusbar3.SetStatusText( "就绪", 0 )

        self.Centre( wx.BOTH )

        # Connect Events
        self.button3_1_1.Bind( wx.EVT_BUTTON, self.fun3_1_1 )
        self.button3_1_2.Bind( wx.EVT_BUTTON, self.fun3_1_2 )
        self.button3_1_3.Bind( wx.EVT_BUTTON, self.fun3_1_3 )
        self.button3_1_4.Bind( wx.EVT_BUTTON, self.fun3_1_4 )
        self.button3_1_5.Bind( wx.EVT_BUTTON, self.fun3_1_5 )
        self.button3_1_6.Bind( wx.EVT_BUTTON, self.fun3_1_6 )
        self.button3_1_7.Bind( wx.EVT_BUTTON, self.fun3_1_7 )

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    # base64加密
    def fun3_1_1(self, event):
        self.textCtrl3_2_2.SetValue( base64encode( self, self.textCtrl3_2_1.GetValue() ) )
        self.statusbar3.SetStatusText( "base64加密成功", 0 )

    # base64解密
    def fun3_1_2(self, event):
        try:
            self.textCtrl3_2_1.SetValue( base64decode( self, self.textCtrl3_2_2.GetValue() ) )
            self.statusbar3.SetStatusText( "base64解密成功", 0 )
        except Exception as e:
            self.statusbar3.SetStatusText( f"base64解密失败，错误为{e}", 0 )

    # md5加密
    def fun3_1_3(self, event):
        self.textCtrl3_2_2.SetValue( md5encode( self, self.textCtrl3_2_1.GetValue() ) )
        self.statusbar3.SetStatusText( "md5加密成功", 0 )

    # sha256加密
    def fun3_1_4(self, event):
        self.textCtrl3_2_2.SetValue( sha256encode( self, self.textCtrl3_2_1.GetValue() ) )
        self.statusbar3.SetStatusText( "sha256加密成功", 0 )

    def fun3_1_5(self, event):
        data=self.textCtrl3_2_1.GetValue()
        onCopy( self, data )

    def fun3_1_6(self, event):
        data=self.textCtrl3_2_2.GetValue()
        onCopy( self, data )

    def fun3_1_7(self, event):
        self.textCtrl3_2_1.Clear()
        self.textCtrl3_2_2.Clear()


###########################################################################
## Class MyFrame4
###########################################################################

class MyFrame4( wx.Frame ):

    def __init__(self, parent):
        wx.Frame.__init__( self, parent, id=wx.ID_ANY, title=u"置顶便笺", pos=wx.Point( -1, -1 ), size=wx.Size( 315, 408 ),
                           style=wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        gbSizer4=wx.GridBagSizer( 0, 0 )
        gbSizer4.SetFlexibleDirection( wx.BOTH )
        gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        gbSizer4_1=wx.GridBagSizer( 0, 0 )
        gbSizer4_1.SetFlexibleDirection( wx.BOTH )
        gbSizer4_1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        self.button4_1_1=wx.Button( self, wx.ID_ANY, u"复制", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer4_1.Add( self.button4_1_1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        self.button4_1_2=wx.Button( self, wx.ID_ANY, u"清除", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer4_1.Add( self.button4_1_2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        gbSizer4.Add( gbSizer4_1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        gbSizer4_2=wx.GridBagSizer( 0, 0 )
        gbSizer4_2.SetFlexibleDirection( wx.BOTH )
        gbSizer4_2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.textCtrl4_2_1=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300, 350 ),
                                        wx.TE_MULTILINE )
        gbSizer4_2.Add( self.textCtrl4_2_1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )


        gbSizer4.Add( gbSizer4_2, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )


        # 如果需要部件变大或缩小，可以使用这两个方法
        gbSizer4.AddGrowableCol(0)
        gbSizer4.AddGrowableRow(1)
        gbSizer4_2.AddGrowableCol(0)
        gbSizer4_2.AddGrowableRow(0)

        self.SetSizer( gbSizer4 )
        self.Layout()

        self.Centre( wx.VERTICAL )
        # Connect Events
        self.button4_1_1.Bind( wx.EVT_BUTTON, self.fun4_1_1 )
        self.button4_1_2.Bind( wx.EVT_BUTTON, self.fun4_1_2 )

        #根据桌面分辨率-315
        self.Move( 1605, 0 )


    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def fun4_1_1(self, event):
        data=self.textCtrl4_2_1.GetValue()
        onCopy( self, data )

    def fun4_1_2(self, event):
        self.textCtrl4_2_1.Clear()


# 通用方法
# 时间戳转日期格式
# TODO 10/13位时间戳
def timestamp_to_date(timestamp, format_string="%Y-%m-%d %H:%M:%S"):
    if len( timestamp )==13:
        time_array=time.localtime( int( timestamp )/1000 )
        str_date=time.strftime( format_string, time_array )
    else:
        time_array=time.localtime( int( timestamp ) )
        str_date=time.strftime( format_string, time_array )
    return str_date


# 将时间字符串转换为10位时间戳
def date_to_timestamp(date, format_string="%Y-%m-%d %H:%M:%S"):
    time_array=time.strptime( date, format_string )
    time_stamp=int( time.mktime( time_array ) )
    return str( time_stamp )


# json格式校验
def json_Data_format(source_str):
    j=json.loads( source_str )
    data=json.dumps( j, sort_keys=False, indent=2, separators=(',', ': '), ensure_ascii=False )
    return data


# json格式校验-缩进
def json_Data_format2(source_str):
    j=json.loads( source_str )
    data=json.dumps( j, sort_keys=False, ensure_ascii=False )
    return data


# 复制数据到剪贴板
def onCopy(self, data):
    """"""
    self.dataObj=wx.TextDataObject()
    self.dataObj.SetText( data )
    if wx.TheClipboard.Open():
        wx.TheClipboard.SetData( self.dataObj )
        wx.TheClipboard.Close()
    else:
        wx.MessageBox( "Unable to open the clipboard", "Error" )


# base64加密
def base64encode(self, data):
    bytes_data=data.encode( "utf-8" )
    str_data=base64.b64encode( bytes_data )  # 被编码的参数必须是二进制数据
    return bytes.decode( str_data )


# base64解密
def base64decode(self, data):
    str_data=base64.b64decode( data ).decode( "utf-8" )
    return str_data


# md5加密
def md5encode(self, data):
    return hashlib.md5( data.encode( encoding='UTF-8' ) ).hexdigest()


# sha256加密
def sha256encode(self, data):
    sha256=hashlib.sha256()
    sha256.update( data.encode( 'utf-8' ) )
    return sha256.hexdigest()


app=wx.App()
main=MyFrame( None )
main.Show()
app.MainLoop()
