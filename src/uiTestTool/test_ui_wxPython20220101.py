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
## Class MyFrame
###########################################################################

class MyFrame( wx.Frame ):

    def __init__(self, parent):
        wx.Frame.__init__( self, parent, id=wx.ID_ANY, title=u"测试小工具2.0", pos=wx.DefaultPosition,
                           size=wx.Size( 1234, 839 ), style=wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        gbSizer=wx.GridBagSizer( 0, 0 )
        gbSizer.SetFlexibleDirection( wx.BOTH )
        gbSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        gbSizer1=wx.GridBagSizer( 0, 0 )
        gbSizer1.SetFlexibleDirection( wx.BOTH )
        gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText1_1=wx.StaticText( self, wx.ID_ANY, u"时间戳转换", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1_1.Wrap( -1 )
        self.m_staticText1_1.SetFont( wx.Font( 14, 74, 90, 92, False, "微软雅黑" ) )

        gbSizer1.Add( self.m_staticText1_1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button1_2=wx.Button( self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.Size( 50, -1 ), 0 )
        gbSizer1.Add( self.m_button1_2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button1_3=wx.Button( self, wx.ID_ANY, u"清除", wx.DefaultPosition, wx.Size( 50, -1 ), 0 )
        gbSizer1.Add( self.m_button1_3, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gbSizer.Add( gbSizer1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        gbSizer2=wx.GridBagSizer( 0, 0 )
        gbSizer2.SetFlexibleDirection( wx.BOTH )
        gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_button2_1=wx.Button( self, wx.ID_ANY, u"转换时间戳为日期格式", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.m_button2_1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl2_2=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125, -1 ), 0 )
        gbSizer2.Add( self.m_textCtrl2_2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button2_3=wx.Button( self, wx.ID_ANY, u"复制", wx.DefaultPosition, wx.Size( 50, -1 ), 0 )
        gbSizer2.Add( self.m_button2_3, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl2_4=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150, -1 ), 0 )
        gbSizer2.Add( self.m_textCtrl2_4, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button2_5=wx.Button( self, wx.ID_ANY, u"复制", wx.DefaultPosition, wx.Size( 50, -1 ), 0 )
        gbSizer2.Add( self.m_button2_5, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gbSizer.Add( gbSizer2, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        gbSizer3=wx.GridBagSizer( 0, 0 )
        gbSizer3.SetFlexibleDirection( wx.BOTH )
        gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_button3_1=wx.Button( self, wx.ID_ANY, u"转换日期格式为时间戳", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer3.Add( self.m_button3_1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl3_2=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50, -1 ), 0 )
        gbSizer3.Add( self.m_textCtrl3_2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText3_3=wx.StaticText( self, wx.ID_ANY, u"年", wx.DefaultPosition, wx.Size( 20, -1 ), 0 )
        self.m_staticText3_3.Wrap( -1 )
        self.m_staticText3_3.SetFont( wx.Font( 14, 74, 90, 92, False, "微软雅黑" ) )

        gbSizer3.Add( self.m_staticText3_3, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl3_4=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30, -1 ), 0 )
        gbSizer3.Add( self.m_textCtrl3_4, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText3_5=wx.StaticText( self, wx.ID_ANY, u"月", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3_5.Wrap( -1 )
        self.m_staticText3_5.SetFont( wx.Font( 14, 74, 90, 92, False, "微软雅黑" ) )

        gbSizer3.Add( self.m_staticText3_5, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl3_6=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30, -1 ), 0 )
        gbSizer3.Add( self.m_textCtrl3_6, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText3_7=wx.StaticText( self, wx.ID_ANY, u"日", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3_7.Wrap( -1 )
        self.m_staticText3_7.SetFont( wx.Font( 14, 74, 90, 92, False, "微软雅黑" ) )

        gbSizer3.Add( self.m_staticText3_7, wx.GBPosition( 0, 6 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl3_8=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30, -1 ), 0 )
        gbSizer3.Add( self.m_textCtrl3_8, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText3_9=wx.StaticText( self, wx.ID_ANY, u"时", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3_9.Wrap( -1 )
        self.m_staticText3_9.SetFont( wx.Font( 14, 74, 90, 92, False, "微软雅黑" ) )

        gbSizer3.Add( self.m_staticText3_9, wx.GBPosition( 0, 8 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl3_10=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30, -1 ), 0 )
        gbSizer3.Add( self.m_textCtrl3_10, wx.GBPosition( 0, 9 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText3_11=wx.StaticText( self, wx.ID_ANY, u"分", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3_11.Wrap( -1 )
        self.m_staticText3_11.SetFont( wx.Font( 14, 74, 90, 92, False, "微软雅黑" ) )

        gbSizer3.Add( self.m_staticText3_11, wx.GBPosition( 0, 10 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl3_12=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30, -1 ), 0 )
        gbSizer3.Add( self.m_textCtrl3_12, wx.GBPosition( 0, 11 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText3_13=wx.StaticText( self, wx.ID_ANY, u"秒", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3_13.Wrap( -1 )
        self.m_staticText3_13.SetFont( wx.Font( 14, 74, 90, 92, False, "微软雅黑" ) )

        gbSizer3.Add( self.m_staticText3_13, wx.GBPosition( 0, 12 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl3_14=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer3.Add( self.m_textCtrl3_14, wx.GBPosition( 0, 13 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button3_15=wx.Button( self, wx.ID_ANY, u"复制", wx.DefaultPosition, wx.Size( 50, -1 ), 0 )
        gbSizer3.Add( self.m_button3_15, wx.GBPosition( 0, 14 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gbSizer.Add( gbSizer3, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        gbSizer4=wx.GridBagSizer( 0, 0 )
        gbSizer4.SetFlexibleDirection( wx.BOTH )
        gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText4_1=wx.StaticText( self, wx.ID_ANY, u"JSON格式化", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4_1.Wrap( -1 )
        self.m_staticText4_1.SetFont( wx.Font( 14, 74, 90, 92, False, "微软雅黑" ) )

        gbSizer4.Add( self.m_staticText4_1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button4_2=wx.Button( self, wx.ID_ANY, u"清除", wx.DefaultPosition, wx.Size( 50, -1 ), 0 )
        gbSizer4.Add( self.m_button4_2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gbSizer.Add( gbSizer4, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        gbSizer5=wx.GridBagSizer( 0, 0 )
        gbSizer5.SetFlexibleDirection( wx.BOTH )
        gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_button5_1=wx.Button( self, wx.ID_ANY, u"去除转义(左_左)", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer5.Add( self.m_button5_1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button5_2=wx.Button( self, wx.ID_ANY, u"复制(左)", wx.DefaultPosition, wx.Size( 60, -1 ), 0 )
        gbSizer5.Add( self.m_button5_2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button5_3=wx.Button( self, wx.ID_ANY, u"格式化校验(左_右)", wx.DefaultPosition,  wx.DefaultSize, 0)
        gbSizer5.Add( self.m_button5_3, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button5_4=wx.Button( self, wx.ID_ANY, u"复制(右)", wx.DefaultPosition,  wx.Size( 60, -1 ), 0 )
        gbSizer5.Add( self.m_button5_4, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button5_5=wx.Button( self, wx.ID_ANY, u"去除空白(右_右)", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer5.Add( self.m_button5_5, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gbSizer.Add( gbSizer5, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        gbSizer6=wx.GridBagSizer( 0, 0 )
        gbSizer6.SetFlexibleDirection( wx.BOTH )
        gbSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_textCtrl6_1=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500, 350 ),
                                        wx.TE_MULTILINE )
        gbSizer6.Add( self.m_textCtrl6_1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl6_2=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500, 350 ), wx.TE_MULTILINE )
        gbSizer6.Add( self.m_textCtrl6_2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gbSizer.Add( gbSizer6, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        gbSizer7=wx.GridBagSizer( 0, 0 )
        gbSizer7.SetFlexibleDirection( wx.BOTH )
        gbSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText7_1=wx.StaticText( self, wx.ID_ANY, u"常用加解密", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7_1.Wrap( -1 )
        self.m_staticText7_1.SetFont( wx.Font( 14, 74, 90, 92, False, "微软雅黑" ) )

        gbSizer7.Add( self.m_staticText7_1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button7_2=wx.Button( self, wx.ID_ANY, u"清除", wx.DefaultPosition, wx.Size( 50, -1 ), 0 )
        gbSizer7.Add( self.m_button7_2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gbSizer.Add( gbSizer7, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        gbSizer8=wx.GridBagSizer( 0, 0 )
        gbSizer8.SetFlexibleDirection( wx.BOTH )
        gbSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_button8_1=wx.Button( self, wx.ID_ANY, u"base64加密(左_右)", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer8.Add( self.m_button8_1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button8_2=wx.Button( self, wx.ID_ANY, u"base64解密(右_左)", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer8.Add( self.m_button8_2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button8_3=wx.Button( self, wx.ID_ANY, u"MD5加密(左_右)", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer8.Add( self.m_button8_3, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button8_4=wx.Button( self, wx.ID_ANY, u"sha256加密(左_右)", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer8.Add( self.m_button8_4, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button8_5=wx.Button( self, wx.ID_ANY, u"复制(左)", wx.DefaultPosition, wx.Size( 60, -1 ), 0 )
        gbSizer8.Add( self.m_button8_5, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button8_6=wx.Button( self, wx.ID_ANY, u"复制(右)", wx.DefaultPosition, wx.Size( 60, -1 ), 0 )
        gbSizer8.Add( self.m_button8_6, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gbSizer.Add( gbSizer8, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        gbSizer9=wx.GridBagSizer( 0, 0 )
        gbSizer9.SetFlexibleDirection( wx.BOTH )
        gbSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_textCtrl9_1=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500, 100 ), 0 )
        gbSizer9.Add( self.m_textCtrl9_1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl9_2=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500, 100 ), 0 )
        gbSizer9.Add( self.m_textCtrl9_2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gbSizer.Add( gbSizer9, wx.GBPosition( 8, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        self.SetSizer( gbSizer )
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
        self.m_button1_2.Bind( wx.EVT_BUTTON, self.button1_2 )
        self.m_button1_3.Bind( wx.EVT_BUTTON, self.button1_3 )
        self.m_button2_1.Bind( wx.EVT_BUTTON, self.button2_1 )
        self.m_button2_3.Bind( wx.EVT_BUTTON, self.button2_3 )
        self.m_button2_5.Bind( wx.EVT_BUTTON, self.button2_5 )
        self.m_button3_1.Bind( wx.EVT_BUTTON, self.button3_1 )
        self.m_button3_15.Bind( wx.EVT_BUTTON, self.button3_15 )
        self.m_button4_2.Bind( wx.EVT_BUTTON, self.button4_2 )
        self.m_button5_1.Bind( wx.EVT_BUTTON, self.button5_1 )
        self.m_button5_2.Bind( wx.EVT_BUTTON, self.button5_2 )
        self.m_button5_3.Bind( wx.EVT_BUTTON, self.button5_3 )
        self.m_button5_4.Bind( wx.EVT_BUTTON, self._button5_4 )
        self.m_button5_5.Bind( wx.EVT_BUTTON, self.button5_5 )
        self.m_button7_2.Bind( wx.EVT_BUTTON, self.button7_2 )
        self.m_button8_1.Bind( wx.EVT_BUTTON, self.button8_1 )
        self.m_button8_2.Bind( wx.EVT_BUTTON, self.button8_2 )
        self.m_button8_3.Bind( wx.EVT_BUTTON, self.button8_3 )
        self.m_button8_4.Bind( wx.EVT_BUTTON, self.button8_4 )
        self.m_button8_5.Bind( wx.EVT_BUTTON, self.button8_5 )
        self.m_button8_6.Bind( wx.EVT_BUTTON, self.button8_6 )

        self.flush()


    def flush(self):
        # 默认给一个当前时间戳2_2
        self.m_textCtrl2_2.SetValue( str( round( time.time()*1000 ) ) )
        # 默认给时间的年、月、日、时、分、秒给3-2~12,2021-01-01 00:00:00
        self.m_textCtrl3_2.SetValue( time.strftime( "%Y-%m-%d %H:%M:%S", time.localtime() )[0:4] )
        self.m_textCtrl3_4.SetValue( time.strftime( "%Y-%m-%d %H:%M:%S", time.localtime() )[5:7] )
        self.m_textCtrl3_6.SetValue( time.strftime( "%Y-%m-%d %H:%M:%S", time.localtime() )[8:10] )
        self.m_textCtrl3_8.SetValue( time.strftime( "%Y-%m-%d %H:%M:%S", time.localtime() )[11:13] )
        self.m_textCtrl3_10.SetValue( time.strftime( "%Y-%m-%d %H:%M:%S", time.localtime() )[14:16] )
        self.m_textCtrl3_12.SetValue( time.strftime( "%Y-%m-%d %H:%M:%S", time.localtime() )[17:19] )

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def button1_2(self, event):
        #调用刷新的方法
        self.flush()

    def button1_3(self, event):
        # 清除时间戳转换所有文本内容共9个
        self.m_textCtrl2_2.Clear()
        self.m_textCtrl2_4.Clear()
        self.m_textCtrl3_2.Clear()
        self.m_textCtrl3_4.Clear()
        self.m_textCtrl3_6.Clear()
        self.m_textCtrl3_8.Clear()
        self.m_textCtrl3_10.Clear()
        self.m_textCtrl3_12.Clear()
        self.m_textCtrl3_14.Clear()

    #时间戳转日期格式按钮
    def button2_1(self, event):
        try:
            timestamp=self.m_textCtrl2_2.GetValue()
            if len( timestamp ) not in [10, 13]:
                toastone=wx.MessageDialog( None, "时间戳非10位或13位!", "错误信息提示", wx.YES_DEFAULT|wx.ICON_QUESTION )
                if toastone.ShowModal()==wx.ID_YES:  # 如果点击了提示框的确定按钮
                    toastone.Destroy()  # 则关
            else:
                self.m_textCtrl2_4.SetValue( timestamp_to_date( timestamp ) )
        except ValueError:
            toastone=wx.MessageDialog( None, "时间戳格式非法", "错误信息提示", wx.YES_DEFAULT|wx.ICON_QUESTION )
            if toastone.ShowModal()==wx.ID_YES:  # 如果点击了提示框的确定按钮
                toastone.Destroy()  # 则关闭提示框

    def button2_3(self, event):
        data=self.m_textCtrl2_2.GetValue()
        onCopy( self, data )

    def button2_5(self, event):
        data=self.m_textCtrl2_4.GetValue()
        onCopy( self, data )

    #日期格式转时间戳按钮
    def button3_1(self, event):
        try:
            date = self.m_textCtrl3_2.GetValue()+"-"+self.m_textCtrl3_4.GetValue()+"-"+self.m_textCtrl3_6.GetValue()+" "+self.m_textCtrl3_8.GetValue()+":"+self.m_textCtrl3_10.GetValue()+":"+self.m_textCtrl3_12.GetValue()
            self.m_textCtrl3_14.SetValue( date_to_timestamp( date ) +"000")
        except ValueError:
            toastone = wx.MessageDialog( None, "日期格式异常!请输入如下日期格式：2021-06-03 01:21:56", "错误信息提示",
                                     wx.YES_DEFAULT | wx.ICON_QUESTION )
            if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                toastone.Destroy()  # 则关闭提示框

    def button3_15(self, event):
        data=self.m_textCtrl3_14.GetValue()
        onCopy( self, data )

    def button4_2(self, event):
        # 清除JSON格式化所有文本内容共2个
        self.m_textCtrl6_1.Clear()
        self.m_textCtrl6_2.Clear()

    #去除转义左_左
    def button5_1(self, event):
        try:
            data_json= self.m_textCtrl6_1.GetValue()
            data_json_res = data_json.replace(r"\n","").replace(r"\t","").replace(r"\r","").replace(r'\"','"')
            self.m_textCtrl6_1.SetValue(data_json_res)
            self.statusbar.SetStatusText( r'去除转义(\n \r \t \"->"）成功', 0 )
        except Exception as e:
            self.statusbar.SetStatusText( f"json校验失败,请重新输入，错误为{e}", 0 )


    #复制左
    def button5_2(self, event):
        data=self.m_textCtrl6_1.GetValue()
        onCopy( self, data )

    #格式化校验左到右
    def button5_3(self, event):
        try:
            data_json=self.m_textCtrl6_1.GetValue()
            # data_json='{"test01"      :          "abc","test02":                      123}'
            data_json_formated=json_Data_format( data_json )
            self.m_textCtrl6_2.SetValue( data_json_formated )
            # print(self.m_textCtrl9.GetValue())
            # self.m_staticText21.S(data_json_formated)
            # print(self.m_staticText21.GetValue())
            self.statusbar.SetStatusText( "json校验成功", 0 )
        except Exception as e:
            self.statusbar.SetStatusText( f"json校验失败,请重新输入，错误为{e}", 0 )
            # print("json校验失败，错误为:",e)


    # 复制右
    def _button5_4(self, event):
        data=self.m_textCtrl6_2.GetValue()
        onCopy( self, data )

    ##去除空间右到右
    def button5_5(self, event):
        try:
            data_json=self.m_textCtrl6_2.GetValue()
            data_json_formated=json_Data_format2( data_json ).replace(" ","")
            self.m_textCtrl6_2.SetValue( data_json_formated )
            self.statusbar.SetStatusText( "去除空白成功", 0 )
        except Exception as e:
            self.statusbar.SetStatusText( f"json校验失败,请重新输入，错误为{e}", 0 )

    def button7_2(self, event):
        # 清除常用加解密所有文本内容共2个
        self.m_textCtrl9_1.Clear()
        self.m_textCtrl9_2.Clear()

    # base64加密按钮
    def button8_1(self, event):
        self.m_textCtrl9_2.SetValue( base64encode( self, self.m_textCtrl9_1.GetValue() ) )
        self.statusbar.SetStatusText( "base64加密成功", 0 )

    # base64解密按钮
    def button8_2(self, event):
        try:
            self.m_textCtrl9_1.SetValue( base64decode( self, self.m_textCtrl9_2.GetValue() ) )
            self.statusbar.SetStatusText( "base64解密成功", 0 )
        except Exception as e:
            self.statusbar.SetStatusText( f"base64解密失败，错误为{e}", 0 )

    # md5加密按钮
    def button8_3(self, event):
        self.m_textCtrl9_2.SetValue(md5encode(self,self.m_textCtrl9_1.GetValue()))
        self.statusbar.SetStatusText( "md5加密成功", 0 )

    #sha256加密
    def button8_4(self, event):
        self.m_textCtrl9_2.SetValue(sha256encode(self,self.m_textCtrl9_1.GetValue()))
        self.statusbar.SetStatusText( "sha256加密成功", 0 )

    def button8_5(self, event):
        data = self.m_textCtrl9_1.GetValue()
        onCopy(self,data)


    def button8_6(self, event):
        data = self.m_textCtrl9_2.GetValue()
        onCopy(self,data)


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
main=MyFrame(None)
main.Show()
app.MainLoop()