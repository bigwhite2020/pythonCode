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


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1( wx.Frame ):

    def __init__(self, parent):
        wx.Frame.__init__( self, parent, id=wx.ID_ANY, title=u"测试小工具1.0", pos=wx.DefaultPosition,
                           size=wx.Size( 1222, 792 ), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL| wx.MAXIMIZE_BOX  )
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        gbSizer1 = wx.GridBagSizer( 0, 0 )
        gbSizer1.SetFlexibleDirection( wx.BOTH )
        gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        gbSizer1_1 = wx.GridBagSizer( 0, 0 )
        gbSizer1_1.SetFlexibleDirection( wx.BOTH )
        gbSizer1_1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_button1_1 = wx.Button( self, wx.ID_ANY, u"时间戳转换", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1_1.Add( self.m_button1_1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button1_2 = wx.Button( self, wx.ID_ANY, u"JSON格式化", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1_1.Add( self.m_button1_2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button1_3 = wx.Button( self, wx.ID_ANY, u"加密解密", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1_1.Add( self.m_button1_3, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button1_4 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1_1.Add( self.m_button1_4, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gbSizer1.Add( gbSizer1_1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        gbSizer1_2 = wx.GridBagSizer( 0, 0 )
        gbSizer1_2.SetFlexibleDirection( wx.BOTH )
        gbSizer1_2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_button1_5 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1_2.Add( self.m_button1_5, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button1_6 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1_2.Add( self.m_button1_6, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button1_7 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1_2.Add( self.m_button1_7, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button1_8 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1_2.Add( self.m_button1_8, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gbSizer1.Add( gbSizer1_2, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        self.SetSizer( gbSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button1_1.Bind( wx.EVT_BUTTON, self.button1_1 )
        self.m_button1_2.Bind( wx.EVT_BUTTON, self.button1_2 )
        self.m_button1_3.Bind( wx.EVT_BUTTON, self.button1_3 )
        self.m_button1_4.Bind( wx.EVT_BUTTON, self.button1_4 )
        self.m_button1_5.Bind( wx.EVT_BUTTON, self.button1_5 )
        self.m_button1_6.Bind( wx.EVT_BUTTON, self.button1_6 )
        self.m_button1_7.Bind( wx.EVT_BUTTON, self.button1_7 )
        self.m_button1_8.Bind( wx.EVT_BUTTON, self.button1_8 )

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class


    def button1_1(self, event):
        # self.frame = wx.Frame( None ,title="测试",size=(300,100),pos=(100,100))
        # self.frame.Show()
        main = MyFrame2( None )
        main.Show()
        #print( round( time.time() * 1000 ) )


    def button1_2(self, event):
        # self.frame = wx.Frame( None ,title="测试",size=(300,100),pos=(100,100))
        # self.frame.Show()
        main = MyFrame3( None )
        main.Show()

        # print(round( time.time() * 1000 ))
        # self.m_textCtrl1.SetValue( str( round( time.time() * 1000 ) ) )

    def button1_3(self, event):
        main = MyFrame4( None )
        main.Show()

    def button1_4(self, event):
        event.Skip()

    def button1_5(self, event):
        event.Skip()

    def button1_6(self, event):
        event.Skip()

    def button1_7(self, event):
        event.Skip()

    def button1_8(self, event):
        event.Skip()


###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2( wx.Frame ):

    def __init__(self, parent):
        wx.Frame.__init__( self, parent, id=wx.ID_ANY, title=u"时间戳转换", pos=wx.DefaultPosition, size=wx.Size( 520, 300 ),
                           style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        gbSizer2 = wx.GridBagSizer( 0, 0 )
        gbSizer2.SetFlexibleDirection( wx.BOTH )
        gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        gbSizer2_1 = wx.GridBagSizer( 0, 0 )
        gbSizer2_1.SetFlexibleDirection( wx.BOTH )
        gbSizer2_1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_button2_1 = wx.Button( self, wx.ID_ANY, u"获取当前时间戳", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2_1.Add( self.m_button2_1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl2_1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2_1.Add( self.m_textCtrl2_1, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button2_2 = wx.Button( self, wx.ID_ANY, u"copy", wx.DefaultPosition, wx.Size( 50, -1 ), 0 )
        gbSizer2_1.Add( self.m_button2_2, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button2_3 = wx.Button( self, wx.ID_ANY, u"clear", wx.DefaultPosition, wx.Size( 50, -1 ), 0 )
        gbSizer2_1.Add( self.m_button2_3, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gbSizer2.Add( gbSizer2_1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        gbSizer2_2 = wx.GridBagSizer( 0, 0 )
        gbSizer2_2.SetFlexibleDirection( wx.BOTH )
        gbSizer2_2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_button2_4 = wx.Button( self, wx.ID_ANY, u"转换日期格式为时间戳", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2_2.Add( self.m_button2_4, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl2_2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125, -1 ), 0 )
        gbSizer2_2.Add( self.m_textCtrl2_2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl2_3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1, -1 ), 0 )
        gbSizer2_2.Add( self.m_textCtrl2_3, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button2_5 = wx.Button( self, wx.ID_ANY, u"copy", wx.DefaultPosition, wx.Size( 50, -1 ), 0 )
        gbSizer2_2.Add( self.m_button2_5, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gbSizer2.Add( gbSizer2_2, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        gbSizer2_3 = wx.GridBagSizer( 0, 0 )
        gbSizer2_3.SetFlexibleDirection( wx.BOTH )
        gbSizer2_3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_button2_6 = wx.Button( self, wx.ID_ANY, u"转换时间戳为日期格式", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2_3.Add( self.m_button2_6, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl2_4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125, -1 ), 0 )
        gbSizer2_3.Add( self.m_textCtrl2_4, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl2_5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2_3.Add( self.m_textCtrl2_5, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button2_7 = wx.Button( self, wx.ID_ANY, u"copy", wx.Point( -1, -1 ), wx.Size( 50, -1 ), 0 )
        gbSizer2_3.Add( self.m_button2_7, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gbSizer2.Add( gbSizer2_3, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        self.SetSizer( gbSizer2 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button2_1.Bind( wx.EVT_BUTTON, self.button2_1 )
        self.m_button2_2.Bind( wx.EVT_BUTTON, self.button2_2 )
        self.m_button2_3.Bind( wx.EVT_BUTTON, self.button2_3 )
        self.m_button2_4.Bind( wx.EVT_BUTTON, self.button2_4 )
        self.m_button2_5.Bind( wx.EVT_BUTTON, self.button2_5 )
        self.m_button2_6.Bind( wx.EVT_BUTTON, self.button2_6 )
        self.m_button2_7.Bind( wx.EVT_BUTTON, self.button2_7 )

        # 默认给一个当前时间戳
        self.m_textCtrl2_1.SetValue( str( round( time.time() * 1000 ) ) )
        self.m_textCtrl2_4.SetValue( str( round( time.time() * 1000 ) ) )
        #默认给当前日期格式
        self.m_textCtrl2_2.SetValue(time.strftime( "%Y-%m-%d %H:%M:%S", time.localtime() ))

    def __del__(self):
            pass

    # Virtual event handlers, overide them in your derived class


    def button2_1(self, event):
        self.m_textCtrl2_1.SetValue( str( round( time.time() * 1000 ) ) )


    def button2_2(self, event):
        data=self.m_textCtrl2_1.GetValue()
        onCopy(self,data)

    #清除文本内容
    def button2_3(self, event):
        self.m_textCtrl2_1.Clear()
        self.m_textCtrl2_2.Clear()
        self.m_textCtrl2_3.Clear()
        self.m_textCtrl2_4.Clear()
        self.m_textCtrl2_5.Clear()

    def button2_4(self, event):
        try:
            date = self.m_textCtrl2_2.GetValue()
            self.m_textCtrl2_3.SetValue( date_to_timestamp( date ) )
        except ValueError:
            toastone = wx.MessageDialog( None, "日期格式异常!请输入如下日期格式：2021-06-03 01:21:56", "错误信息提示",
                                     wx.YES_DEFAULT | wx.ICON_QUESTION )
            if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                toastone.Destroy()  # 则关闭提示框

    def button2_5(self, event):
        data=self.m_textCtrl2_3.GetValue()
        onCopy(self,data)

    def button2_6(self, event):
        try:
            timestamp = self.m_textCtrl2_4.GetValue()
            if len( timestamp ) not in [10, 13]:
                toastone = wx.MessageDialog( None, "时间戳非10位或13位!", "错误信息提示", wx.YES_DEFAULT | wx.ICON_QUESTION )
                if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                    toastone.Destroy()  # 则关
            else:
                self.m_textCtrl2_5.SetValue( timestamp_to_date( timestamp ) )
        except ValueError:
            toastone = wx.MessageDialog( None, "时间戳格式非法", "错误信息提示", wx.YES_DEFAULT | wx.ICON_QUESTION )
            if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                toastone.Destroy()  # 则关闭提示框

    def button2_7(self, event):
        data=self.m_textCtrl2_5.GetValue()
        onCopy(self,data)


###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3( wx.Frame ):

    def __init__(self, parent):
        wx.Frame.__init__( self, parent, id=wx.ID_ANY, title=u"json校验", pos=wx.DefaultPosition,
                           size=wx.Size( 1200, 800 ), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        gbSizer3 = wx.GridBagSizer( 0, 0 )
        gbSizer3.SetFlexibleDirection( wx.BOTH )
        gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        gbSizer3_1 = wx.GridBagSizer( 0, 0 )
        gbSizer3_1.SetFlexibleDirection( wx.BOTH )
        gbSizer3_1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_button3_1 = wx.Button( self, wx.ID_ANY, u"格式化校验", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer3_1.Add( self.m_button3_1, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button3_2 = wx.Button( self, wx.ID_ANY, u"copy", wx.DefaultPosition, wx.Size( 50, -1 ), 0 )
        gbSizer3_1.Add( self.m_button3_2, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button3_3 = wx.Button( self, wx.ID_ANY, u"clear", wx.DefaultPosition, wx.Size( 50, -1 ), 0 )
        gbSizer3_1.Add( self.m_button3_3, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button3_4 = wx.Button( self, wx.ID_ANY, u"去除空白空行", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer3_1.Add( self.m_button3_4, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button3_5 = wx.Button( self, wx.ID_ANY, u"导入json(预留)", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer3_1.Add( self.m_button3_5, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gbSizer3.Add( gbSizer3_1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        bSizer3_2 = wx.BoxSizer( wx.VERTICAL )

        self.m_textCtrl3_1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 1000, 600 ),
                                          wx.TE_MULTILINE )
        bSizer3_2.Add( self.m_textCtrl3_1, 0, wx.ALL, 5 )

        gbSizer3.Add( bSizer3_2, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        self.SetSizer( gbSizer3 )
        self.Layout()

        # 状态栏
        self.statusbar = self.CreateStatusBar()
        # 将状态栏分割为1个部分
        self.statusbar.SetFieldsCount( 1 )
        # 分割状态栏的比例为3：2：1，用负数表示
        # statusbar.SetStatusWidths( [-1] )
        # 每部分状态栏显示的值，当鼠标停在menu上时，0号状态栏会临时显示上面menu里的提示信息
        self.statusbar.SetStatusText( "就绪", 0 )

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button3_1.Bind( wx.EVT_BUTTON, self.button3_1 )
        self.m_button3_2.Bind( wx.EVT_BUTTON, self.button3_2 )
        self.m_button3_3.Bind( wx.EVT_BUTTON, self.button3_3 )
        self.m_button3_4.Bind( wx.EVT_BUTTON, self.button3_4 )
        self.m_button3_5.Bind( wx.EVT_BUTTON, self.button3_5 )


    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def button3_1(self, event):
        try:
            data_json = self.m_textCtrl3_1.GetValue()
            # data_json='{"test01"      :          "abc","test02":                      123}'
            data_json_formated = json_Data_format( data_json )
            self.m_textCtrl3_1.SetValue( data_json_formated )
            # print(self.m_textCtrl9.GetValue())
            # self.m_staticText21.S(data_json_formated)
            # print(self.m_staticText21.GetValue())
            self.statusbar.SetStatusText( "json校验成功", 0 )
        except Exception as e:
            self.statusbar.SetStatusText( f"json校验失败,请重新输入，错误为{e}", 0 )
            # print("json校验失败，错误为:",e)

    def button3_2(self, event):
        data=self.m_textCtrl3_1.GetValue()
        onCopy(self,data)

    def button3_3(self, event):
        self.m_textCtrl3_1.Clear()

    def button3_4(self, event):
        try:
            data_json = self.m_textCtrl3_1.GetValue()
            data_json_formated = json_Data_format2( data_json )
            self.m_textCtrl3_1.SetValue( data_json_formated )
        except Exception as e:
            self.statusbar.SetStatusText( f"json校验失败,请重新输入，错误为{e}", 0 )

    def button3_5(self, event):
        event.Skip()


###########################################################################
## Class MyFrame4
###########################################################################

class MyFrame4( wx.Frame ):

    def __init__(self, parent):
        wx.Frame.__init__( self, parent, id=wx.ID_ANY, title=u"加密工具", pos=wx.DefaultPosition,
                           size=wx.Size( 750, 280 ), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        gbSizer4 = wx.GridBagSizer( 0, 0 )
        gbSizer4.SetFlexibleDirection( wx.BOTH )
        gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        gbSizer4_1 = wx.GridBagSizer( 0, 0 )
        gbSizer4_1.SetFlexibleDirection( wx.BOTH )
        gbSizer4_1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_button4_1 = wx.Button( self, wx.ID_ANY, u"base64加密", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer4_1.Add( self.m_button4_1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button4_2 = wx.Button( self, wx.ID_ANY, u"base64解密", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer4_1.Add( self.m_button4_2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button4_3 = wx.Button( self, wx.ID_ANY, u"MD5加密", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer4_1.Add( self.m_button4_3, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button4_4 = wx.Button( self, wx.ID_ANY, u"sha256 加密", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer4_1.Add( self.m_button4_4, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button4_5 = wx.Button( self, wx.ID_ANY, u"copy", wx.DefaultPosition, wx.Size( 50, -1 ), 0  )
        gbSizer4_1.Add( self.m_button4_5, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button4_6 = wx.Button( self, wx.ID_ANY, u"clear", wx.DefaultPosition, wx.Size( 50, -1 ), 0 )
        gbSizer4_1.Add( self.m_button4_6, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


        gbSizer4.Add( gbSizer4_1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        gbSizer4_2 = wx.GridBagSizer( 0, 0 )
        gbSizer4_2.SetFlexibleDirection( wx.BOTH )
        gbSizer4_2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_textCtrl4_1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350, 150 ), 0 )
        gbSizer4_2.Add( self.m_textCtrl4_1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl4_2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350, 150 ), 0 )
        gbSizer4_2.Add( self.m_textCtrl4_2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gbSizer4.Add( gbSizer4_2, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        self.SetSizer( gbSizer4 )
        self.Layout()

        # 状态栏
        self.statusbar = self.CreateStatusBar()
        # 将状态栏分割为1个部分
        self.statusbar.SetFieldsCount(1)
        # 分割状态栏的比例为3：2：1，用负数表示
        #statusbar.SetStatusWidths( [-1] )
        # 每部分状态栏显示的值，当鼠标停在menu上时，0号状态栏会临时显示上面menu里的提示信息
        self.statusbar.SetStatusText( "就绪", 0)

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button4_1.Bind( wx.EVT_BUTTON, self.button4_1 )
        self.m_button4_2.Bind( wx.EVT_BUTTON, self.button4_2 )
        self.m_button4_3.Bind( wx.EVT_BUTTON, self.button4_3 )
        self.m_button4_4.Bind( wx.EVT_BUTTON, self.button4_4 )
        self.m_button4_5.Bind( wx.EVT_BUTTON, self.button4_5 )
        self.m_button4_6.Bind( wx.EVT_BUTTON, self.button4_6 )

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    #base64加密
    def button4_1(self, event):
        self.m_textCtrl4_2.SetValue(base64encode(self,self.m_textCtrl4_1.GetValue()))
        self.statusbar.SetStatusText( "base64加密成功", 0 )

    #base64解密
    def button4_2(self, event):
        try:
            self.m_textCtrl4_2.SetValue( base64decode( self, self.m_textCtrl4_1.GetValue() ) )
            self.statusbar.SetStatusText( "base64解密成功", 0 )
        except Exception as e:
            self.statusbar.SetStatusText( f"base64解密失败，错误为{e}", 0 )

    #md5加密
    def button4_3(self, event):
        self.m_textCtrl4_2.SetValue(md5encode(self,self.m_textCtrl4_1.GetValue()))
        self.statusbar.SetStatusText( "md5加密成功", 0 )

    #sha256加密
    def button4_4(self, event):
        self.m_textCtrl4_2.SetValue(sha256encode(self,self.m_textCtrl4_1.GetValue()))
        self.statusbar.SetStatusText( "sha256加密成功", 0 )

    def button4_5(self, event):
        data = self.m_textCtrl4_2.GetValue()
        onCopy(self,data)

    def button4_6(self, event):
        self.m_textCtrl4_1.Clear()
        self.m_textCtrl4_2.Clear()


#通用方法
# 时间戳转日期格式
# TODO 10/13位时间戳
def timestamp_to_date(timestamp, format_string="%Y-%m-%d %H:%M:%S"):
    if len( timestamp ) == 13:
        time_array = time.localtime( int( timestamp ) / 1000 )
        str_date = time.strftime( format_string, time_array )
    else:
        time_array = time.localtime( int( timestamp ) )
        str_date = time.strftime( format_string, time_array )
    return str_date


# 将时间字符串转换为10位时间戳
def date_to_timestamp(date, format_string="%Y-%m-%d %H:%M:%S"):
    time_array = time.strptime( date, format_string )
    time_stamp = int( time.mktime( time_array ) )
    return str( time_stamp )


# json格式校验
def json_Data_format(source_str):
    j = json.loads( source_str )
    data = json.dumps( j, sort_keys=False, indent=2, separators=(',', ': '), ensure_ascii=False )
    return data

#json格式校验-缩进
def json_Data_format2(source_str):
    j = json.loads( source_str )
    data = json.dumps( j, sort_keys=False, ensure_ascii=False )
    return data

#复制数据到剪贴板
def onCopy(self, data):
    """"""
    self.dataObj = wx.TextDataObject()
    self.dataObj.SetText(data)
    if wx.TheClipboard.Open():
      wx.TheClipboard.SetData(self.dataObj)
      wx.TheClipboard.Close()
    else:
        wx.MessageBox( "Unable to open the clipboard", "Error" )

#base64加密
def base64encode(self,data):
    bytes_data = data.encode( "utf-8" )
    str_data = base64.b64encode( bytes_data )  # 被编码的参数必须是二进制数据
    return bytes.decode( str_data )

#base64解密
def base64decode(self,data):
    str_data = base64.b64decode( data ).decode( "utf-8" )
    return  str_data

#md5加密
def md5encode(self,data):
    return hashlib.md5( data.encode( encoding='UTF-8' ) ).hexdigest()
#sha256加密
def sha256encode(self, data):
    sha256 = hashlib.sha256()
    sha256.update( data.encode( 'utf-8' ) )
    return sha256.hexdigest()

app = wx.App()
main=MyFrame1(None)
main.Show()
app.MainLoop()